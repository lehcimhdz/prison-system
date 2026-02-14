from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.amazon.aws.hooks.s3 import S3Hook
from datetime import datetime
import pandas as pd
import io

def transform_silver():
    """Reads raw CSVs from Bronze, cleans data, and saves as Parquet to Silver."""
    hook = S3Hook(aws_conn_id='minio_conn')
    bronze_bucket = 'bronze'
    silver_bucket = 'silver'

    if not hook.check_for_bucket(silver_bucket):
        hook.create_bucket(silver_bucket)

    # List today's files
    prefix = f"raw/{datetime.now().strftime('%Y-%m-%d')}/"
    keys = hook.list_keys(bucket_name=bronze_bucket, prefix=prefix)
    
    if not keys:
        print("No files found in Bronze.")
        return

    for key in keys:
        if not key.endswith('.csv'): continue
        
        # Read file
        obj = hook.get_key(key, bronze_bucket)
        df = pd.read_csv(io.BytesIO(obj.get()['Body'].read()))
        
        print(f"Processing {key}, rows: {len(df)}")
        
        # --- Transformations (Business Logic) ---
        
        # 1. Cleanse Persons
        if 'dim_persons.csv' in key:
            # Rule: Ensure proper capitalization
            df['first_name'] = df['first_name'].str.title()
            df['last_name'] = df['last_name'].str.title()
            
        # 2. Validate Wallets (Rule #8, #9)
        if 'dim_wallets.csv' in key:
            # Rule: Balance cannot be negative (in theory, but our dirty data gen makes it possible)
            # Tag invalid records
            df['is_valid'] = df['current_balance'] >= 0
            
        # 3. Access Logs (Rule #1, #3)
        if 'fact_access_logs.csv' in key:
            # Enrich: Ensure timestamp is datetime
            df['timestamp'] = pd.to_datetime(df['timestamp'])
            
        # Save as Parquet to Silver
        file_name = key.split('/')[-1].replace('.csv', '.parquet')
        silver_key = f"processed/{datetime.now().strftime('%Y-%m-%d')}/{file_name}"
        
        buffer = io.BytesIO()
        df.to_parquet(buffer, index=False)
        
        print(f"Saving to {silver_bucket}/{silver_key}")
        hook.load_bytes(
            bytes_data=buffer.getvalue(),
            key=silver_key,
            bucket_name=silver_bucket,
            replace=True
        )

with DAG('02_transform_silver', start_date=datetime(2023, 1, 1), schedule_interval='@daily', catchup=False) as dag:
    
    transform_task = PythonOperator(
        task_id='cleanse_and_normalize',
        python_callable=transform_silver
    )

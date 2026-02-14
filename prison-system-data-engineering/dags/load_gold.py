from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.amazon.aws.hooks.s3 import S3Hook
from airflow.providers.postgres.hooks.postgres import PostgresHook
from datetime import datetime
import pandas as pd
import io

def load_gold():
    """Reads Parquet from Silver and loads into PostgreSQL Data Warehouse."""
    s3_hook = S3Hook(aws_conn_id='minio_conn')
    pg_hook = PostgresHook(postgres_conn_id='postgres_default')
    silver_bucket = 'silver'
    
    # Schema Definition (DDL)
    # We create tables if they don't exist
    ddl = """
    CREATE TABLE IF NOT EXISTS dim_persons (
        person_id UUID PRIMARY KEY,
        first_name VARCHAR(100),
        last_name VARCHAR(100),
        dob DATE,
        gender CHAR(1),
        biometric_hash TEXT,
        type VARCHAR(50)
    );
    
    CREATE TABLE IF NOT EXISTS dim_wallets (
        wallet_id VARCHAR(50) PRIMARY KEY,
        inmate_id UUID,
        current_balance DECIMAL(10, 2),
        status VARCHAR(20),
        is_valid BOOLEAN
    );

    CREATE TABLE IF NOT EXISTS fact_access_logs (
        log_id UUID PRIMARY KEY,
        person_id UUID,
        location_id VARCHAR(50),
        timestamp TIMESTAMP,
        direction VARCHAR(10),
        reason TEXT
    );
    
    CREATE TABLE IF NOT EXISTS fact_wallet_transactions (
        transaction_id UUID PRIMARY KEY,
        wallet_id VARCHAR(50),
        amount DECIMAL(10, 2),
        type VARCHAR(20),
        timestamp TIMESTAMP,
        description TEXT
    );
    """
    pg_hook.run(ddl)

    # List transformed files
    prefix = f"processed/{datetime.now().strftime('%Y-%m-%d')}/"
    keys = s3_hook.list_keys(bucket_name=silver_bucket, prefix=prefix)
    
    if not keys:
        print("No files found in Silver.")
        return

    for key in keys:
        if not key.endswith('.parquet'): continue
        
        print(f"Loading {key} to Postgres...")
        
        # Determine table name from filename
        # dim_persons.parquet -> dim_persons
        table_name = key.split('/')[-1].replace('.parquet', '')
        
        # Read Parquet
        obj = s3_hook.get_key(key, silver_bucket)
        df = pd.read_parquet(io.BytesIO(obj.get()['Body'].read()))
        
        # Use simple Pandas to SQL (replace for simplicity in this demo)
        # In prod, we'd use COPY command for bulk load
        engine = pg_hook.get_sqlalchemy_engine()
        df.to_sql(table_name, engine, if_exists='replace', index=False)
        print(f"Loaded {len(df)} rows into {table_name}")

with DAG('03_load_gold', start_date=datetime(2023, 1, 1), schedule_interval='@daily', catchup=False) as dag:
    
    load_task = PythonOperator(
        task_id='load_warehouse',
        python_callable=load_gold
    )

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.amazon.aws.hooks.s3 import S3Hook
from datetime import datetime
import os
import glob

def upload_to_minio():
    """Reads all CSVs from the data generator output and uploads them to MinIO 'bronze' bucket."""
    hook = S3Hook(aws_conn_id='minio_conn')
    bucket_name = 'bronze'
    
    # Ensure bucket exists
    if not hook.check_for_bucket(bucket_name):
        hook.create_bucket(bucket_name)

    # Path to generated files
    # Note: In docker-compose, we mount ./scripts/data_generator to /opt/airflow/scripts/data_generator
    data_dir = '/opt/airflow/scripts/data_generator'
    files = glob.glob(os.path.join(data_dir, '*.csv'))
    
    for file_path in files:
        file_name = os.path.basename(file_path)
        key = f"raw/{datetime.now().strftime('%Y-%m-%d')}/{file_name}"
        
        print(f"Uploading {file_name} to {bucket_name}/{key}...")
        hook.load_file(
            filename=file_path,
            key=key,
            bucket_name=bucket_name,
            replace=True
        )

with DAG('01_ingest_bronze', start_date=datetime(2023, 1, 1), schedule_interval='@daily', catchup=False) as dag:
    
    ingest_task = PythonOperator(
        task_id='upload_csvs_to_minio',
        python_callable=upload_to_minio
    )

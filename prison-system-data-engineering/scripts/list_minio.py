from airflow.providers.amazon.aws.hooks.s3 import S3Hook

hook = S3Hook(aws_conn_id='minio_conn')
print("Keys in Bronze bucket:")
for key in hook.list_keys(bucket_name='bronze'):
    print(key)

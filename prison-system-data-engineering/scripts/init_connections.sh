#!/bin/bash
# Script to initialize Airflow connections and variables

echo "Initializing Airflow Connections..."

# 1. MinIO Connection
# Conn Type: aws
# Login: minioadmin (Access Key)
# Password: minioadmin (Secret Key)
# Extra: {"endpoint_url": "http://minio:9000"}
docker exec prison-system-data-engineering-airflow-scheduler-1 airflow connections add 'minio_conn' \
    --conn-type 'aws' \
    --conn-login 'minioadmin' \
    --conn-password 'minioadmin' \
    --conn-extra '{"endpoint_url": "http://minio:9000"}'

echo "Connections Initialized."

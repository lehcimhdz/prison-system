# Step-by-Step Guide: Building Your First Data Engineering Pipeline

Welcome! This guide will walk you through building a professional data pipeline for the Mexico City Prison System simulation.
We will use **Fake Data** to simulate a real-world environment.

## Phase 1: Environment Setup (What we've done so far)

1.  **Project Structure:** We created a standard folder structure.
    - `dags/`: Where your Airflow workflows live.
    - `scripts/`: Python scripts for tasks like data generation.
    - `docker/`: Infrastructure configuration.
2.  **Infrastructure:** We created a `docker-compose.yml` to spin up:
    - **Airflow:** To schedule and run tasks.
    - **PostgreSQL:** To store the final data.
    - **MinIO:** To store raw files (like an S3 bucket).

### Action Item 1: Start the services
Open your terminal in the project root and run:
```bash
docker-compose up -d
```
*Wait a few minutes for everything to start.*

## Phase 2: Generating Data

We need data to work with. We've provided scripts in `scripts/data_generator/` that use the `Faker` library.

### Action Item 2: Generate Fake Data
Run the following commands to create CSV files:
```bash
# Create a virtual environment first (optional but recommended)
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Run the generators
python scripts/data_generator/generate_inmates.py
python scripts/data_generator/generate_staff.py
python scripts/data_generator/generate_movements.py
```
You should now see `inmates.csv`, `staff.csv`, and `movements.csv` in the `scripts/data_generator/` folder.

## Phase 3: Building Your First ETL DAG

Now comes the fun part. You will write an Airflow DAG (Directed Acyclic Graph) to:
1.  **Extract:** Read the CSV files we just generated.
2.  **Load (Raw):** Upload them to MinIO (Bronze Layer).
3.  **Transform:** Clean the data (e.g., filter out released inmates).
4.  **Load (Warehouse):** Insert the clean data into PostgreSQL.

### Challenge for You:
Create a file `dags/prison_etl.py`.
Start simple:
```python
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def print_hello():
    print("Hello from the Prison System Pipeline!")

with DAG('prison_system_etl', start_date=datetime(2023, 1, 1), schedule_interval='@daily', catchup=False) as dag:
    task1 = PythonOperator(
        task_id='hello_task',
        python_callable=print_hello
    )
```
Go to `http://localhost:8080` (user: airflow, pass: airflow) and see if your DAG appears!

## Next Steps
- Implement the logic to upload files to MinIO using `MinioHook`.
- Implement a task to read from MinIO, clean the data using Pandas, and write to Postgres using `PostgresHook`.

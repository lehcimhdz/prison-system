# Technology Stack Explained

## 1. Apache Airflow (Orchestration)
- **Role:** The "Conductor". It schedules and monitors your workflows.
- **Why:** Industry standard for defining dependencies as code (Python). It handles retries, logging, and alerting.
- **In this project:** We use it to trigger data generation, move files to MinIO, and load data into Postgres.

## 2. PostgreSQL (Data Warehouse & Metadata)
- **Role:** The "Database". Stores the final, clean data for analysis. Also used by Airflow to store its own state.
- **Why:** Robust, open-source relational database. Excellent for structured data.
- **In this project:** Stores tables like `dim_inmates`, `fact_visits`, `dim_staff`.

## 3. MinIO (Object Storage - Data Lake)
- **Role:** The "File System". S3-compatible storage for raw files.
- **Why:** Decouples storage from compute. Cheap, scalable, and standard API.
- **In this project:** Stores the raw CSV/JSON files we generate (`bronze`), and intermediate processed files (`silver`).

## 4. Docker & Docker Compose (Infrastructure)
- **Role:** The "Environment". Packages applications and dependencies into containers.
- **Why:** "It works on my machine" is solved. Ensures consistency across all environments.
- **In this project:** Runs Airflow, Postgres, and MinIO as isolated services that talk to each other.

## 5. Faker (Data Generation)
- **Role:** The "Simulator". Generates realistic fake data.
- **Why:** We need PII (Personally Identifiable Information) like names, addresses, and judicial records for a realistic simulation, but cannot use real data.
- **In this project:** Generates millions of rows of test data.

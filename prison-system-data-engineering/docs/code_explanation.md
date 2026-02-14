# Code Logic & Script Explanation

This document explains the "How" and "Why" of the code provided in `scripts/`.

## 1. Data Generation Scripts (`scripts/data_generator/`)
We use the `Faker` library to generate realistic synthetic data. This is crucial for testing our pipeline without compromising real sensitive data.

### `generate_inmates.py`
**Goal:** Create a master dataset of prisoners (`dim_inmates`).
- **`Faker('es_MX')`**: We initialize Faker with the Mexican locale to get Hispanic names and addresses.
- **`fake.unique.random_number(digits=8)`**: Generates a unique 8-digit ID for each inmate.
- **`cell_block` logic**: We simulate cell blocks (A-D) and cell numbers (1-50) using `random.choice` and `random.randint`.
- **Output:** Writes a CSV file with headers: `inmate_id`, `first_name`, `last_name`, `dob`, etc.

### `generate_staff.py`
**Goal:** Create a list of employees (`dim_staff`).
- **Roles:** We define a list of roles (`Guard`, 'Warden', 'Nurse', etc.) and assign them randomly.
- **Shift:** Randomly assigns 'Morning', 'Evening', or 'Night' shifts.
- **Salary:** Generates a random float between 10k and 50k.

### `generate_movements.py`
**Goal:** Create transactional data (`fact_movements`). This is the "high volume" table.
- **`fake.uuid4()`**: detailed unique identifier for each transaction.
- **`inmate_id`**: Randomly picks an ID. Note: In a real app, we'd ensure this ID exists in the inmates list. Here, we allow random IDs to simulate "dirty data" that our pipeline will need to clean later!
- **Types:** simulates Visits, Commissary purchases, Medical checks, etc.

## 2. Infrastructure Code (`docker-compose.yml`)
**Goal:** Define the services that make up our platform.
- **`x-airflow-common`**: A "template" block (YAML anchor) to avoid repeating configuration for the Scheduler, Webserver, and Triggerer.
- **`postgres`**: The database service. We use standard port `5432`.
- **`minio`**: The object storage service. We map port `9000` (API) and `9001` (Console).
- **`volumes`**: We persist data so it survives container restarts (`postgres-db-volume`, `minio_data`).

## 3. requirements.txt
**Goal:** Define Python dependencies.
- **`apache-airflow`**: The simulation engine.
- **`psycopg2-binary`**: Driver to talk to PostgreSQL.
- **`minio`**: Client library to talk to MinIO/S3.
- **`faker`**: The library used for data generation.

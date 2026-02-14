# System Architecture

## Overview
The architecture follows a standard ELT (Extract, Load, Transform) pattern, designed for scalability and maintainability.

```mermaid
graph LR
    subgraph "Source Systems (Simulated)"
        A[Data Generators] -->|CSV/JSON| B[Raw Data Landing (Local/API)]
    end

    subgraph "Data Lake (MinIO)"
        B -->|Ingest| C[Bronze Layer (Raw)]
        C -->|Cleanse| D[Silver Layer (Cleaned)]
        D -->|Agg| E[Gold Layer (Business Logic)]
    end

    subgraph "Data Warehouse (PostgreSQL)"
        E -->|Load| F[Analytical Tables]
    end

    subgraph "Orchestration & Compute"
        G[Apache Airflow] -->|Triggers| A
        G -->|Orchestrates| C
        G -->|Orchestrates| D
        G -->|Orchestrates| E
        G -->|Orchestrates| F
    end

    subgraph "Consumption"
        F -->|Query| H[BI / Analytics / ML]
    end
```

## Data Flow
1.  **Ingestion:** Python scripts generate fake data (inmates, visits, etc.) effectively acting as our "Source Systems".
2.  **Raw Storage:** Data is ingested into MinIO (S3 compatible) in the `bronze` bucket.
3.  **Processing:** Airflow triggers processing jobs (Python/Spark) to clean and transform data.
4.  **Warehousing:** Processed data is loaded into PostgreSQL for rigorous relational querying and integrity.
5.  **Analysis:** The final data is available for dashboards and reporting.

# Project Folder Structure

This document explains the organization of the codebase.

```
prison-system-data-engineering/
├── dags/                 # Airflow DAGs (Directed Acyclic Graphs) - Your workflows
│   └── example_dag.py
├── plugins/              # Custom Airflow plugins (hooks, operators, sensors)
├── scripts/              # Standalone scripts
│   └── data_generator/   # Scripts to generate fake data (Faker)
├── tests/                # Unit and integration tests
├── docker/               # Dockerfiles for custom images (e.g., airflow with custom reqs)
├── config/               # Configuration files (e.g., airflow.cfg, postgresql.conf)
├── notebooks/            # Jupyter notebooks for data exploration and prototyping
├── src/                  # Source code for reusable modules (ETL logic, utils)
├── docs/                 # Project documentation
├── .gitignore            # Files to ignore in git
├── docker-compose.yml    # Defines the services (Airflow, Postgres, MinIO)
├── requirements.txt      # Python dependencies for the project
└── README.md             # Entry point for the project
```

## Key Directories
- **`dags/`**: The heart of Airflow. Each Python file here represents a workflow.
- **`scripts/data_generator/`**: Since we don't have real prison data, we use Python scripts here to generate realistic fake data.
- **`docker/`**: Contains the definition of our compute environments.
- **`src/`**: Shared logic. If you write a function to clean names, put it here and import it in your DAGs.

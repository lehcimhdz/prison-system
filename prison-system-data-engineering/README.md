# Prison System Data Engineering Pipeline

A comprehensive data engineering project simulating the Mexico City Prison System.
This project is designed for educational purposes to demonstrate a professional, production-ready data pipeline.

## 🎯 Goal
To build a complete data ecosystem that centralizes, secures, and analyzes prison data (inmates, staff, visitors, transactions, etc.) using a modern tech stack.

## 🚀 Tech Stack
- **Orchestration:** Apache Airflow
- **Storage:** PostgreSQL (Metadata & Data Warehouse), MinIO (Object Storage)
- **Processing:** Python, Spark (future), Dask (future)
- **Infrastructure:** Docker, Docker Compose
- **Data Generation:** Faker (Python)

## 📂 Project Structure
See [Folder Structure](docs/folder_structure.md) for a detailed breakdown.

## 🏗 Architecture
See [Architecture](docs/architecture.md) for the high-level design.

## 🚦 Getting Started
1. **Prerequisites:** Docker, Docker Compose, Python 3.9+
2. **Setup:**
   ```bash
   pip install -r requirements.txt
   docker-compose up -d
   ```
3. **Run Data Generator:**
   ```bash
   python scripts/data_generator/generate_inmates.py
   ```

## 📚 Educational Guides
- [Step-by-Step Guide](docs/step_by_step_guide.md)
- [Tech Stack Explained](docs/tech_stack.md)

# Business Logic & Requirements Mapping

This document explains how our codebase directly addresses the 13 critical requirements provided by the user.

## 1. Centralized Identification (Huella Digital)
- **Requirement:** Know who is where, always. Use Biometrics.
- **Implementation:**
    - `dim_persons` table has a `biometric_hash` column.
    - **Code:** `scripts/data_generator/generate_persons.py` generates a unique SHA-256 hash for every person (Inmate, Staff, Visitor).
    - **ETL:** `dags/load_gold.py` loads this into Postgres for querying.

## 2. Visitor Control
- **Requirement:** Register who visits whom and what they bring.
- **Implementation:**
    - `dim_visitors_details` links a visitor to an inmate.
    - **Code:** `generate_persons.py` creates visitor records linked to random inmates.
    - **ETL:** `fact_access_logs` tracks their entry/exit.

## 3. Staff & Role Tracking
- **Requirement:** Track staff by area (cleaners, cooks) and shift.
- **Implementation:**
    - `dim_staff_details` captures `role`, `shift`, and `salary`.
    - **Code:** `generate_persons.py` assigns specific roles like 'Nurse', 'Guard', 'Janitor'.

## 4, 5, 6. Suppliers, Vehicles, & Materials
- **Requirement:** Control external entries linked to contracts.
- **Implementation:**
    - `dim_suppliers` table links companies to `contract_id`.
    - **Code:** `scripts/data_generator/generate_master_data.py` generates suppliers with contract start/end dates.

## 7. Inmate Profile
- **Requirement:** Comprehensive data (health, crime, sentence).
- **Implementation:**
    - `dim_inmates_details` captures `sentence_start`, `crime`, and `status`.
    - **Future:** Add `dim_medical_records` (scaffolded in architecture).

## 8, 9, 10. Financial Wallet (Monedero Electrónico)
- **Requirement:** Cashless system to prevent corruption.
- **Implementation:**
    - **Entities:** `dim_wallets` and `fact_wallet_transactions`.
    - **Code:** `scripts/data_generator/generate_financials.py` creates wallets and simulates:
        - Family Deposits (`DEPOSIT`)
        - Commissary Purchases (`PURCHASE`)
        - Work Payments (`SALARY`)
    - **Logic:** `dags/transform_silver.py` validates that `current_balance` is non-negative.

## 11. discipline & Anti-Corruption
- **Requirement:** Track guard behavior.
- **Implementation:**
    - **Data:** `fact_access_logs` tracks every staff movement. If a guard enters a cell block they aren't assigned to, it's queryable.

## 12. Zoning (Blocks & Cells)
- **Requirement:** Hierarchy of perimeters.
- **Implementation:**
    - `dim_locations` and `dim_cells`.
    - **Code:** `generate_master_data.py` creates Blocks A-D, Cells 001-050, and Common Areas (Gym, Kitchen).

## 13. Scalability
- **Requirement:** Multi-prison support.
- **Implementation:**
    - The data model leverages UUIDs (`person_id`, `wallet_id`), allowing data from multiple facilities to be merged without collision.

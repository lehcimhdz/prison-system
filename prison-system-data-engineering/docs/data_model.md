# Conceptual Data Model - Prison Management System

This document outlines the data model designed to meet the 13 core requirements provided by the user.

## Core Entities
### 1. Person (Master Registry)
- **Concept:** Every human (Inmate, Staff, Visitor, Supplier) is a `Person`.
- **Primary Key:** `person_id` (UUID)
- **Attributes:** `first_name`, `last_name`, `dob`, `gender`, `biometric_hash` (Fingerprint - Req #1).

### 2. Role (Inmate, Staff, Visitor, Supplier)
- **Inmate:** `inmate_id` (FK to Person), `sentence_start`, `sentence_end`, `security_level`, `cell_block_id`.
- **Staff:** `staff_id` (FK to Person), `role` (Guard, Doctor, Cleaner), `shift`, `salary`, `hire_date`.
- **Visitor:** `visitor_id` (FK to Person), `approved_status`, `inmate_relationship` (FK to Inmate).
- **Supplier:** `supplier_id` (FK to Person), `contract_id`, `company_name`, `service_type`.

## Operational Entities
### 3. Facility (Req #12)
- **Blocks:** `block_id`, `name` (A, B, C), `security_level`.
- **Cells:** `cell_id`, `block_id` (FK), `capacity`.
- **Common Areas:** `area_id` (Cafeteria, Workshop, Gym).

### 4. Access Log (Req #1, #3, #4, #5, #12)
- **Concept:** Tracks *every* movement.
- **Attributes:** `log_id`, `person_id` (FK), `timestamp`, `location_id` (Where they are), `direction` (ENTRY/EXIT), `reason`.

## Financial Entities (Req #8, #9, #10)
### 5. Electronic Wallet
- **Concept:** Cashless system.
- **Attributes:** `wallet_id`, `inmate_id` (FK), `balance`, `status` (Active/Frozen).

### 6. Wallet Transaction
- **Concept:** Record of every penny.
- **Attributes:** `transaction_id`, `wallet_id` (FK), `amount` (+/-), `type` (DEPOSIT, PURCHASE, TRANSFER, SALARY), `timestamp`, `description`.

## Detailed Requirements Mapping

| Requirement | Entity / Feature | Description |
| :--- | :--- | :--- |
| **1. Central ID** | `dim_person.biometric_hash` | Unique identifier for everyone. |
| **2. Visitors** | `dim_visitor`, `fact_visits` | Links visitor to inmate and logs items brought. |
| **3. Staff Tracking** | `dim_staff`, `fact_access_logs` | Tracks cleaners/cooks/etc. movement and hours. |
| **4. Suppliers** | `dim_supplier` | Links external workers to contracts. |
| **5. Vehicles** | `dim_vehicle_log` | Tracks vehicles entering/exiting. |
| **6. Materials** | `fact_inventory_log` | Tracks material/arms entry linked to contracts. |
| **7. Inmate Details** | `dim_inmate_profile` | Extended bio: health, education, behavior. |
| **8. Cashless** | `dim_wallet` | Electronic wallet for every inmate. |
| **9. Transactions** | `fact_wallet_transactions` | Ledger of all financial movements. |
| **10. Release** | `proc_release_inmate` | Process to close wallet and return funds. |
| **11. Corruption** | `fact_staff_incident` | Logs disciplinary actions against staff. |
| **12. Zones** | `dim_location` | Hierarchical: Facility -> Block -> Cell. |
| **13. Scalability** | `dim_prison` | Supports multiple prisons in one system. |

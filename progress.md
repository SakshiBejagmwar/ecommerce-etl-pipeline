# E-Commerce ETL Pipeline - Project Progress

---

# Phase 1 - Azure Foundation Setup

## Objective

Set up the Azure environment required for the Enterprise Data Engineering ETL Pipeline.

---

## Resources Created

| Resource | Name |
|----------|------|
| Azure Subscription | Azure Free Trial |
| Resource Group | rg-ecommerce-dev |
| Region | Central India |
| Storage Account | stgecomdatalake001 |
| Container 1 | src-files |
| Container 2 | tgt-files |

---

## Tasks Completed

- Created Azure Free Account
- Verified Azure Subscription
- Created Resource Group
- Created ADLS Gen2 Storage Account
- Enabled Hierarchical Namespace
- Created src-files container
- Created tgt-files container
- Uploaded all source CSV files into src-files

---

## Validation

- Resource Group created successfully
- Storage Account created successfully
- ADLS Gen2 enabled
- Containers created successfully
- Source files uploaded successfully

---

## Technologies Used

- Microsoft Azure
- Azure Data Lake Storage Gen2

---

## Learning Outcomes

- Azure Subscription
- Resource Group
- Azure Storage Account
- ADLS Gen2
- Storage Containers
- Uploading data into ADLS

---

---

# Phase 2 - Azure Data Factory

## Objective

Convert source CSV files stored in ADLS Gen2 into Parquet format using Azure Data Factory.

---

## Resources Created

| Resource | Name |
|----------|------|
| Azure Data Factory | adf-ecommerce001 |
| Linked Service | ls_adls_gen2 |
| Pipeline | pipeline1 |

---

## Tasks Completed

- Created Azure Data Factory
- Created Linked Service
- Created Copy Activity Pipeline
- Converted CSV files into Parquet
- Stored Parquet files into tgt-files/parquet_files

---

## Validation

- Pipeline executed successfully
- Parquet files created successfully
- Pipeline monitoring completed without errors

---

## Technologies Used

- Azure Data Factory
- Azure Data Lake Storage Gen2
- Parquet

---

## Learning Outcomes

- Azure Data Factory
- Linked Service
- Datasets
- Copy Activity
- Pipeline
- Trigger
- Monitoring
- CSV to Parquet Conversion

---

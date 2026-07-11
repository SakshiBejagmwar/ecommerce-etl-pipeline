# E-Commerce Sales Analytics Platform

## Project Overview

This project demonstrates an end-to-end Enterprise Data Engineering ETL Pipeline using Azure, Azure Databricks, Delta Lake, dbt Cloud, Apache Airflow (Docker), and Microsoft Fabric. The pipeline ingests raw e-commerce datasets stored in Azure Data Lake Storage Gen2 (ADLS Gen2), processes them using the Medallion Architecture (Bronze, Silver, and Gold layers), and delivers business-ready data for analytics and reporting.

---

## Business Problem

Organizations receive large volumes of e-commerce transactional data from multiple sources. Processing this raw data into reliable, analytics-ready datasets requires scalable storage, automated ETL pipelines, data quality validation, orchestration, logging, and business intelligence reporting.

This project builds an enterprise-grade ETL pipeline to solve these challenges.

---

## Technology Stack

| Category | Technology |
|----------|------------|
| Cloud Platform | Microsoft Azure |
| Storage | Azure Data Lake Storage Gen2 (ADLS Gen2) |
| Processing | Azure Databricks |
| Language | Python, PySpark, SQL |
| Data Format | Delta Lake |
| Data Modeling | dbt Cloud |
| SQL Engine | Databricks SQL |
| Orchestration | Databricks Workflows, Apache Airflow (Docker) |
| Version Control | Git & GitHub |
| Testing | dbt Tests, Pytest |
| Monitoring | Logging & Audit Framework |
| Reporting | Microsoft Fabric |

---

# High Level Design (HLD)

![](daigrams/HLD.jpeg)

---

# Low Level Design (LLD)

![](daigrams/LLD.jpeg)

---

# Star Schema Data Model

![](daigrams/DMD.jpeg)

---

# List of Tables

![](daigrams/LOT.png)

---

# Medallion Architecture

## Bronze Layer

- Raw data ingestion from ADLS Gen2
- Schema evolution
- Incremental loading
- Watermark implementation
- Audit logging
- Error logging
- Delta Lake storage

---

## Silver Layer

- Data cleansing
- Data validation
- Duplicate removal
- Data standardization
- Surrogate key generation
- SCD Type 2 implementation
- Delta OPTIMIZE
- ZORDER
- VACUUM
- Time Travel

---

## Gold Layer

- Business-ready dimensional models
- Fact and Dimension tables
- KPI marts
- Star schema implementation
- Analytics-ready datasets using dbt Cloud

---

# Pipeline Flow

```
CSV Files
      │
      ▼
Azure Data Lake Storage Gen2
      │
      ▼
Azure Data Factory
(CSV → Parquet)
      │
      ▼
Azure Databricks
      │
      ├── Bronze Layer
      │
      ├── Silver Layer
      │
      ▼
dbt Cloud
(Gold Layer)
      │
      ▼
Microsoft Fabric
(Dashboards & Reports)
```

---

# Pipeline Orchestration

The complete ETL pipeline is orchestrated using:

- Databricks Workflows
- Apache Airflow (Docker)

Pipeline Execution Order:

```
Task 1 → Bronze Layer
        ↓
Task 2 → Silver Layer
        ↓
Task 3 → dbt Gold Models
        ↓
Task 4 → Microsoft Fabric Dashboard Refresh
```

---

# Data Quality Checks

Implemented quality checks include:

- Null value validation
- Duplicate record detection
- Schema validation
- Primary Key validation
- Incremental load validation
- dbt Generic Tests
- dbt Schema Tests

---

# Monitoring & Logging

- Audit Tables
- Error Logging
- Pipeline Execution Logs
- Airflow Logs
- Databricks Job Logs

---

# Project Folder Structure

```
E-Commerce-Sales-Analytics-Platform
│
├── datasets
│
├── databricks
│   ├── Bronze
│   ├── Silver
│   └── Common
│
├── dbt
│   ├── models
│   ├── tests
│   └── dbt_project.yml
│
├── airflow
│   └── dags
│
├── diagrams
│
├── dashboards
│
└── README.md
```

---

# Future Enhancements

- CI/CD using GitHub Actions
- Slack Notifications
- Automated Data Quality Monitoring
- Real-time Streaming using Delta Live Tables
- Unity Catalog Governance

---

# Author

Sakshi Bejagmwar
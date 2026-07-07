# E-Commerce ETL Pipeline - Project Progress

---

## ✅ Phase 1 – Azure Foundation

- Created Azure Resource Group
- Configured ADLS Gen2 Storage Account
- Created `src-files` & `tgt-files` containers
- Uploaded source CSV files

---

## ✅ Phase 2 – Azure Data Factory

- Created Azure Data Factory
- Configured Linked Service
- Built Copy Data Pipeline
- Converted CSV files to Parquet
- Stored Parquet files in ADLS Gen2

---

## ✅ Phase 3 – Databricks Setup

- Created Azure Databricks Workspace
- Configured Unity Catalog
- Created Bronze, Silver & Gold Catalogs/Schemas
- Configured Storage Credential & External Location
- Connected Databricks with ADLS Gen2

---

## ✅ Phase 4 – Bronze Layer

- Loaded Parquet files into Bronze Delta Tables
- Implemented Incremental Loading, Watermark & Schema Evolution
- Implemented Audit & Error Logging
- Validated Bronze Tables

**Tables:** Customers, Orders, Products, Payments, Categories, Sellers

---

## ✅ Phase 5 – Silver Layer

- Cleansed & Validated Bronze Data
- Generated Surrogate Keys
- Implemented SCD Type 2
- Applied OPTIMIZE, ZORDER & VACUUM
- Demonstrated Time Travel

**Tables:** Customers, Orders, Products, Payments, Categories, Sellers, Sales

---

## ✅ Phase 6 – Gold Layer

- Configured DBT with Databricks
- Created Staging, Dimension, Fact & Mart Models
- Built Business KPI Tables
- Validated Gold Tables
- Demonstrated Time Travel
- Exported Gold Delta Tables to ADLS Gen2

**Dimensions:** Customer, Product, Seller, Date

**Fact:** Sales

**Marts:** Daily Sales, Monthly Sales, Yearly Sales, Customer Summary, Order Summary, Seller Summary, Category Summary

**KPIs:** Sales Summary, Customer KPI, Product KPI, Seller KPI, Executive Dashboard

---

## 🚀 Current Status

**End-to-End Azure Data Engineering Pipeline Completed Successfully**
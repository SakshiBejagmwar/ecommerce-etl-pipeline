# E-Commerce ETL Pipeline - Project Progress

---

# ✅ Phase 1 – Azure Foundation Setup

**Objective**
Set up Azure infrastructure for the ETL pipeline.

### Completed
- Created Azure Free Subscription
- Created Resource Group (`rg-ecommerce-dev`)
- Created ADLS Gen2 Storage Account (`stgecomdatalake001`)
- Created `src-files` and `tgt-files` containers
- Uploaded source CSV files

**Technologies**
- Azure
- ADLS Gen2

**Status:** ✅ Completed

---

# ✅ Phase 2 – Azure Data Factory

**Objective**
Convert CSV files to Parquet using Azure Data Factory.

### Completed
- Created Azure Data Factory (`adf-ecommerce001`)
- Configured Linked Service
- Built Copy Data Pipeline
- Converted CSV to Parquet
- Stored Parquet files in ADLS Gen2

**Technologies**
- Azure Data Factory
- ADLS Gen2
- Parquet

**Status:** ✅ Completed

---

# ✅ Phase 3 – Databricks Environment Setup

**Objective**
Configure Databricks and Unity Catalog for the ETL pipeline.

### Completed
- Created Azure Databricks Workspace
- Configured Unity Catalog
- Created Bronze Catalog & Schema
- Configured Storage Credential & External Location
- Connected Databricks with ADLS Gen2

**Technologies**
- Azure Databricks
- Unity Catalog
- ADLS Gen2

**Status:** ✅ Completed

---

# ✅ Phase 4 – Bronze Layer

**Objective**
Load Parquet files into Bronze Delta Tables.

### Completed
- Created reusable Config, Logger & Utilities notebooks
- Loaded all source datasets into Bronze Delta Tables
- Implemented Incremental Loading (Delta MERGE)
- Implemented Audit Logging, Error Logging & Watermarking
- Enabled Schema Evolution
- Validated Bronze tables

**Bronze Tables**
- Customers
- Orders
- Order Payments
- Products
- Product Categories
- Sellers

**Technologies**
- Databricks
- Delta Lake
- Unity Catalog

**Status:** ✅ Completed
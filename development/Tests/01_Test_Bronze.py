# Databricks notebook source
# MAGIC %run /Workspace/E-Commerce-ETL/Common/01_Config

# COMMAND ----------

# MAGIC %run /Workspace/E-Commerce-ETL/Common/02_Utilities

# COMMAND ----------

# ==========================================================
# Project      : E-Commerce Sales Analytics Platform
# Notebook     : 01_Test_Bronze
# Description  : Bronze Layer Testing
# Author       : Sakshi Bejagmwar
# ==========================================================
# Test 1 : Bronze Tables Exist
# ==========================================================

tables = [

    "bronze_customers",
    "bronze_orders",
    "bronze_products",
    "bronze_order_payments",
    "bronze_product_categories",
    "bronze_sellers"

]

for table in tables:

    assert spark.catalog.tableExists(
        f"{CATALOG}.{SCHEMA}.{table}"
    ), f"{table} does not exist"

print("✅ Test 1 Passed : All Bronze tables exist")


# ==========================================================
# Test 2 : Row Count Validation
# ==========================================================

for table in tables:

    row_count = spark.table(
        f"{CATALOG}.{SCHEMA}.{table}"
    ).count()

    assert row_count > 0, f"{table} is empty"

print("✅ Test 2 Passed : All Bronze tables contain data")


# ==========================================================
# Test 3 : Metadata Columns Validation
# ==========================================================

required_columns = [

    "bronze_load_timestamp",
    "bronze_load_date"

]

for table in tables:

    df = spark.table(f"{CATALOG}.{SCHEMA}.{table}")

    for column in required_columns:

        assert column in df.columns, f"{column} missing in {table}"

print("✅ Test 3 Passed : Metadata columns validated")


# ==========================================================
# Test 4 : Audit Log Validation
# ==========================================================

audit_count = spark.table(
    f"{CATALOG}.{SCHEMA}.bronze_audit_log"
).count()

assert audit_count > 0, "Audit Log is empty"

print("✅ Test 4 Passed : Audit Log validation successful")


# ==========================================================
# Test 5 : Error Log Table Exists
# ==========================================================

assert spark.catalog.tableExists(
    f"{CATALOG}.{SCHEMA}.bronze_error_log"
), "Error Log table missing"

print("✅ Test 5 Passed : Error Log table exists")


# ==========================================================
# Test 6 : Watermark Table Exists
# ==========================================================

assert spark.catalog.tableExists(
    f"{CATALOG}.{SCHEMA}.bronze_watermark"
), "Watermark table missing"

print("✅ Test 6 Passed : Watermark table exists")


# ==========================================================
# Test 7 : Watermark Records
# ==========================================================

watermark_count = spark.table(
    f"{CATALOG}.{SCHEMA}.bronze_watermark"
).count()

assert watermark_count > 0, "No watermark records found"

print("✅ Test 7 Passed : Watermark validation successful")


# ==========================================================
# Bronze Testing Completed
# ==========================================================

print("===========================================")
print("✅ ALL BRONZE LAYER TESTS PASSED")
print("===========================================")
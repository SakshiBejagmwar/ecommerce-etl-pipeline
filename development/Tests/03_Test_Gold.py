# Databricks notebook source
# MAGIC %run /Workspace/E-Commerce-ETL/Common/01_Config

# COMMAND ----------

CATALOG = "gold_catalog"
SCHEMA = "gold_sch"

# COMMAND ----------

# ==========================================================
# Project      : E-Commerce Sales Analytics Platform
# Notebook     : 03_Test_Gold
# Description  : Gold Layer Testing
# Author       : Sakshi Bejagmwar
# ==========================================================
# Test 1 : Gold Tables Exist
# ==========================================================

tables = [

    "dim_customer",
    "dim_product",
    "dim_seller",
    "dim_date",
    "fact_sales",
    "daily_sales",
    "monthly_sales",
    "yearly_sales",
    "sales_summary",
    "customer_kpi",
    "product_kpi",
    "seller_kpi",
    "executive_dashboard"

]

for table in tables:

    assert spark.catalog.tableExists(
        f"{CATALOG}.{SCHEMA}.{table}"
    ), f"{table} does not exist"

print("✅ Test 1 Passed : All Gold tables exist")

# ==========================================================
# Test 2 : Row Count Validation
# ==========================================================

for table in tables:

    row_count = spark.table(
        f"{CATALOG}.{SCHEMA}.{table}"
    ).count()

    assert row_count > 0, f"{table} is empty"

print("✅ Test 2 Passed : All Gold tables contain data")

# ==========================================================
# Test 3 : Fact Table Validation
# ==========================================================

fact_count = spark.table(
    f"{CATALOG}.{SCHEMA}.fact_sales"
).count()

assert fact_count > 0

print("✅ Test 3 Passed : Fact Sales validated")

# ==========================================================
# Test 4 : Dimension Tables Validation
# ==========================================================

dimensions = [

    "dim_customer",
    "dim_product",
    "dim_seller",
    "dim_date"

]

for table in dimensions:

    cnt = spark.table(
        f"{CATALOG}.{SCHEMA}.{table}"
    ).count()

    assert cnt > 0

print("✅ Test 4 Passed : Dimension tables validated")

# ==========================================================
# Test 5 : KPI Tables Validation
# ==========================================================

kpis = [

    "sales_summary",
    "customer_kpi",
    "product_kpi",
    "seller_kpi",
    "executive_dashboard"

]

for table in kpis:

    cnt = spark.table(
        f"{CATALOG}.{SCHEMA}.{table}"
    ).count()

    assert cnt > 0

print("✅ Test 5 Passed : KPI tables validated")

# ==========================================================
# Test 6 : Aggregate Tables Validation
# ==========================================================

aggregates = [

    "daily_sales",
    "monthly_sales",
    "yearly_sales"

]

for table in aggregates:

    cnt = spark.table(
        f"{CATALOG}.{SCHEMA}.{table}"
    ).count()

    assert cnt > 0

print("✅ Test 6 Passed : Aggregate tables validated")

# ==========================================================
# Test 7 : Revenue Validation
# ==========================================================

negative_revenue = spark.sql(f"""

SELECT *

FROM {CATALOG}.{SCHEMA}.fact_sales

WHERE revenue < 0

""").count()

assert negative_revenue == 0

print("✅ Test 7 Passed : Revenue validation successful")

# ==========================================================
# Test 8 : Customer Dimension Validation
# ==========================================================

null_customers = spark.sql(f"""

SELECT *

FROM {CATALOG}.{SCHEMA}.dim_customer

WHERE customer_id IS NULL

""").count()

assert null_customers == 0

print("✅ Test 8 Passed : Customer Dimension validated")

# ==========================================================
# Test 9 : Date Dimension Validation
# ==========================================================

null_dates = spark.sql(f"""

SELECT *

FROM {CATALOG}.{SCHEMA}.dim_date

WHERE order_date IS NULL

""").count()

assert null_dates == 0

print("✅ Test 9 Passed : Date Dimension validated")

# ==========================================================
# Test 10 : Executive Dashboard Validation
# ==========================================================

dashboard = spark.table(
    f"{CATALOG}.{SCHEMA}.executive_dashboard"
)

assert dashboard.count() > 0

print("✅ Test 10 Passed : Executive Dashboard validated")

# ==========================================================
# Gold Layer Testing Completed
# ==========================================================

print("==========================================")
print("✅ ALL GOLD LAYER TESTS PASSED")
print("==========================================")
# Databricks notebook source
# MAGIC %run /Workspace/E-Commerce-ETL/Common/01_Config

# COMMAND ----------

CATALOG = "silver_catalog"
SCHEMA = "silver_sch"

# COMMAND ----------

# ==========================================================
# Project      : E-Commerce Sales Analytics Platform
# Notebook     : 02_Test_Silver
# Description  : Silver Layer Testing
# Author       : Sakshi Bejagmwar
# ==========================================================
# Test 1 : Silver Tables Exist
# ==========================================================

tables = [

    "silver_customers",
    "silver_orders",
    "silver_products",
    "silver_order_payments",
    "silver_product_categories",
    "silver_sellers",
    "silver_sales"

]

for table in tables:

    assert spark.catalog.tableExists(
        f"{CATALOG}.{SCHEMA}.{table}"
    ), f"{table} does not exist"

print("✅ Test 1 Passed : All Silver tables exist")

# ==========================================================
# Test 2 : Row Count Validation
# ==========================================================

for table in tables:

    row_count = spark.table(
        f"{CATALOG}.{SCHEMA}.{table}"
    ).count()

    assert row_count > 0, f"{table} is empty"

print("✅ Test 2 Passed : All Silver tables contain data")

# ==========================================================
# Test 3 : Customer Surrogate Key Validation
# ==========================================================

customer_df = spark.table(
    f"{CATALOG}.{SCHEMA}.silver_customers"
)

assert "customer_sk" in customer_df.columns

print("✅ Test 3 Passed : Customer Surrogate Key exists")

# ==========================================================
# Test 4 : Duplicate Customer Validation
# ==========================================================

duplicate_customers = spark.sql(f"""

SELECT customer_id

FROM {CATALOG}.{SCHEMA}.silver_customers

GROUP BY customer_id

HAVING COUNT(*) > 1

""").count()

assert duplicate_customers == 0

print("✅ Test 4 Passed : No duplicate customers")

# ==========================================================
# Test 5 : NULL Customer Validation
# ==========================================================

null_customers = spark.sql(f"""

SELECT *

FROM {CATALOG}.{SCHEMA}.silver_customers

WHERE customer_id IS NULL

""").count()

assert null_customers == 0

print("✅ Test 5 Passed : Customer IDs are not NULL")

# ==========================================================
# Test 6 : SCD Type 2 Columns Validation
# ==========================================================

required_columns = [

    "effective_date",
    "expiry_date",
    "is_current"

]

for col in required_columns:

    assert col in customer_df.columns, f"{col} missing"

print("✅ Test 6 Passed : SCD Type 2 columns exist")

# ==========================================================
# Test 7 : Current Customer Records
# ==========================================================

current_records = spark.sql(f"""

SELECT *

FROM {CATALOG}.{SCHEMA}.silver_customers

WHERE is_current = true

""").count()

assert current_records > 0

print("✅ Test 7 Passed : Current customer records exist")

# ==========================================================
# Test 8 : Silver Sales Validation
# ==========================================================

sales_count = spark.table(
    f"{CATALOG}.{SCHEMA}.silver_sales"
).count()

assert sales_count > 0

print("✅ Test 8 Passed : Silver Sales table contains data")

# ==========================================================
# Test 9 : Payment Table Validation
# ==========================================================

payment_count = spark.table(
    f"{CATALOG}.{SCHEMA}.silver_order_payments"
).count()

assert payment_count > 0

print("✅ Test 9 Passed : Payment table validated")

# ==========================================================
# Test 10 : Product Table Validation
# ==========================================================

product_count = spark.table(
    f"{CATALOG}.{SCHEMA}.silver_products"
).count()

assert product_count > 0

print("✅ Test 10 Passed : Product table validated")

# ==========================================================
# Test 11 : Seller Table Validation
# ==========================================================

seller_count = spark.table(
    f"{CATALOG}.{SCHEMA}.silver_sellers"
).count()

assert seller_count > 0

print("✅ Test 11 Passed : Seller table validated")

# ==========================================================
# Test 12 : Product Categories Validation
# ==========================================================

category_count = spark.table(
    f"{CATALOG}.{SCHEMA}.silver_product_categories"
).count()

assert category_count > 0

print("✅ Test 12 Passed : Product Categories validated")

# ==========================================================
# Silver Layer Testing Completed
# ==========================================================

print("============================================")
print("✅ ALL SILVER LAYER TESTS PASSED SUCCESSFULLY")
print("============================================")
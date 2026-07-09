# Databricks notebook source
# MAGIC %run /Workspace/E-Commerce-ETL/Common/01_Config

# COMMAND ----------

# MAGIC %run /Workspace/E-Commerce-ETL/Common/02_Utilities

# COMMAND ----------

# ==========================================================
# Project      : E-Commerce Sales Analytics Platform
# Notebook     : 04_Test_Utilities
# Description  : Utilities Testing
# Author       : Sakshi Bejagmwar
# ==========================================================
from datetime import datetime

# ==========================================================
# Test 1 : Audit Function Exists
# ==========================================================

assert callable(write_audit)

print("✅ Test 1 Passed : write_audit() exists")

# ==========================================================
# Test 2 : Error Function Exists
# ==========================================================

assert callable(write_error)

print("✅ Test 2 Passed : write_error() exists")

# ==========================================================
# Test 3 : Watermark Function Exists
# ==========================================================

assert callable(update_watermark)

print("✅ Test 3 Passed : update_watermark() exists")

# ==========================================================
# Test 4 : Audit Log Write
# ==========================================================

write_audit(
    table_name="test_table",
    file_name="test.parquet",
    start_time=datetime.now(),
    end_time=datetime.now(),
    rows_read=10,
    rows_loaded=10,
    status="SUCCESS"
)

audit_count = spark.sql(f"""

SELECT *

FROM {CATALOG}.{SCHEMA}.bronze_audit_log

WHERE table_name='test_table'

""").count()

assert audit_count > 0

print("✅ Test 4 Passed : Audit function working")

# ==========================================================
# Test 5 : Error Log Write
# ==========================================================

try:

    raise Exception("Sample Error")

except Exception as e:

    write_error(
        "test_table",
        e
    )

error_count = spark.sql(f"""

SELECT *

FROM {CATALOG}.{SCHEMA}.bronze_error_log

WHERE table_name='test_table'

""").count()

assert error_count > 0

print("✅ Test 5 Passed : Error function working")

# ==========================================================
# Test 6 : Watermark Update
# ==========================================================

update_watermark("test_table")

watermark_count = spark.sql(f"""

SELECT *

FROM {CATALOG}.{SCHEMA}.bronze_watermark

WHERE table_name='test_table'

""").count()

assert watermark_count == 1

print("✅ Test 6 Passed : Watermark updated successfully")

# ==========================================================
# Utilities Testing Completed
# ==========================================================

print("==========================================")
print("✅ ALL UTILITIES TESTS PASSED")
print("==========================================")
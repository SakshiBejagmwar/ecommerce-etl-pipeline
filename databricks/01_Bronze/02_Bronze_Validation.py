# Databricks notebook source
# MAGIC %run ../Common/01_Config.ipynb
# MAGIC
# MAGIC print("=" * 60)
# MAGIC print("Bronze Layer Validation")
# MAGIC print("=" * 60)
# MAGIC
# MAGIC for dataset in datasets:
# MAGIC
# MAGIC     table = dataset["table"]
# MAGIC
# MAGIC     df = spark.table(f"{CATALOG}.{SCHEMA}.{table}")
# MAGIC
# MAGIC     print(f"\nTable : {table}")
# MAGIC     print(f"Row Count : {df.count()}")
# MAGIC     print(f"Columns   : {len(df.columns)}")
# MAGIC
# MAGIC display(
# MAGIC     spark.table(f"{CATALOG}.{SCHEMA}.bronze_audit_log")
# MAGIC )
# MAGIC
# MAGIC display(
# MAGIC     spark.table(f"{CATALOG}.{SCHEMA}.bronze_error_log")
# MAGIC )
# MAGIC
# MAGIC display(
# MAGIC     spark.table(f"{CATALOG}.{SCHEMA}.bronze_watermark")
# MAGIC )
# MAGIC
# Databricks notebook source
# MAGIC %run ../Common/01_Config

# COMMAND ----------

# MAGIC %run ../Common/02_Utilities

# COMMAND ----------

# MAGIC %run ../Common/03_Logger

# COMMAND ----------

logger.info("Gold Layer Started")

spark.sql(f"USE CATALOG {GOLD_CATALOG}")
spark.sql(f"USE SCHEMA {GOLD_SCHEMA}")

logger.info("Gold Layer DBT Models Created Successfully")

gold_tables = [
    "dim_customer",
    "dim_product",
    "dim_seller",
    "dim_date",
    "fact_sales",
    "daily_sales",
    "monthly_sales",
    "yearly_sales",
    "customer_summary",
    "order_summary",
    "seller_summary",
    "category_summary",
    "sales_summary",
    "customer_kpi",
    "product_kpi",
    "seller_kpi",
    "executive_dashboard"
]

for table in gold_tables:
    count = spark.table(f"{GOLD_CATALOG}.{GOLD_SCHEMA}.{table}").count()
    logger.info(f"{table} : {count} records")

logger.info("Gold Layer Completed Successfully")
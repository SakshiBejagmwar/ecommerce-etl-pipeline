# Databricks notebook source
# MAGIC %run /Workspace/E-Commerce-ETL/Common/03_Logger

# COMMAND ----------

# ==========================================================
# Project      : E-Commerce Sales Analytics Platform
# Notebook     : 05_Test_Logger
# Description  : Logger Testing
# Author       : Sakshi Bejagmwar
# ==========================================================
import logging

# ==========================================================
# Test 1 : Logger Exists
# ==========================================================

assert logger is not None

print("✅ Test 1 Passed : Logger object created")

# ==========================================================
# Test 2 : Logger Name
# ==========================================================

assert logger.name == "ECommercePipeline"

print("✅ Test 2 Passed : Logger name validated")

# ==========================================================
# Test 3 : Logger Level
# ==========================================================

assert logger.getEffectiveLevel() == logging.INFO

print("✅ Test 3 Passed : Logger level is INFO")

# ==========================================================
# Test 4 : INFO Logging
# ==========================================================

logger.info("Logger INFO Test")

print("✅ Test 4 Passed : INFO log generated")

# ==========================================================
# Test 5 : WARNING Logging
# ==========================================================

logger.warning("Logger WARNING Test")

print("✅ Test 5 Passed : WARNING log generated")

# ==========================================================
# Test 6 : ERROR Logging
# ==========================================================

logger.error("Logger ERROR Test")

print("✅ Test 6 Passed : ERROR log generated")

# ==========================================================
# Logger Testing Completed
# ==========================================================

print("==========================================")
print("✅ ALL LOGGER TESTS PASSED")
print("==========================================")
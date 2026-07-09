# Databricks notebook source
# MAGIC %run /Workspace/E-Commerce-ETL/Common/04_Slack_Notifications

# COMMAND ----------

# ==========================================================
# Project      : E-Commerce Sales Analytics Platform
# Notebook     : 06_Test_Slack
# Description  : Slack Notification Testing
# Author       : Sakshi Bejagmwar
# ==========================================================
# Test 1 : Success Notification Function Exists
# ==========================================================

assert callable(send_success_notification)

print("✅ Test 1 Passed : Success Notification function exists")

# ==========================================================
# Test 2 : Failure Notification Function Exists
# ==========================================================

assert callable(send_failure_notification)

print("✅ Test 2 Passed : Failure Notification function exists")

# ==========================================================
# Test 3 : Send Success Notification
# ==========================================================

try:

    send_success_notification(
        layer="Testing",
        notebook="06_Test_Slack",
        pipeline="Slack Test Pipeline"
    )

    print("✅ Test 3 Passed : Success notification sent")

except Exception as e:

    raise AssertionError(f"Success notification failed : {str(e)}")

# ==========================================================
# Test 4 : Send Failure Notification
# ==========================================================

try:

    send_failure_notification(
        layer="Testing",
        notebook="06_Test_Slack",
        pipeline="Slack Test Pipeline",
        error="Sample Error for Testing"
    )

    print("✅ Test 4 Passed : Failure notification sent")

except Exception as e:

    raise AssertionError(f"Failure notification failed : {str(e)}")

# ==========================================================
# Slack Testing Completed
# ==========================================================

print("==========================================")
print("✅ ALL SLACK TESTS PASSED")
print("==========================================")
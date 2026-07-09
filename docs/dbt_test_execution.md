# DBT Test Execution Report

## Project

**Project Name:** E-Commerce Sales Analytics Platform

**Testing Tool:** dbt

**Database:** Databricks Delta Lake

**Environment:** Azure Databricks

---

# Objective

The objective of this testing phase is to validate the quality, integrity, consistency, and business correctness of the Gold Layer models developed using DBT.

---

# Models Tested

## Dimension Models

- dim_customer
- dim_product
- dim_seller
- dim_date

---

## Fact Models

- fact_sales

---

## Aggregate Models

- daily_sales
- monthly_sales
- yearly_sales

---

## KPI Models

- sales_summary
- customer_kpi
- product_kpi
- seller_kpi
- executive_dashboard

---

# Generic DBT Tests Implemented

## Unique Tests

- customer_sk
- customer_id
- product_sk
- product_id
- seller_sk
- seller_id
- order_date

---

## Not Null Tests

- Business Keys
- Surrogate Keys
- Revenue
- Total Sales
- KPI Metrics
- Aggregate Columns

---

## Relationship Tests

- fact_sales.customer_id → dim_customer.customer_id

- fact_sales.order_date → dim_date.order_date

---

## Accepted Values Tests

### Quarter

Allowed Values

- 1
- 2
- 3
- 4

### Customer Type

Allowed Values

- New Customer
- Repeat Customer

---

# Custom SQL Tests Implemented

The following business validation tests were implemented.

| Test Name | Purpose |
|------------|----------|
| duplicate_customers | Validate duplicate customer records |
| duplicate_orders | Validate duplicate order records |
| duplicate_products | Validate duplicate products |
| duplicate_sellers | Validate duplicate sellers |
| future_order_date | Validate future dates |
| invalid_payment_installments | Validate payment installments |
| missing_customer_key | Validate foreign keys |
| missing_order_key | Validate foreign keys |
| missing_payment_key | Validate foreign keys |
| revenue_positive | Revenue validation |
| daily_sales_validation | Aggregate validation |
| monthly_sales_validation | Aggregate validation |
| yearly_sales_validation | Aggregate validation |
| sales_summary_validation | KPI validation |
| executive_dashboard_validation | Executive KPI validation |
| customer_kpi_validation | Customer KPI validation |
| product_kpi_validation | Product KPI validation |
| seller_kpi_validation | Seller KPI validation |

---

# Test Execution

Command Executed

```bash
dbt test
```

---

# Test Result Summary

| Metric | Count |
|----------|-------|
| Total Models | 24 |
| Total Data Tests | 75 |
| Passed | 75 |
| Failed | 0 |
| Warnings | 0 |

---

# Validation Outcome

The following validations were successfully completed.

- Generic DBT Tests
- Business Rule Validation
- Fact Table Validation
- Dimension Validation
- KPI Validation
- Aggregate Validation
- Relationship Validation
- Data Quality Validation

---

# Conclusion

All DBT models successfully passed the implemented Generic Tests and Custom SQL Tests.

The Gold Layer data satisfies the defined business rules and quality validations.

The Gold Layer is validated and ready for downstream reporting and dashboard consumption.
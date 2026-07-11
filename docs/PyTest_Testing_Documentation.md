# PyTest Testing Documentation

## Project

**Project Name:** E-Commerce Sales Analytics Platform

**Framework:** PyTest

**Platform:** Azure Databricks

---

# Objective

PyTest was implemented to validate the ETL pipeline components using automated unit and validation tests. The tests verify that the data pipeline produces the expected outputs and that supporting utility components function correctly.

---

# PyTest Structure

```
pytest/
│
├── conftest.py
├── test_bronze.py
├── test_silver.py
├── test_gold.py
├── test_utilities.py
└── test_logger.py
```

---

# Test Files

## 1. conftest.py

### Purpose

Provides common fixtures shared across all PyTest modules.

### Responsibilities

- Creates Spark Session fixture
- Shares common configuration
- Avoids duplicate setup code

---

## 2. test_bronze.py

### Purpose

Validates Bronze Layer ingestion.

### Test Cases

| Test ID | Description | Status |
|----------|-------------|--------|
| BR-01 | Bronze tables exist | PASS |
| BR-02 | Bronze tables contain data | PASS |
| BR-03 | Audit log table exists | PASS |
| BR-04 | Error log table exists | PASS |
| BR-05 | Watermark table exists | PASS |
| BR-06 | Audit log contains records | PASS |
| BR-07 | Watermark table contains records | PASS |

---

## 3. test_silver.py

### Purpose

Validates Silver Layer transformations.

### Test Cases

| Test ID | Description | Status |
|----------|-------------|--------|
| SL-01 | Silver tables exist | PASS |
| SL-02 | Silver tables contain data | PASS |
| SL-03 | Customer surrogate key validation | PASS |
| SL-04 | Duplicate customer validation | PASS |

---

## 4. test_gold.py

### Purpose

Validates Gold Layer business models.

### Test Cases

| Test ID | Description | Status |
|----------|-------------|--------|
| GL-01 | Gold tables exist | PASS |
| GL-02 | Fact table contains data | PASS |
| GL-03 | Revenue validation | PASS |
| GL-04 | Dimension table validation | PASS |
| GL-05 | KPI table validation | PASS |

---

## 5. test_utilities.py

### Purpose

Validates common utility components.

### Test Cases

| Test ID | Description | Status |
|----------|-------------|--------|
| UT-01 | Audit table validation | PASS |
| UT-02 | Error table validation | PASS |
| UT-03 | Watermark table validation | PASS |

---

## 6. test_logger.py

### Purpose

Validates logger configuration.

### Test Cases

| Test ID | Description | Status |
|----------|-------------|--------|
| LG-01 | Logger object created | PASS |
| LG-02 | Logger name validation | PASS |

---

# Execution

Install PyTest

```bash
%pip install pytest
```

Run an individual test file

```python
import pytest

pytest.main([
    "-v",
    "test_bronze.py"
])
```

Run all tests

```python
import pytest

pytest.main([
    "-v"
])
```

---

# Test Summary

| Component | Status |
|-----------|--------|
| Bronze Layer | PASS |
| Silver Layer | PASS |
| Gold Layer | PASS |
| Utilities | PASS |
| Logger | PASS |

---

# Conclusion

PyTest was successfully integrated into the Azure Databricks project to automate validation of the ETL pipeline. The implemented tests verify the existence of data objects, validate row availability, check supporting utility components, and confirm logger configuration.

These automated tests complement the notebook-based validation and DBT data quality tests, helping improve the reliability and maintainability of the E-Commerce Sales Analytics Platform.
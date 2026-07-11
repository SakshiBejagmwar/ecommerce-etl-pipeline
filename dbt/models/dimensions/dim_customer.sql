{{ config(materialized='table') }}
select
    customer_sk,
    customer_id,
    customer_unique_id,
    customer_zip_code_prefix,
    customer_city,
    customer_state,
    effective_date,
    expiry_date,
    is_current
from {{ ref('stg_customers') }}
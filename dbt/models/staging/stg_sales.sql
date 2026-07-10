select
    sales_sk,
    order_sk,
    customer_sk,
    payment_sk,
    order_id,
    customer_id,
    order_status,
    order_purchase_timestamp,
    payment_type,
    payment_installments,
    payment_value
from {{ source('silver','silver_sales') }}
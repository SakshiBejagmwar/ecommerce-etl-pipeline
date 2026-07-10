select
    payment_sk,
    order_id,
    payment_sequential,
    payment_type,
    payment_installments,
    payment_value
from {{ source('silver','silver_order_payments') }}
{{ config(materialized='table') }}

select

    s.sales_sk,

    c.customer_sk,

    o.order_sk,

    p.payment_sk,

    o.order_id,

    o.customer_id,

    o.order_status,

    cast(o.order_purchase_timestamp as date) as order_date,

    o.order_purchase_timestamp,

    p.payment_type,

    p.payment_installments,

    p.payment_value as revenue,

    current_timestamp() as gold_load_timestamp

from {{ ref('stg_sales') }} s

left join {{ ref('stg_customers') }} c
on s.customer_id=c.customer_id

left join {{ ref('stg_orders') }} o
on s.order_id=o.order_id

left join {{ ref('stg_order_payments') }} p
on s.order_id=p.order_id
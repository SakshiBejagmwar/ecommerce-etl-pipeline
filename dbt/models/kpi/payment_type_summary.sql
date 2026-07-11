{{ config(materialized='table') }}

select
    payment_type,
    count(distinct order_id) as total_orders,
    sum(revenue) as total_revenue,
    avg(revenue) as avg_revenue
from {{ ref('fact_sales') }}
group by payment_type
order by total_revenue desc
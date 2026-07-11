{{ config(materialized='table') }}

select
    order_status,
    count(distinct order_id) as total_orders,
    sum(revenue) as total_revenue
from {{ ref('fact_sales') }}
group by order_status
order by total_orders desc
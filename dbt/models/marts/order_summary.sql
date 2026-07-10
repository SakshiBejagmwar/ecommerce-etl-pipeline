{{ config(materialized='table') }}

select

    order_status,

    count(order_id) as total_orders,

    sum(revenue) as total_revenue,

    round(avg(revenue),2) as average_order_value

from {{ ref('fact_sales') }}

group by order_status
{{ config(materialized='table') }}

select

    customer_id,

    count(order_id) as total_orders,

    sum(revenue) as total_revenue,

    round(avg(revenue),2) as average_order_value,

    max(order_date) as last_order_date

from {{ ref('fact_sales') }}

group by customer_id
{{ config(materialized='table') }}

select

sum(revenue) as total_revenue,

count(distinct order_id) as total_orders,

count(distinct customer_id) as total_customers,

round(avg(revenue),2) as average_order_value,

sum(case when order_status='DELIVERED' then 1 else 0 end) as delivered_orders,

sum(case when order_status='CANCELED' then 1 else 0 end) as cancelled_orders

from {{ ref('fact_sales') }}
{{ config(materialized='table') }}

select

order_date,

sum(revenue) total_sales,

count(order_id) total_orders,

avg(revenue) average_order_value

from {{ ref('fact_sales') }}

group by order_date
{{ config(materialized='table') }}

select

year(order_date) year,

month(order_date) month,

sum(revenue) monthly_revenue,

count(order_id) total_orders

from {{ ref('fact_sales') }}

group by

year(order_date),

month(order_date)
{{ config(materialized='table') }}

select

year(order_date) year,

sum(revenue) yearly_revenue,

count(order_id) total_orders

from {{ ref('fact_sales') }}

group by

year(order_date)
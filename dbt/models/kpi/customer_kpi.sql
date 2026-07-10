{{ config(materialized='table') }}

select

customer_id,

count(order_id) as total_orders,

sum(revenue) as total_revenue,

round(avg(revenue),2) as average_order_value,

case
    when count(order_id) > 1 then 'Repeat Customer'
    else 'New Customer'
end as customer_type

from {{ ref('fact_sales') }}

group by customer_id
{{ config(materialized='table') }}

select

    customer_id,

    count(distinct order_id) as total_orders,

    sum(revenue) as total_revenue,

    round(avg(revenue),2) as average_order_value,

    dense_rank() over(
        order by sum(revenue) desc
    ) as customer_rank

from {{ ref('fact_sales') }}

group by customer_id
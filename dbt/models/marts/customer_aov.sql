{{ config(materialized='table') }}

select

    customer_id,

    count(distinct order_id) as total_orders,

    sum(revenue) as total_revenue,

    round(
        sum(revenue) /
        count(distinct order_id),
        2
    ) as average_order_value

from {{ ref('fact_sales') }}

group by customer_id

order by average_order_value desc
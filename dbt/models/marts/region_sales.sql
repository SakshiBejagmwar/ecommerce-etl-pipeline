{{ config(materialized='table') }}

select

    dc.customer_state as region,

    sum(fs.revenue) as total_revenue,

    count(distinct fs.order_id) as total_orders,

    avg(fs.revenue) as average_order_value

from {{ ref('fact_sales') }} fs

left join {{ ref('dim_customer') }} dc
    on fs.customer_sk = dc.customer_sk

group by dc.customer_state

order by total_revenue desc
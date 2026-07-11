{{ config(materialized='table') }}

select

    ds.seller_id,

    ds.seller_city,

    ds.seller_state,

    count(distinct fs.order_id) as total_orders,

    sum(fs.revenue) as total_revenue,

    round(avg(fs.revenue),2) as average_order_value,

    dense_rank() over(
        order by sum(fs.revenue) desc
    ) as seller_rank

from {{ ref('fact_sales') }} fs

left join {{ ref('dim_seller') }} ds
    on fs.seller_sk = ds.seller_sk

group by

    ds.seller_id,
    ds.seller_city,
    ds.seller_state
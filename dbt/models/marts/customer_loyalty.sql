{{ config(materialized='table') }}

with customer_orders as (

    select

        customer_id,

        count(distinct order_id) as total_orders,

        sum(revenue) as total_revenue,

        avg(revenue) as average_order_value

    from {{ ref('fact_sales') }}

    group by customer_id

)

select

    customer_id,

    total_orders,

    total_revenue,

    average_order_value,

    case
        when total_orders = 1 then 'One-Time Customer'
        else 'Repeat Customer'
    end as customer_type

from customer_orders
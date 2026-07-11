{{ config(materialized='table') }}

select distinct

    cast(order_purchase_timestamp as date) as order_date,
    year(order_purchase_timestamp) as year,
    month(order_purchase_timestamp) as month,
    day(order_purchase_timestamp) as day,
    quarter(order_purchase_timestamp) as quarter

from {{ ref('stg_orders') }}

where order_purchase_timestamp is not null
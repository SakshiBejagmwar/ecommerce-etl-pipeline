{{ config(materialized='table') }}

select

seller_state,

count(seller_id) as total_sellers,

count(distinct seller_city) as total_cities

from {{ ref('dim_seller') }}

group by seller_state
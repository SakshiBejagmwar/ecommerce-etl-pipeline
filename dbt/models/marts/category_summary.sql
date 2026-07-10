{{ config(materialized='table') }}

select

    product_category_name,

    count(product_id) as total_products,

    round(avg(product_weight_g),2) as average_weight

from {{ ref('dim_product') }}

group by product_category_name
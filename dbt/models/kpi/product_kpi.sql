{{ config(materialized='table') }}

select

product_category_name,

count(product_id) as total_products,

round(avg(product_weight_g),2) as average_weight,

round(avg(product_length_cm),2) as average_length,

round(avg(product_height_cm),2) as average_height,

round(avg(product_width_cm),2) as average_width

from {{ ref('dim_product') }}

group by product_category_name
select
    category_sk,
    product_category_name,
    product_category_name_english
from {{ source('silver','silver_product_categories') }}
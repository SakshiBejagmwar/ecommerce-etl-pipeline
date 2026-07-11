select
    seller_sk,
    seller_id,
    seller_city,
    seller_state
from {{ source('silver','silver_sellers') }}
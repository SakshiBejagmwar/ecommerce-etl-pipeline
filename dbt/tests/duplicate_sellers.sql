SELECT
    seller_id,
    COUNT(*) AS total_records
FROM {{ ref('dim_seller') }}
GROUP BY seller_id
HAVING COUNT(*) > 1
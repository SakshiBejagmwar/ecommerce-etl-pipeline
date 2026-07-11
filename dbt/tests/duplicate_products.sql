SELECT
    product_id,
    COUNT(*) AS total_records
FROM {{ ref('dim_product') }}
GROUP BY product_id
HAVING COUNT(*) > 1
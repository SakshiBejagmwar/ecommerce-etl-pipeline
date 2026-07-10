SELECT *
FROM {{ ref('product_kpi') }}
WHERE total_products < 0
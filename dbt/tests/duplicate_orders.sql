SELECT
    order_id,
    COUNT(*) AS cnt
FROM {{ ref('fact_sales') }}
GROUP BY order_id
HAVING COUNT(*) > 1
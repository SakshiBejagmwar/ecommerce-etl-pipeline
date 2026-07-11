SELECT
    customer_id,
    COUNT(*) AS cnt
FROM {{ ref('dim_customer') }}
GROUP BY customer_id
HAVING COUNT(*) > 1
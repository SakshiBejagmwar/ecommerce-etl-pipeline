SELECT *
FROM {{ ref('customer_kpi') }}
WHERE total_orders <= 0
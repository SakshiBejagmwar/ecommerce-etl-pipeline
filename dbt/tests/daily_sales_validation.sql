SELECT *
FROM {{ ref('daily_sales') }}
WHERE total_sales < 0
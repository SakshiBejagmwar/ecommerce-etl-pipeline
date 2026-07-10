SELECT *
FROM {{ ref('sales_summary') }}
WHERE total_revenue < 0
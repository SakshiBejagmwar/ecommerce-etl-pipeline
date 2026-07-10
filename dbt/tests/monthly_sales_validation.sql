SELECT *
FROM {{ ref('monthly_sales') }}
WHERE monthly_revenue < 0
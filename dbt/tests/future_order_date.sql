SELECT *
FROM {{ ref('fact_sales') }}
WHERE order_date > CURRENT_DATE
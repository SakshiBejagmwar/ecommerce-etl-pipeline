SELECT *
FROM {{ ref('fact_sales') }}
WHERE payment_installments <= 0
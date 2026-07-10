SELECT *
FROM {{ ref('fact_sales') }}
WHERE order_sk IS NULL
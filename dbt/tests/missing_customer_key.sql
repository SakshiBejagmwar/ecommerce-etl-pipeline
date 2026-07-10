SELECT *
FROM {{ ref('fact_sales') }}
WHERE customer_sk IS NULL
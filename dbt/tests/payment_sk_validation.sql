SELECT *
FROM {{ ref('fact_sales') }}
WHERE payment_sk IS NULL
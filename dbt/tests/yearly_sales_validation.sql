SELECT *
FROM {{ ref('yearly_sales') }}
WHERE yearly_revenue < 0
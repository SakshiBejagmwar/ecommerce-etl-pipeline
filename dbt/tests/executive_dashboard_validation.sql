SELECT *
FROM {{ ref('executive_dashboard') }}
WHERE total_revenue < 0
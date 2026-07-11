SELECT *
FROM {{ ref('seller_kpi') }}
WHERE total_sellers <= 0
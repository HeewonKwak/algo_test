-- https://solvesql.com/problems/day-of-furniture/
WITH T AS (
  SELECT
  order_date,
  COUNT(DISTINCT order_id) AS ALL_ORDER
  FROM records
  GROUP BY order_date HAVING ALL_ORDER >= 10
)


SELECT
r.order_date,
COUNT(DISTINCT r.order_id) AS furniture,
-- T.ALL_ORDER,
ROUND(COUNT(DISTINCT r.order_id) * 100 / T.ALL_ORDER, 2) AS furniture_pct
FROM records r
JOIN T ON (r.order_date = T.order_date)
WHERE category = 'Furniture'
GROUP BY r.order_date HAVING furniture_pct >= 40
ORDER BY furniture_pct DESC, r.order_date
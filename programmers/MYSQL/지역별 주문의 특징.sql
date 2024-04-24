-- https://solvesql.com/problems/characteristics-of-orders/
WITH A AS
(SELECT
region,
-- category
COUNT(DISTINCT order_id) AS F
FROM records
WHERE category IN ("Furniture")
GROUP BY region),
B AS
(SELECT
region,
COUNT(DISTINCT order_id) AS T
FROM records
WHERE category IN ("Technology")
GROUP BY region),
C AS
(SELECT
region,
COUNT(DISTINCT order_id) AS OF
FROM records
WHERE category IN ("Office Supplies")
GROUP BY region)

SELECT
r.region AS Region,
A.F AS Furniture,
C.OF AS "Office Supplies",
B.T AS Technology
FROM records r
LEFT JOIN A ON (r.region = A.region)
LEFT JOIN B ON (r.region = B.region)
LEFT JOIN C ON (r.region = C.region)
GROUP BY r.region
ORDER BY r.region
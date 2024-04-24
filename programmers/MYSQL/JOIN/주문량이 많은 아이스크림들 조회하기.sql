-- https://school.programmers.co.kr/learn/courses/30/lessons/133027

-- 코드를 입력하세요
WITH july_t AS
(SELECT
FLAVOR,
SUM(TOTAL_ORDER) AS TOTAL_ORDER
FROM JULY
GROUP BY FLAVOR)

SELECT
f.FLAVOR
FROM FIRST_HALF f
JOIN july_t j
ON (f.FLAVOR = j.FLAVOR)
ORDER BY f.TOTAL_ORDER + j.TOTAL_ORDER DESC
LIMIT 3
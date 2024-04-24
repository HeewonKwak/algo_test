-- https://solvesql.com/problems/multiple-medalist/
SELECT
a.name
FROM athletes a
JOIN records r ON (a.id = r.athlete_id)
JOIN games g ON (r.game_id = g.id)
WHERE r.medal IS NOT NULL AND g.year >= 2000
GROUP BY a.id HAVING COUNT(DISTINCT r.team_id) > 1
ORDER BY a.name
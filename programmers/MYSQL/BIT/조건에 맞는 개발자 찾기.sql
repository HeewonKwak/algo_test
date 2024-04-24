```
INFO:
NAME: SELECT / 조건에 맞는 개발자 찾기
LEVEL / Correct rate: level2 / 45% 
LINK: https://school.programmers.co.kr/learn/courses/30/lessons/276034
```

SELECT
    DISTINCT(d.ID),
    d.EMAIL,
    d.FIRST_NAME,
    d.LAST_NAME
FROM DEVELOPERS d
WHERE d.SKILL_CODE & (SELECT CODE FROM SKILLCODES WHERE NAME IN ('Python')) 
    OR d.SKILL_CODE & (SELECT CODE FROM SKILLCODES WHERE NAME IN ('C#'))
ORDER BY d.ID
-- 1) 10 records with one without name (1 no-name + 9 with name)
(
    SELECT score, name
    FROM second_table
    WHERE
        name IS NULL
        OR name = ''
    ORDER BY score DESC
    LIMIT 1
)
UNION ALL
(
    SELECT score, name
    FROM second_table
    WHERE
        name IS NOT NULL
        AND name != ''
    ORDER BY score DESC
    LIMIT 9
)
ORDER BY score DESC;

-- 2) 10 records with multiple without name (3 no-name + 7 with name)
(
    SELECT score, name
    FROM second_table
    WHERE
        name IS NULL
        OR name = ''
    ORDER BY score DESC
    LIMIT 3
)
UNION ALL
(
    SELECT score, name
    FROM second_table
    WHERE
        name IS NOT NULL
        AND name != ''
    ORDER BY score DESC
    LIMIT 7
)
ORDER BY score DESC;

-- 3) 10 records, all with name
SELECT score, name
FROM second_table
WHERE
    name IS NOT NULL
    AND name != ''
ORDER BY score DESC
LIMIT 10;
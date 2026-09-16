DROP TABLE IF EXISTS letters;

CREATE TABLE letters (
    position INTEGER,
    char TEXT
);

INSERT INTO letters VALUES
(0, 'l'),
(1, 'e'),
(2, 'e'),
(3, 't'),
(4, 'c'),
(5, 'o'),
(6, 'd'),
(7, 'e');

SELECT
    char,
    COUNT(*) AS char_count
FROM letters
GROUP BY char
ORDER BY char_count DESC;

SELECT
    char,
    COUNT(*) AS char_count
FROM letters
GROUP BY char
HAVING COUNT(*) = 1;


SELECT
    position,
    char
FROM letters
WHERE char IN (
    SELECT
        char
    FROM letters
    GROUP BY char
    HAVING COUNT(*) = 1
)
ORDER BY position
LIMIT 1;


-- Review:
-- GROUP BY char groups the same characters together.
-- COUNT(*) counts how many times each character appears.
-- HAVING COUNT(*) = 1 keeps only characters that appear once.
-- IN subquery checks whether a character is in the unique-character list.
-- ORDER BY position sorts characters by their original order.
-- LIMIT 1 returns the first unique character.

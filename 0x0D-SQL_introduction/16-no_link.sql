-- Shows all records in second_table without a name value sorted by score
SELECT score, name FROM second_table WHERE CHAR_LENGTH(name) > 0 ORDER BY score DESC;

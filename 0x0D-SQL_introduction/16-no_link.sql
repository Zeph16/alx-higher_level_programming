-- Shows all records in second_table without a name value sorted by score
SELECT score, name FROM second_table where name IS NOT NULL ORDER BY score DESC;

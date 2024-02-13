--  a script that lists the number of records with the same score in the table
SELECT score, COUNT(score) as number from second_table ORDER BY score DESC;

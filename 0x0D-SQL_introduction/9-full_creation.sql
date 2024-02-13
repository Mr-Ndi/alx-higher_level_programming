-- a script that creates a table called first_table in the current database.
CREATE TABLE IF NOT EXISTS second_table(
        id int,
        name VARCHAR(256),
        score int
        );

INSERT INTO second_table(id, name, score) VALUES
(1, 'JOHN', 10),
(2, 'Alex', 3),
(3, 'Bob', 14),
(4, 'George', 8);

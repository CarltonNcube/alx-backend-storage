# 0x00. MySQL Advanced

## Back-end
- **SQL**
- **MySQL**


## Resources
- Read or watch:
  - [MySQL cheatsheet](https://devhints.io/mysql)
  - [MySQL Performance: How To Leverage MySQL Database Indexing](https://severalnines.com/database-blog/mysql-database-indexing-tips-best-practices)
  - [Stored Procedure](https://www.mysqltutorial.org/mysql-stored-procedure-tutorial.aspx)
  - [Triggers](https://www.mysqltutorial.org/mysql-triggers.aspx)
  - [Views](https://www.mysqltutorial.org/mysql-views-tutorial.aspx)
  - [Functions and Operators](https://www.mysqltutorial.org/mysql-functions/)
  - [Trigger Syntax and Examples](https://dev.mysql.com/doc/refman/8.0/en/trigger-syntax.html)
  - [CREATE TABLE Statement](https://dev.mysql.com/doc/refman/8.0/en/create-table.html)
  - [CREATE PROCEDURE and CREATE FUNCTION Statements](https://dev.mysql.com/doc/refman/8.0/en/create-procedure.html)
  - [CREATE INDEX Statement](https://dev.mysql.com/doc/refman/8.0/en/create-index.html)
  - [CREATE VIEW Statement](https://dev.mysql.com/doc/refman/8.0/en/create-view.html)



## More Info
### Comments for your SQL file:
```bash
$ cat my_script.sql
-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
SELECT id, name FROM students WHERE batch_id = 3 ORDER BY created_at DESC LIMIT 3;
$

    Use “container-on-demand” to run MySQL
    Credentials in the container: root/root
    How to import a SQL dump:

bash

$ echo "CREATE DATABASE hbtn_0d_tvshows;" | mysql -uroot -p
Enter password: 
$ curl "https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" -s | mysql -uroot -p hbtn_0d_tvshows
Enter password: 
$ echo "SELECT * FROM tv_genres" | mysql -uroot -p hbtn_0d_tvshows
Enter password: 
id  name
1   Drama
2   Mystery
3   Adventure
4   Fantasy
5   Comedy
6   Crime
7   Suspense
8   Thriller
$

Tasks

0. We are all unique!
Write a SQL script that creates a table users following specific requirements.

1. In and not out
Write a SQL script that creates a table users following specific requirements.

2. Best band ever!
Write a SQL script that ranks country origins of bands, ordered by the number of (non-unique) fans.

3. Old school band
Write a SQL script that lists all bands with Glam rock as their main style, ranked by their longevity.

4. Buy buy buy
Write a SQL script that creates a trigger that decreases the quantity of an item after adding a new order.

5. Email validation to sent
Write a SQL script that creates a trigger that resets the attribute valid_email only when the email has been changed.

6. Add bonus
Write a SQL script that creates a stored procedure AddBonus that adds a new correction for a student.

7. Average score
Write a SQL script that creates a stored procedure ComputeAverageScoreForUser that computes and stores the average score for a student.

8. Optimize simple search
Write a SQL script that creates an index idx_name_first on the table names and the first letter of name.

9. Optimize search and score
Write a SQL script that creates an index idx_name_first_score on the table names and the first letter of name


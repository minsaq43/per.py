# SQL / MySQL Notes

## 1. What is SQL?

**SQL (Structured Query Language)** is used to communicate with and manage databases.

With SQL you can:

- Create databases
- Create tables
- Insert data
- Read data
- Update data
- Delete data
- Search/filter data
- Sort data
- Combine data from multiple tables

**MySQL** is a database management system that uses SQL.

---

## 2. Installing MySQL

### Ubuntu / Debian

Open Terminal:

```bash
sudo apt update
```

Install MySQL:

```bash
sudo apt install mysql-server
```

Check installation:

```bash
mysql --version
```

Start MySQL:

```bash
sudo systemctl start mysql
```

Enable MySQL to start automatically:

```bash
sudo systemctl enable mysql
```

Check its status:

```bash
sudo systemctl status mysql
```

---

## 3. Starting MySQL

On Ubuntu, try:

```bash
sudo mysql
```

Or:

```bash
mysql -u root -p
```

Once inside, you'll see:

```text
mysql>
```

Exit:

```sql
exit;
```

or:

```sql
quit;
```

---

## 4. Important MySQL Rule

Most SQL commands end with:

```sql
;
```

For example:

```sql
SHOW DATABASES;
```

If you make a mistake while entering a command, cancel the current input with:

```text
\c
```

---

## 5. Show Available Databases

```sql
SHOW DATABASES;
```

---

## 6. Select a Database

Before working with tables, select the database:

```sql
USE database_name;
```

Example:

```sql
USE task_4_db;
```

You should see:

```text
Database changed
```

If you forget `USE`, you may get:

```text
ERROR 1046 (3D000): No database selected
```

---

## 7. Show Tables

After selecting a database:

```sql
SHOW TABLES;
```

---

## 8. Describe a Table

To see the table's columns:

```sql
DESCRIBE hacking_tools;
```

Short version:

```sql
DESC hacking_tools;
```

---

## 9. Display Everything in a Table

```sql
SELECT * FROM hacking_tools;
```

`*` means all columns.

---

## 10. Select Specific Columns

```sql
SELECT name FROM hacking_tools;
```

Multiple columns:

```sql
SELECT name, category FROM hacking_tools;
```

---

## 11. WHERE Clause

`WHERE` filters results.

```sql
SELECT * FROM hacking_tools
WHERE category = 'USB attacks';
```

Another example:

```sql
SELECT * FROM users
WHERE id = 5;
```

---

## 12. Comparison Operators

| Operator | Meaning |
|---|---|
| `=` | Equal |
| `!=` | Not equal |
| `<>` | Not equal |
| `>` | Greater than |
| `<` | Less than |
| `>=` | Greater than or equal |
| `<=` | Less than or equal |

Examples:

```sql
SELECT * FROM hacking_tools
WHERE amount > 100;
```

```sql
SELECT * FROM hacking_tools
WHERE amount <= 100;
```

```sql
SELECT * FROM hacking_tools
WHERE category != 'USB attacks';
```

---

## 13. AND / OR / NOT

### AND

Both conditions must be true:

```sql
SELECT * FROM hacking_tools
WHERE amount > 100 AND amount < 400;
```

### OR

At least one condition must be true:

```sql
SELECT * FROM hacking_tools
WHERE category = 'USB attacks'
OR category = 'RFID cloning';
```

### NOT

Reverses a condition:

```sql
SELECT * FROM hacking_tools
WHERE NOT category = 'USB attacks';
```

---

## 14. LIKE

`LIKE` searches for patterns.

### Starts with

```sql
SELECT * FROM hacking_tools
WHERE name LIKE 'B%';
```

Finds names beginning with `B`.

### Ends with

```sql
SELECT * FROM hacking_tools
WHERE name LIKE '%y';
```

### Contains

```sql
SELECT * FROM hacking_tools
WHERE name LIKE '%hack%';
```

`%` means any number of characters.

---

## 15. ORDER BY

Sort results.

Ascending:

```sql
SELECT * FROM hacking_tools
ORDER BY amount ASC;
```

Descending:

```sql
SELECT * FROM hacking_tools
ORDER BY amount DESC;
```

`ASC` = smallest → largest / A → Z

`DESC` = largest → smallest / Z → A

---

## 16. LIMIT

Limit the number of results:

```sql
SELECT * FROM hacking_tools
LIMIT 5;
```

---

## 17. DISTINCT

`DISTINCT` removes duplicate values.

```sql
SELECT DISTINCT category
FROM hacking_tools;
```

### Count distinct values

```sql
SELECT COUNT(DISTINCT category)
FROM hacking_tools;
```

This returns the number of unique categories.

---

## 18. Aggregate Functions

### COUNT

```sql
SELECT COUNT(*) FROM hacking_tools;
```

Number of rows.

### SUM

```sql
SELECT SUM(amount) FROM hacking_tools;
```

Total amount.

### AVG

```sql
SELECT AVG(amount) FROM hacking_tools;
```

Average amount.

### MIN

```sql
SELECT MIN(amount) FROM hacking_tools;
```

Smallest value.

### MAX

```sql
SELECT MAX(amount) FROM hacking_tools;
```

Largest value.

---

## 19. GROUP BY

Groups rows with the same value.

```sql
SELECT category, COUNT(*)
FROM hacking_tools
GROUP BY category;
```

This tells you how many tools belong to each category.

---

## 20. HAVING

`HAVING` filters grouped results.

```sql
SELECT category, COUNT(*)
FROM hacking_tools
GROUP BY category
HAVING COUNT(*) > 1;
```

Remember:

- `WHERE` → filters rows
- `HAVING` → filters groups

---

## 21. Creating a Database

```sql
CREATE DATABASE school;
```

Select it:

```sql
USE school;
```

---

## 22. Creating a Table

```sql
CREATE TABLE students (
    id INT,
    name VARCHAR(100),
    age INT
);
```

Check it:

```sql
SHOW TABLES;
```

Describe it:

```sql
DESCRIBE students;
```

---

## 23. INSERT — Add Data

```sql
INSERT INTO students (id, name, age)
VALUES (1, 'Ali', 18);
```

Insert another:

```sql
INSERT INTO students (id, name, age)
VALUES (2, 'Sara', 19);
```

View:

```sql
SELECT * FROM students;
```

---

## 24. UPDATE — Modify Data

```sql
UPDATE students
SET age = 20
WHERE id = 2;
```

**Warning:** Be careful with `UPDATE` without `WHERE`.

This:

```sql
UPDATE students
SET age = 20;
```

could change every row.

---

## 25. DELETE — Remove Data

Delete one row:

```sql
DELETE FROM students
WHERE id = 2;
```

**Warning:** Be careful with:

```sql
DELETE FROM students;
```

This removes all rows from the table.

---

## 26. DROP

Delete a table:

```sql
DROP TABLE students;
```

Delete a database:

```sql
DROP DATABASE school;
```

These are destructive commands. Don't run them on a database you need.

---

## 27. NULL

`NULL` means there is no value.

Find NULL values:

```sql
SELECT * FROM students
WHERE age IS NULL;
```

Find non-NULL values:

```sql
SELECT * FROM students
WHERE age IS NOT NULL;
```

Don't use:

```sql
WHERE age = NULL
```

Use:

```sql
WHERE age IS NULL
```

---

## 28. Useful MySQL Commands

| Command | Purpose |
|---|---|
| `SHOW DATABASES;` | List databases |
| `USE db;` | Select database |
| `SHOW TABLES;` | List tables |
| `DESCRIBE table;` | Show table structure |
| `SELECT * FROM table;` | Show all data |
| `SELECT column FROM table;` | Show specific column |
| `exit;` | Leave MySQL |
| `\c` | Cancel current query |

---

## 29. SQL Query Structure

A common query looks like:

```sql
SELECT column1, column2
FROM table_name
WHERE condition
ORDER BY column1 DESC
LIMIT 10;
```

Example:

```sql
SELECT name, amount
FROM hacking_tools
WHERE amount > 100
ORDER BY amount DESC
LIMIT 5;
```

Think of it as:

**SELECT → FROM → WHERE → GROUP BY → HAVING → ORDER BY → LIMIT**

---

## 30. CRUD

CRUD is very important.

| Letter | Operation | SQL |
|---|---|---|
| C | Create | `INSERT` |
| R | Read | `SELECT` |
| U | Update | `UPDATE` |
| D | Delete | `DELETE` |

Example:

```sql
-- Create
INSERT INTO students VALUES (1, 'Ali', 18);

-- Read
SELECT * FROM students;

-- Update
UPDATE students SET age = 19 WHERE id = 1;

-- Delete
DELETE FROM students WHERE id = 1;
```

---

## 31. Practical MySQL Workflow

When you connect to a MySQL server, remember this sequence:

```sql
SHOW DATABASES;
```

Choose the database:

```sql
USE database_name;
```

List tables:

```sql
SHOW TABLES;
```

Inspect a table:

```sql
DESCRIBE table_name;
```

Read the data:

```sql
SELECT * FROM table_name;
```

Then filter/search:

```sql
SELECT * FROM table_name
WHERE column = 'value';
```

---

## 32. TryHackMe Quick Reference

For the SQL Fundamentals room, these are especially useful:

```sql
SHOW DATABASES;
```

```sql
USE tools_db;
```

```sql
SHOW TABLES;
```

```sql
SELECT * FROM hacking_tools;
```

```sql
SELECT name, category FROM hacking_tools;
```

```sql
SELECT DISTINCT category FROM hacking_tools;
```

```sql
SELECT COUNT(DISTINCT category) FROM hacking_tools;
```

```sql
SELECT * FROM hacking_tools
WHERE name LIKE '%hack%';
```

```sql
SELECT * FROM hacking_tools
ORDER BY amount DESC;
```

```sql
SELECT category, COUNT(*)
FROM hacking_tools
GROUP BY category;
```

---

## 33. The 10 Commands to Memorize First

```sql
SHOW DATABASES;
USE database_name;
SHOW TABLES;
DESCRIBE table_name;
SELECT * FROM table_name;
SELECT column FROM table_name;
SELECT DISTINCT column FROM table_name;
SELECT COUNT(*) FROM table_name;
SELECT * FROM table_name WHERE condition;
SELECT * FROM table_name ORDER BY column DESC;
```

These cover a large part of beginner SQL work.

---

# Quick Cheat Sheet

```text
DATABASE
  SHOW DATABASES;
  USE database_name;

TABLES
  SHOW TABLES;
  DESCRIBE table_name;

READ
  SELECT * FROM table_name;
  SELECT column FROM table_name;

FILTER
  WHERE
  AND
  OR
  NOT
  LIKE

SORT
  ORDER BY column ASC;
  ORDER BY column DESC;

LIMIT
  LIMIT 5;

UNIQUE
  DISTINCT

COUNTING
  COUNT()
  COUNT(DISTINCT column)

CALCULATIONS
  SUM()
  AVG()
  MIN()
  MAX()

GROUPING
  GROUP BY
  HAVING

CRUD
  INSERT
  SELECT
  UPDATE
  DELETE
```

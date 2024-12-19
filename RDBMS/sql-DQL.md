[toc]

# General

## `AS` - Alias, give a custom name

> An alias only exists for the duration of that query.

When use the alias in query, the result "column name" will be named to that alias.

```sql
# On column name
SELECT column_name AS alias_name
FROM table_name;

# On table name
SELECT column_name(s)
FROM table_name AS alias_name;
```

In this example, we use the "Customers" and "Orders" tables, and give them the table aliases of "c" and "o" respectively (Here we use aliases to make the SQL shorter):
```sql
SELECT o.OrderID, o.OrderDate, c.CustomerName
FROM Customers AS c, Orders AS o
WHERE c.CustomerName='Around the Horn' AND c.CustomerID=o.CustomerID;
```



## Null
> A field with a NULL value is a field with no value.

It's only possible to use `IS NULL` and `IS NOT NULL` operators to check.
```sql
SELECT column_names
FROM table_name
WHERE column_name IS NULL;

###

SELECT column_names
FROM table_name
WHERE column_name IS NOT NULL;
```

### `IFNULL()` - give default value if it is null

Different rdbms might have different function name.

MySQL - `IFNULL`
```sql
SELECT ProductName, UnitPrice * (UnitsInStock + IFNULL(UnitsOnOrder, 0))
FROM Products;
```

SQL Server - `ISNULL()`
```sql
SELECT ProductName, UnitPrice * (UnitsInStock + ISNULL(UnitsOnOrder, 0))
FROM Products;
```

# READ

## `SELECT`

```sql
SELECT * FROM table;
SELECT c1, c2 FROM table;
```

### `SELECT` Distinct

```sql
SELECT DISTINCT c1, c2, ... FROM table;
```

## `WHERE` to filter records
```sql
SELECT *
FROM table
WHERE condition;
```

Example:
```sql
SELECT * FROM customers WHERE Country="Mexico";
SELECT * FROM customers WHERE CustomerID=1;
```

| Operator | Description                          |
|----------|--------------------------------------|
| =        | equal                                |
| >        | greater than                         |
| <        | less than                            |
| >=       |                                      |
| <=       |                                      |
| <>       | not equal, some vers may be '!='     |
| BETWEEN  | between a certain range              |
| LIKE     | search for a pattern                 |
| IN       | specify possible values for a column |

### `WHERE` with `AND, OR, NOT`

The query is self-explanatory:
```sql
# AND
SELECT column1, column2, ...
FROM table_name
WHERE condition1 AND condition2 AND condition3 ...;

# OR
SELECT column1, column2, ...
FROM table_name
WHERE condition1 OR condition2 OR condition3 ...;

# NOT
SELECT column1, column2, ...
FROM table_name
WHERE NOT condition;
```

Example:
```sql
# ex1
SELECT * FROM Customers
WHERE Country='Germany' AND (City='Berlin' OR City='München');

# ex2
SELECT * FROM Customers
WHERE NOT Country='Germany' AND NOT Country='USA';
```

### `WHERE ... IN ...` - shorthand for `OR`

```sql
SELECT column_name(s)
FROM table_name
WHERE column_name IN (value1, value2, ...);

# means

WHERE column_name=value1 OR column_name=value2, OR ...
```

Example:
```sql
SELECT * FROM Customers
WHERE Country IN ('Germany', 'France', 'UK');
```

### `WHERE ... LIKE pattern` - for match a specified pattern in column

**Note: different rdbms has different wildcards.** 

| sign | description |
|------|-------------|
| %    | 0...many    |
| _    | one         |

Syntax
```sql
SELECT column1, column2, ...
FROM table_name
WHERE columnN LIKE pattern;
```

Example: 1 char before r, and 0 ... many after
```sql
SELECT * FROM Customers
WHERE CustomerName LIKE '_r%';

### FOUND
# Around the Horn
# Ernst Handel
```

### `WHERE ... BETWEEN ...` - value within range (inclusive)

> The operator is inclusive: begin and end values are included. 

This can be used for text. However, there might unexpected results.

```sql
SELECT column_name(s)
FROM table_name
WHERE column_name BETWEEN value1 AND value2;
```

Example:
```sql
SELECT * FROM Products
WHERE Price NOT BETWEEN 10 AND 20;
```

#### `WHERE ... BETWEEN Date` - find records between dates

Between '01-July-1996' and '31-July-1996':
```sql
# approach 1
SELECT * FROM Orders
WHERE OrderDate BETWEEN #07/01/1996# AND #07/31/1996#;

# approach 2
SELECT * FROM Orders
WHERE OrderDate BETWEEN '1996-07-01' AND '1996-07-31';
```

## `HAVING condition` - when want to apply function on `WHERE`

> `HAVING` was added to SQL because the `WHERE` keyword cannot be used with aggregate functions.

```sql
SELECT column_name(s)
FROM table_name
WHERE condition
GROUP BY column_name(s)
HAVING condition
ORDER BY column_name(s);
```

Example
```sql
SELECT COUNT(CustomerID), Country
FROM Customers
GROUP BY Country
HAVING COUNT(CustomerID) > 5;
```

## `ORDER BY` - sort

```sql
SELECT column1, column2, ...
FROM table_name
ORDER BY column1 <ASC|DESC>;
```

Example:
```sql
SELECT * FROM Customers
ORDER BY Country DESC;
```

Multiple columns example:
```sql
SELECT * FROM Customers
ORDER BY Country ASC, CustomerName DESC;
```

## `EXISTS` - test for record existence

> The `EXISTS` operator is used to test for the existence of any record in a subquery. It returns TRUE when find one or more.

```sql
SELECT column_name(s)
FROM table_name
WHERE EXISTS
(SELECT column_name FROM table_name WHERE condition);
```

> Think query inside `WHERE EXISTS (Query)` as subquery. It then joins 2 tables and populates the result.

Example: It lists the suppliers with a product price less than 20
```sql
SELECT SupplierName
FROM Suppliers
WHERE EXISTS (SELECT ProductName FROM Products WHERE Products.SupplierID = Suppliers.supplierID AND Price < 20);
```

| SupplierName  |
|---------------|
| Tokyo Traders |
| Exotic Liquid |

## `JOIN`

> A `JOIN` clause is used to combine rows from two or more tables, based on a related column between them.

![Join types](https://www.w3schools.com/sql/img_rightjoin.gif) 

- `(INNER) JOIN`
- `LEFT (OUTER) JOIN`
- `RIGHT (OUTER) JOIN`
- `FULL (OUTER) JOIN`

### `INNER JOIN` - default join

![Inner join](https://www.w3schools.com/sql/img_innerjoin.gif) 

```sql
SELECT column_name(s)
FROM table1
INNER JOIN table2
ON table1.column_name = table2.column_name;
```

#### Join the same table twice

There is a football league. There is a match schedule as follow:

football match 
| Home_team | Away_team |
|-----------|-----------|
| A         | B         |
| C         | A         |

team elo
| team | elo |
|------|-----|
| A    | 100 |
| B    | 200 |
| C    | 400 |

To produce the table like this, we have to join the table twice:
| Home_team | Away_team | Home elo | Away elo |
|-----------|-----------|----------|----------|
| A         | B         | 100      | 200      |

Query:
```sql
SELECT 
    game.Home_team,
    game.Away_team,
    home_elo.elo as homeElo,
    away_elo.elo as awayElo
FROM football as game
INNER JOIN `team.elo` as home_elo
ON game.Home_team = home_elo.team

INNER JOIN `team.elo` as away_elo
ON game.Away_team = away_elo.team
```

### `LEFT JOIN` - everything from left table

> It returns all records from the left table (table1), and the matching records from the right table (table2). The result is 0 records from the right side, if there is no match.

There might be null columns.

![LEFT JOIN](https://www.w3schools.com/sql/img_leftjoin.gif) 

```sql
SELECT column_name(s)
FROM table1
LEFT JOIN table2
ON table1.column_name = table2.column_name;
```

### `RIGHT JOIN` - everything from right table

> returns all records from the right table (table2), and the matching records from the left table (table1). The result is 0 records from the left side, if there is no match.

![Right join](https://www.w3schools.com/sql/img_rightjoin.gif) 

```sql
SELECT column_name(s)
FROM table1
RIGHT JOIN table2
ON table1.column_name = table2.column_name;
```

### `FULL (OUTER) JOIN` - everything from both side

> It returns all records when there is a match in left (table1) or right (table2) table records.

![FULL JOIN](https://www.w3schools.com/sql/img_fulljoin.gif) 

## `UNION` - combine 2 or more result-set

- Every `SELECT` statement within `UNION` must have the same number of columns
- The columns must also have similar data types
- The columns in every `SELECT` statement must also be in the same order

```sql
SELECT column_name(s) FROM table1
UNION
SELECT column_name(s) FROM table2;
```

It's set, by default everything is distinct. However, if you want to allow duplicate from both tables, use `UNION ALL`:
```sql
Q1
UNION ALL
Q2
```

## `GROUP BY` - find the number of something

[w3 - Group by](https://www.w3schools.com/sql/sql_groupby.asp) 

- It groups rows that have the same values into summary rows, like "find the number of customers in each country".

- It often used with aggregate functions `COUNT(), MAX(), MIN(), SUM(), AVG()` to group the result-set by one or more columns.

```sql
SELECT column_name(s)
FROM table_name
WHERE condition
GROUP BY column_name(s)
ORDER BY column_name(s);
```

Example:

Table:
| CustomerID | Country |
|------------|---------|
| 1          | UK      |
| 2          | Mexico  |
| 3          | Germany |
| 4          | US      |
| 5          | Germany |
| 6          | Sweden  |
| ...        | ...     |

```sql
SELECT COUNT(CustomerID), Country
FROM Customers
GROUP BY Country;
```

Result in:
| Count(CustomerID) | Country |
|-------------------|---------|
| 2                 | Germany |

## `ANY, ALL` - 

### `ANY` - find the rows that meet the sub-query condition

> Execute the sub query and select that based on condition

Use operator like `=, >=, <, ...`

```sql
SELECT column_name(s)
FROM table_name
WHERE column_name operator ANY
  (SELECT column_name
  FROM table_name
  WHERE condition);
```

Example:
```sql
SELECT ProductName
FROM Products
WHERE ProductID = ANY
  (SELECT ProductID
  FROM OrderDetails
  WHERE Quantity = 10);
```
First, the sub query finds the `Quentity=10`. Then, we select `ProductName` from `Products`. Join then together.

### `ALL` - returns the record only if every record meets the condition

> Only if all values are true, in the range, the columns from the sub query will be all selected.

```sql
SELECT ALL ProductName
FROM Products
WHERE TRUE;
```

Example:
```sql
SELECT ProductName
FROM Products
WHERE ProductID = ALL
  (SELECT ProductID
  FROM OrderDetails
  WHERE Quantity = 10);
```

## Select head records

To select the top/head number of records, the query is varied based on the database system.

MySQL use `LIMIT`:
```
SELECT column_name(s)
FROM table_name
WHERE condition
LIMIT number;

### example
SELECT * FROM Customers
LIMIT 3;
```

SQL Server / MS Access:
```sql
SELECT TOP number|percent column_name(s)
FROM table_name
WHERE condition;

### example
SELECT TOP 3 * FROM Customers;
```

Oracle:
```sql
SELECT column_name(s)
FROM table_name
ORDER BY column_name(s)
FETCH FIRST number ROWS ONLY;

### example
SELECT * FROM Customers
FETCH FIRST 3 ROWS ONLY;
```

## `CASE` - if-else-if expression

It works like if-then-else-statement.

```sql
CASE
    WHEN condition1 THEN result1
    WHEN condition2 THEN result2
    WHEN conditionN THEN resultN
    ELSE result
END;
```

Example:
```sql
SELECT OrderID, Quantity,
CASE
    WHEN Quantity > 30 THEN 'The quantity is greater than 30'
    WHEN Quantity = 30 THEN 'The quantity is 30'
    ELSE 'The quantity is under 30'
END AS QuantityText
FROM OrderDetails;
```

Result table:
| OrderID | Quentity | QuantityText                    |
|---------|----------|---------------------------------|
| 10248   | 12       | The quantity is under 30        |
| 10248   | 10       | The quantity is under 30        |
| 10249   | 40       | The quantity is greater than 30 |

# Creation

## `INSERT` - create new record

```sql
# specify the desired columns
INSERT INTO table_name (column1, column2, column3, ...)
VALUES (value1, value2, value3, ...);

# or feed all values
INSERT INTO table_name
VALUES (value1, value2, value3, ...);
```

Example:
```sql
# All columns
INSERT INTO Customers (CustomerName, ContactName, Address, City, PostalCode, Country)
VALUES ('Cardinal', 'Tom B. Erichsen', 'Skagen 21', 'Stavanger', '4006', 'Norway');


# desired columns
INSERT INTO Customers (CustomerName, City, Country)
VALUES ('Cardinal', 'Stavanger', 'Norway');
```

# UPDATE

> Used to modify the existing records in table

Note: Be careful when updating records in a table! **Notice the `WHERE` clause** in the `UPDATE` statement. The WHERE clause specifies which record(s) that should be updated. If you omit the WHERE clause, **all records in the table will be updated!**

```sql
UPDATE table_name
SET c1 = v1, c2 = v2, ...
WHERE condition;
```

Example:
```sql
UPDATE Customers
SET ContactName = 'Alfred Schmidt', City= 'Frankfurt'
WHERE CustomerID = 1;
```

# DELETE

Specify the condition in `WHERE` clause. Otherwise, **the entire table will be deleted!** 

```sql
DELETE FROM table_name WHERE condition;
```

Example:
```sql
# delete a record
DELETE FROM Customers WHERE CustomerName='Alfreds Futterkiste';

# delete the table
DELETE FROM Customers;
```

# Functions

## `Min` and `Max`

> Find the min or max

```sql
# MIN
SELECT MIN(column_name)
FROM table_name
WHERE condition;

# MAX
SELECT MAX(Price) AS LargestPrice
FROM Products;
```

## `Count`, `Avg`, `Sum`

```sql
# count
SELECT COUNT(column_name)
FROM table_name
WHERE condition;

# average
SELECT AVG(column_name)
FROM table_name
WHERE condition;

# sum
SELECT SUM(column_name)
FROM table_name
WHERE condition;
```

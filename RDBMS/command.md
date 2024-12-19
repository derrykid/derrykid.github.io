# Connection and quit

[doc](https://dev.mysql.com/doc/refman/8.0/en/connecting-disconnecting.html) 

```bash
mysql -h host -u user -p
Enter password:
```

Disconnecting:
```bash
mysql> QUIT;
```

# Databases

## Show database
```bash
show databases;
```

## Use database
```bash
use database_name;
```

To change to another database, you have to start with the root, not something like `cd ..`:
```bash
USE demo;
SHOW TABLES;

// displaying tables, run sql queries
select * from table where condition;
// want to switch to another database schema
SHOW databases;
USE products;
```

# Table

## Show table

```bash
mysql> SHOW TABLES;
```

## Use table by query

```bash
mysql > select * from table;
```

## See table column information
```bash
DESCRIBE table_name;
```

# mysql 8

Using locally installed mysql.

## Set-up

```mysql
systemctl status mysql
mysql -u root -p

mysql> use learning
mysql> show tables
...
flights
...
```

## Learning

- Create table

  ```mysql
  mysql> CREATE TABLE flights (
    -> id MEDIUMINT NOT NULL AUTO_INCREMENT,
    -> origin CHAR(30) NOT NULL,
    -> destination CHAR(30) NOT NULL,
    -> duration MEDIUMINT NOT NULL,
    -> PRIMARY KEY (id)
    -> );
  ```

- Source sql file into table

  ```mysql
  $ head -2 insert_flights.sql
  use learning
  INSERT INTO flights (origin, destination, duration) VALUES ('New York', 'London', 415);
  $ mysql -u root -p < insert_flights.sql
  ```

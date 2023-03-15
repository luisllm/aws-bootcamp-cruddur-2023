# Week 4 — Postgres and RDS
## My journal - week4

-  **Did all the tasks in the week4 to-do list**
   -  **Created AWS RDS instance**
![image week4-rds](./images/week4-rds.png)
&nbsp;
&nbsp;
   -  **Created all the bash scripts for all common database actions**
```
gitpod /workspace/aws-bootcamp-cruddur-2023/backend-flask (main) $ ./bin/db-setup 
./bin/db-setup: line 2: -e: command not found
== db-setup
== db-drop
ERROR:  database "cruddur" does not exist
== db-create
CREATE DATABASE
== db-schema-load
/workspace/aws-bootcamp-cruddur-2023/backend-flask/db/schema.sql
not using production
CREATE EXTENSION
NOTICE:  table "users" does not exist, skipping
DROP TABLE
NOTICE:  table "activities" does not exist, skipping
DROP TABLE
CREATE TABLE
CREATE TABLE
== db-seed
/workspace/aws-bootcamp-cruddur-2023/backend-flask/db/seed.sql
not using production
INSERT 0 2
INSERT 0 1
gitpod /workspace/aws-bootcamp-cruddur-2023/backend-flask (main) $ ./bin/db-connect 
psql (13.10 (Ubuntu 13.10-1.pgdg20.04+1))
Type "help" for help.

cruddur=# \dt
           List of relations
 Schema |    Name    | Type  |  Owner   
--------+------------+-------+----------
 public | activities | table | postgres
 public | users      | table | postgres
(2 rows)

cruddur=#
```
   -  **Installed Postgres driver in backend**
![image week4-postgres-driver](./images/week4-postgres-driver.png)
&nbsp;
&nbsp;
   -  **Connected Gitpod to RDS**
![image week4-gitpod-to-rds](./images/week4-gitpod-to-rds.png)
&nbsp;
&nbsp;
   -  **Connected Gitpod to RDS**
```
gitpod /workspace/aws-bootcamp-cruddur-2023/backend-flask (main) $ psql $PROD_CONNECTION_URL
psql (13.10 (Ubuntu 13.10-1.pgdg20.04+1), server 14.6)
WARNING: psql major version 13, server major version 14.
         Some psql features might not work.
SSL connection (protocol: TLSv1.2, cipher: ECDHE-RSA-AES256-GCM-SHA384, bits: 256, compression: off)
Type "help" for help.

cruddur=> \l
                                      List of databases
   Name    |    Owner    | Encoding |   Collate   |    Ctype    |      Access privileges      
-----------+-------------+----------+-------------+-------------+-----------------------------
 cruddur   | cruddurroot | UTF8     | en_US.UTF-8 | en_US.UTF-8 | 
 postgres  | cruddurroot | UTF8     | en_US.UTF-8 | en_US.UTF-8 | 
 rdsadmin  | rdsadmin    | UTF8     | en_US.UTF-8 | en_US.UTF-8 | rdsadmin=CTc/rdsadmin      +
           |             |          |             |             | rdstopmgr=Tc/rdsadmin
 template0 | rdsadmin    | UTF8     | en_US.UTF-8 | en_US.UTF-8 | =c/rdsadmin                +
           |             |          |             |             | rdsadmin=CTc/rdsadmin
 template1 | cruddurroot | UTF8     | en_US.UTF-8 | en_US.UTF-8 | =c/cruddurroot             +
           |             |          |             |             | cruddurroot=CTc/cruddurroot
(5 rows)
```
   -  **Created Congito Trigger to insert user into database**
![image week4-gitpod-to-rds](./images/week4-gitpod-to-rds.png)
&nbsp;
&nbsp;
   -  **Created new activities with a database insert**
![image week4-gitpod-to-rds](./images/week4-gitpod-to-rds.png)
&nbsp;
&nbsp;
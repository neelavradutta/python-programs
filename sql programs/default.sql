create database db;
use db;
create table if not exists student(name varchar(100), phno int , marks double);
insert into student(name,phno,marks)values("neel",45,78.45682),("rohit",85,82.48545);

drop table student
select * from student 

show tables

set sql_safe_updates=0
update student set name = "bro" where name="neel"
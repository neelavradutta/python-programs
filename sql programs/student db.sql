create database college
use college

create table std (roll int primary key,name varchar(100),dept varchar(100))
insert into std (roll,name,dept)values(1,"neel","csbs"),(2,"pro","cse");


select * from std

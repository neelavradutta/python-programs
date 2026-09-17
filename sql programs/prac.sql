create database if not exists student
use student

create table bio(id int primary key,class varchar(100),name varchar(50))
insert into bio(id,name,class) values(7,'rohit','10')

select * from bio
select lower(name) from bio
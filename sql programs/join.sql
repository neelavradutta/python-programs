
CREATE TABLE students (
    student_id INT PRIMARY KEY,
    name VARCHAR(50),
    age INT,
    department VARCHAR(50)
);

INSERT INTO students (student_id, name, age, department)
VALUES
(1, 'Rahul', 20, 'CSE'),
(2, 'Priya', 21, 'CSE'),
(3, 'Amit', 22, 'ECE'),
(4, 'Sneha', 20, 'ECE'),
(5, 'Rohan', 23, 'CSE');


CREATE TABLE marks (
    mark_id INT PRIMARY KEY,
    student_id INT,
    subject VARCHAR(50),
    marks INT,
    FOREIGN KEY (student_id) REFERENCES students(student_id)
);

INSERT INTO marks (mark_id, student_id, subject, marks)
VALUES
(1, 1, 'DBMS', 85),
(2, 1, 'OS', 78),
(3, 2, 'DBMS', 92),
(4, 2, 'OS', 88),
(5, 3, 'DBMS', 65),
(6, 4, 'DBMS', 72),
(7, 5, 'DBMS', 90);

select *from students
select *from students


select * from students s1 inner join marks m1 on s1.student_id=m1.student_id

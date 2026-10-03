CREATE DATABASE abc;

USE abc;

CREATE TABLE cources (
    course_id VARCHAR(5) PRIMARY KEY,
    course VARCHAR(20),
    department VARCHAR(20)
);

CREATE TABLE assessments (
    assessment_id INTEGER PRIMARY KEY,
    month_2 VARCHAR(10),
    course_id VARCHAR(20),
    batch VARCHAR(20),
    score INTEGER,
    attendance_pct INTEGER,
    FOREIGN KEY (course_id) REFERENCES cources(course_id)
);

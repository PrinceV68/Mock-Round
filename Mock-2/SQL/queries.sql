INSERT INTO cources (course_id, course, department)
VALUES
('C1', 'Course 1', 'Department 1'),
('C2', 'Course 2', 'Department 2'),
('C3', 'Course 3', 'Department 3'),
('C4', 'Course 4', 'Department 4');

INSERT INTO assessments
(assessment_id, month_2, course_id, batch, score, attendance_pct)
VALUES
(1, 'Jan', 'C1', 'Morning', 72, 90),
(2, 'Jan', 'C2', 'Evening', 45, 70),
(3, 'Jan', 'C3', 'Morning', 65, 85),
(4, 'Jan', 'C4', 'Weekend', 38, 60),
(5, 'Feb', 'C1', 'Evening', 80, 95),
(6, 'Feb', 'C2', 'Weekend', 55, 80),
(7, 'Feb', 'C3', 'Morning', 48, 75),
(8, 'Feb', 'C4', 'Evening', 68, 88),
(9, 'Mar', 'C1', 'Weekend', 90, 98),
(10, 'Mar', 'C2', 'Morning', 60, 82),
(11, 'Mar', 'C3', 'Evening', 75, 92),
(12, 'Mar', 'C4', 'Weekend', 42, 65);

-- S2a — Average score by department
SELECT
    c.department,
    AVG(a.score) AS avg_score
FROM assessments AS a
JOIN cources AS c
	 on a.course_id = c.course_id
GROUP BY c.department
;

-- S2b — Underperforming courses
SELECT
    c.course_id,
    c.course,
    AVG(a.score) AS avg_score
FROM assessments AS a
JOIN cources AS c
    ON a.course_id = c.course_id
GROUP BY c.course_id, c.course
HAVING AVG(a.score) < 60;


-- S2c — Top two batches by average score
SELECT
    batch,
    AVG(score) AS avg_score
FROM assessments
GROUP BY batch
ORDER BY avg_score DESC, batch desc
LIMIT 2;

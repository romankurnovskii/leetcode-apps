WITH ExamStats AS (
    SELECT
        student_id,
        exam_id,
        score,
        RANK() OVER (PARTITION BY exam_id ORDER BY score DESC) AS high_rank,
        RANK() OVER (PARTITION BY exam_id ORDER BY score ASC) AS low_rank,
        COUNT(*) OVER (PARTITION BY exam_id) AS exam_count
    FROM Exam
),
QuietStudents AS (
    SELECT DISTINCT student_id
    FROM ExamStats
    WHERE student_id NOT IN (
        SELECT student_id
        FROM ExamStats
        WHERE high_rank = 1 OR low_rank = 1
    )
)
SELECT s.student_id, s.student_name
FROM Student s
INNER JOIN QuietStudents q ON s.student_id = q.student_id
ORDER BY s.student_id;


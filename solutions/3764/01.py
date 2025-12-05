# Solution for LeetCode 3764: Most Common Course Pairs
# Find skill mastery pathways by analyzing course completion sequences among top-performing students

"""
SQL Solution:

WITH top_performers AS (
    -- Step 1: Identify top-performing students
    -- Must have at least 5 courses with average rating >= 4
    SELECT 
        user_id
    FROM 
        course_completions
    GROUP BY 
        user_id
    HAVING 
        COUNT(*) >= 5 
        AND AVG(course_rating) >= 4
),
ordered_courses AS (
    -- Step 2: Get courses for top performers in chronological order
    SELECT 
        cc.user_id,
        cc.course_name,
        cc.completion_date,
        ROW_NUMBER() OVER (
            PARTITION BY cc.user_id 
            ORDER BY cc.completion_date
        ) AS course_order
    FROM 
        course_completions cc
    INNER JOIN 
        top_performers tp ON cc.user_id = tp.user_id
),
course_pairs AS (
    -- Step 3: Create consecutive course pairs
    SELECT 
        oc1.course_name AS first_course,
        oc2.course_name AS second_course
    FROM 
        ordered_courses oc1
    INNER JOIN 
        ordered_courses oc2 
        ON oc1.user_id = oc2.user_id 
        AND oc2.course_order = oc1.course_order + 1
)
-- Step 4: Count pair frequencies and order results
SELECT 
    first_course,
    second_course,
    COUNT(*) AS transition_count
FROM 
    course_pairs
GROUP BY 
    first_course, 
    second_course
ORDER BY 
    transition_count DESC,
    first_course ASC,
    second_course ASC;
"""


# Solution for LeetCode 3705: Find Golden Hour Customers
# Find customers who consistently order during peak hours and provide high satisfaction

"""
SQL Solution:

WITH customer_stats AS (
    SELECT 
        customer_id,
        COUNT(*) AS total_orders,
        SUM(
            CASE 
                WHEN TIME(order_timestamp) BETWEEN '11:00:00' AND '14:00:00'
                     OR TIME(order_timestamp) BETWEEN '18:00:00' AND '21:00:00'
                THEN 1 
                ELSE 0 
            END
        ) AS peak_hour_orders,
        COUNT(order_rating) AS rated_orders,
        AVG(order_rating) AS avg_rating
    FROM 
        restaurant_orders
    GROUP BY 
        customer_id
    HAVING 
        COUNT(*) >= 3
        AND SUM(
            CASE 
                WHEN TIME(order_timestamp) BETWEEN '11:00:00' AND '14:00:00'
                     OR TIME(order_timestamp) BETWEEN '18:00:00' AND '21:00:00'
                THEN 1 
                ELSE 0 
            END
        ) * 100.0 / COUNT(*) >= 60.0
        AND AVG(order_rating) >= 4.0
        AND COUNT(order_rating) * 100.0 / COUNT(*) >= 50.0
)
SELECT 
    customer_id,
    total_orders,
    ROUND(peak_hour_orders * 100.0 / total_orders, 0) AS peak_hour_percentage,
    ROUND(avg_rating, 2) AS average_rating
FROM 
    customer_stats
ORDER BY 
    average_rating DESC,
    customer_id DESC;
"""

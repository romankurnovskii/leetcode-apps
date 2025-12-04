from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Build adjacency list
        graph = [[] for _ in range(numCourses)]
        in_degree = [0] * numCourses
        
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            in_degree[course] += 1
        
        # Find all courses with no prerequisites
        queue = []
        for i in range(numCourses):
            if in_degree[i] == 0:
                queue.append(i)
        
        res = []
        while queue:
            course = queue.pop(0)
            res.append(course)
            
            # Reduce in-degree of dependent courses
            for next_course in graph[course]:
                in_degree[next_course] -= 1
                if in_degree[next_course] == 0:
                    queue.append(next_course)
        
        return res if len(res) == numCourses else []


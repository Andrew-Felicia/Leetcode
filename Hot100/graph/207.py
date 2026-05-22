from collections import defaultdict
from collections import deque
from typing import List
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        in_degree = [0] * numCourses

        for coures, prereq in prerequisites:
            graph[prereq].append(coures)
            in_degree[coures] += 1

        queue = deque()
        for course in range(len(in_degree)):
            if in_degree[course] == 0:
                queue.append(course)

        completed_courses = 0

        while queue:
            current_course = queue.popleft()
            completed_courses += 1

            for next_course in graph[current_course]:
                in_degree[next_course] -= 1
                
                if in_degree[next_course] == 0:
                    queue.append(next_course)
                    
        return completed_courses == numCourses
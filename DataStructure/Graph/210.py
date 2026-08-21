from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        gragh = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        for course, pre in prerequisites:
            gragh[pre].append(course)
            indegree[course] += 1

        result = []
        count = 0
        queue = [i for i in range(numCourses) if indegree[i] == 0]
        while queue:
            cur = queue.pop()
            count += 1
            result.append(cur)
            for next_course in gragh[cur]:
                indegree[next_course] -= 1
                if indegree[next_course] == 0:
                    queue.append(next_course)
        return result if count == numCourses else []
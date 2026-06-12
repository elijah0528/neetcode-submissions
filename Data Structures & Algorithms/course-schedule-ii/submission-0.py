from collections import defaultdict, deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indegree = [0] * numCourses

        for next_course, prereq in prerequisites:
            graph[prereq].append(next_course)
            indegree[next_course] += 1

        q = deque()
        for i in range(len(indegree)):
            if indegree[i] == 0:
                q.append(i)
        
        res = []

        while q:
            curr = q.popleft()
            res.append(curr)
            for next_course in graph[curr]:
                indegree[next_course] -= 1
                if indegree[next_course] == 0:
                    q.append(next_course)
        if max(indegree) > 0:
            return []
        return res
    
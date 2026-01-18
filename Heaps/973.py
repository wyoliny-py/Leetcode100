# 973. K Closest Points to Origin
import heapq
class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        # O(n + k log n)
        # hashmap = {}
        # listik = []
        # for i in range(len(points)):
        #     r = points[i][0] ** 2 + points[i][1] ** 2
        #     if r in hashmap:
        #         hashmap[r].append(points[i])
        #     else:
        #         hashmap[r] = [points[i]]
        #     listik.append(r)
        # heapq.heapify(listik)
        # answer = []
        # for _ in range(k):
        #     r = heapq.heappop(listik)
        #     answer.append(hashmap[r][0])
        #     for i in range(1, len(hashmap[r])):
        #         answer.append(hashmap[r][i])
        # return answer
    
        # Optimal:
        heap = []
        for point in points:
            dist = point[0] ** 2 + point[1] ** 2
            heapq.heappush(heap, (dist, point))
        
        return [heapq.heappop(heap)[1] for _ in range(k)]
        # O(n)
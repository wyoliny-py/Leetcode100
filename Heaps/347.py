# 347. Top K Frequent Elements
from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # O (n log n)
        # hash_map = Counter(nums)
        # return list(sorted(hash_map.keys(), key=lambda x: hash_map[x], reverse=True))[:k]


        # O(n log k)
        counter = Counter(nums)
        heap = []

        for key, val in counter.items():
            if len(heap) < k:
                heapq.heappush(heap, (val, key))
            else:
                heapq.heappushpop(heap, (val, key))
        
        return [h[1] for h in heap]


    
# 1046. Last Stone Weight
import heapq
class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:

        # Brute Force (1)
        # O(n^2 log n)
        # stones.sort(reverse=True)
        # while len(stones) > 1:
        #     if stones[0] == stones[1]:
        #         del stones[0]
        #         del stones[0]
        #     else:
        #         stones[0] = stones[0] - stones[1]
        #         del stones[1]
        #         stones.sort(reverse=True)
        # return stones[0] if stones else 0

        # Brute Force (2)
        # O(n ^ 2)
	    # def remove_largest():
	    #     index_of_largest = stones.index(max(stones))
	    #     return stones.pop(index_of_largest)
			
	    # while len(stones) > 1:
	    #     stone_1 = remove_largest()
	    #     stone_2 = remove_largest()
	    #     if stone_1 != stone_2:
	    #         stones.append(stone_1 - stone_2)
	    # return stones[0] if stones else 0

        # O (n log n) with Heap
        n = len(stones)
        for i in range(n):
            stones[i] = -stones[i]
        
        heapq.heapify(stones)
        while len(stones) > 1:
            largest = heapq.heappop(stones)
            next_largest = heapq.heappop(stones)

            if next_largest != largest:
                heapq.heappush(stones, largest - next_largest)
            
        if len(stones) == 1:
            return -heapq.heappop(stones)
        else:
            return 0
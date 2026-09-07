import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxheap = [-stone for stone in stones]
        heapq.heapify(maxheap)
        while len(maxheap) > 1:
            x = heapq.heappop(maxheap)
            y = heapq.heappop(maxheap)

            if x != y:
                result = x - y
                heapq.heappush(maxheap, result)
        
        if len(maxheap) == 0:
            return 0
        else:
            return -maxheap[0]
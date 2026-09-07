import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k 
        self.heap = []
        for num in nums:
            heapq.heappush(self.heap, num)
        if len(self.heap) > self.k:
            diff = len(self.heap) - self.k
            for _ in range(diff):
                heapq.heappop(self.heap)
        
        

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if(self.k < len(self.heap)):
            heapq.heappop(self.heap)
        return self.heap[0]

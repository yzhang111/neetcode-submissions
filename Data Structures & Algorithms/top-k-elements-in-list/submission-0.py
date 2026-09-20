import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            if num not in freq:
                freq[num] = 0
            freq[num] += 1

        heap = []
        for item in freq:
            heapq.heappush(heap,(freq[item], item))

            if len(heap) > k:
                heapq.heappop(heap)
        
        return [item[1] for item in heap]
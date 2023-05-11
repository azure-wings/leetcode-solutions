from heapq import heapify, heappop, heappush


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for stone in stones:
            heappush(heap, -stone)

        while len(heap) > 1:
            fst_largest = heappop(heap)
            sec_largest = heappop(heap)

            if sec_largest == fst_largest:
                continue
            elif sec_largest > fst_largest:
                heapq.heappush(heap, fst_largest - sec_largest)

        return -heap[0] if heap else 0
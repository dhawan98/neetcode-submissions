class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxheap = [-stone for stone in stones]
        heapq.heapify(maxheap)

        while len (maxheap) > 1:
            first = -heapq.heappop(maxheap)
            second = -heapq.heappop(maxheap)

            if first != second:
                newstone = first - second
                heapq.heappush(maxheap, -newstone)

        return -maxheap[0] if maxheap else 0
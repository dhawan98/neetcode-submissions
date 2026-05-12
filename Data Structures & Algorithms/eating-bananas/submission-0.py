class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def canfinish(k):
            hours = 0
            for pile in piles:
                hours += (pile+k-1)//k
            return hours <=h
        left, right = 1, max(piles)
        answer = right

        while left <= right:
            mid = (left+right)//2
            if canfinish(mid):
                answer = mid
                right = mid-1
            else:
                left = mid + 1
        return answer

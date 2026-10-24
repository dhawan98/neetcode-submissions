class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        best = 0
        current = 0
        for num in seen:
            if num-1 not in seen:
                current=1
                while num+current in seen:
                    current+=1
                best = max(current, best)
        return best
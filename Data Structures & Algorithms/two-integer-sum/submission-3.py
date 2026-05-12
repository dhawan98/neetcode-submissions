class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i,n  in enumerate(nums):
            compl = target - n
            if compl in seen:
                return [seen[compl], i]
            seen[n]=i

class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        #if 0 - it makes product 0, we rhave to reset
        res = max(nums)
        currMin, currMax = 1, 1
        for num in nums:
            if num == 0:
                currMin, currMax = 1, 1
            tmpMax = currMax * num
            currMax = max(currMax*num, currMin*num, num)
            currMin = min(num*currMin, tmpMax, num)
            
            res = max(currMax, res)
        return res
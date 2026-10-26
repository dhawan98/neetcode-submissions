class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        cMax, cMin = 1, 1
        for num in nums:
            if num == 0:
                cMax, cMin = 1, 1
            tmp = cMax*num
            cMax = max(cMax*num, cMin*num, num)
            cMin = min(tmp, cMin*num, num)
            res = max(res, cMax)
        return res
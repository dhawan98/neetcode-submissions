class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)

        target = total//2

        if total %2!=0:
            return False

        dp = [False] * (target+1)
        dp[0] = True

        for i in nums:
            for j in range(target, i-1, -1):
                if dp[j-i]:
                    dp[j]=True

        return dp[target]
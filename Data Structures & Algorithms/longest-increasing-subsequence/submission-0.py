class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        print(f"Initial dp: {dp}")

        for i in range(len(nums)):
            print(f"\nEvaluating nums[{i}] = {nums[i]}")
            for j in range(i):
                print(f"  Comparing to nums[{j}] = {nums[j]}")
                if nums[i] > nums[j]:
                    print(f"    nums[{i}] > nums[{j}] → update dp[{i}] from {dp[i]} to {max(dp[i], dp[j] + 1)}")
                    dp[i] = max(dp[i], dp[j] + 1)
            print(f"  dp after index {i}: {dp}")

        print(f"\nFinal dp: {dp}")
        return max(dp)

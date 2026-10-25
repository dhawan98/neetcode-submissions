class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #idea- DP, for all the coins, we can create dp[c] 
        # if coin = 1 exists, dp[1]=1, otherwise (-1)
        # for dp[10] , i already have dp[1,2,3,...9], makes it easier
        # for every coin, i can see dp[10] like coins 1,2,5 etc. 
        # compare that to dp[9]+1 (if coin of value 1 exists)
        #. i needs to be larger than c 
        dp = [float("inf")] *(amount+1)

        dp[0] = 0
        for i in range(1, (amount+1)):
            for c in coins:
                if i>=c:
                    dp[i] = min(dp[i], 1+dp[i-c])
        return dp[-1] if dp[-1]!=float("inf") else -1
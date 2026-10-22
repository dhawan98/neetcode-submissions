class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        # pass
        res = prices.copy()

        for i, price in enumerate(prices):
            for j in range(i+1, len(prices)):
                if prices[j] <= price:
                    res[i] -= prices[j]
                    break
        return res

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []         # Final result
        subset = []      # Current subset being built

        def dfs(i):
            print(f"DFS called with i = {i}, current subset = {subset}")
            
            if i >= len(nums):
                print(f"Reached end. Adding subset to result: {subset}\n")
                res.append(subset.copy())
                return

            # Include nums[i]
            subset.append(nums[i])
            print(f"Including nums[{i}] = {nums[i]}, subset becomes {subset}")
            dfs(i + 1)

            # Backtrack and exclude nums[i]
            popped = subset.pop()
            print(f"Backtracking, removed {popped}, subset back to {subset}")
            dfs(i + 1)

        dfs(0)
        return res

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # validonly if open = closed = n
        # only add ( if open<n
        # add ) only if closed<open

        res = []
        stack = []

        def backtrack(openN, closedN):
            if openN == closedN == n:
                res.append("".join(stack))
                return
            if openN < n:
                stack.append("(")
                backtrack(openN+1, closedN)
                stack.pop()
            if openN > closedN:
                stack.append(")")
                backtrack(openN, closedN+1)
                stack.pop()
        if n>0:
            backtrack(0, 0)
        return res
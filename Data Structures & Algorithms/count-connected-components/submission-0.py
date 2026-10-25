class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        res = 0
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        visited = set()

        def dfs(node):
            for nei in graph[node]:
                if nei not in visited:
                    visited.add(nei)
                    dfs(nei)

        for node in range(n):
            if node not in visited:
                visited.add(node)
                res+=1
                dfs(node)

        return res
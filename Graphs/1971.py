# 1971. Find if Path Exists in Graph
from collections import defaultdict
class Solution:
    def validPath(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True
        
        d = defaultdict(list)
        for u, v in edges:
            d[u].append(v)
            d[v].append(u)
        
        seen = set()
        seen.add(source)
        def dfs(node):
            if node == destination:
                return True
            for nei_node in d[node]:
                if nei_node not in seen:
                    seen.add(nei_node)
                    if dfs(nei_node):
                        return True
            
            return False
        
        return dfs(source)
# 133. Clone Graph

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        o_to_n = {}
        source = node
        seen = set()
        stk = [source]
        seen.add(source)

        while stk:
            node = stk.pop()
            o_to_n[node] = Node(val=node.val)
            for nei_node in node.neighbors:
                if nei_node not in seen:
                    seen.add(nei_node)
                    stk.append(nei_node)
        
        for old_node, new_node in o_to_n.items():
            for nei_node in old_node.neighbors:
                new_node.neighbors.append(o_to_n[nei_node])
        
        return o_to_n[source]

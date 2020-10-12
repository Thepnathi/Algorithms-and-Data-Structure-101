from typing import List, Dict
from collections import Counter, namedtuple

class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self, root=None):
        self.root = TreeNode(root)
          
    def insertNodes(self, nodes: List[int]) -> None:
        queue = [self.root]
        left, right = False, False
        for node in nodes:
            newNode = TreeNode(node)
            if left is False:
                queue[0].left = newNode
                queue.append(newNode)
                left = True
            elif right is False:
                queue[0].right = newNode
                queue.append(newNode)
                right = True
            
            if left and right:
                queue.pop(0)
                left, right = False, False
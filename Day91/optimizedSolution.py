class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

class Solution:
    
    def pairSumBST(self, root, target, seen):
        
        if root == None:
            return False
        
        if (target - root.data) in seen:
            return True

        seen.add(root.data)

        if self.pairSumBST(root.left, target, seen):
            return True
        
        if self.pairSumBST(root.right, target, seen):
            return True
        
        return False

    def findTarget(self, root, target): 
        '''
        This function returns true if a pair of node sum to the target
        
        Approach:
        Use preorder traversal and hashset to check
        if difference from target is alreay seen
        
        Time Complexity: O(n)
        Space Complexity: O(h)
        '''

        seen = set()
        
        return self.pairSumBST(root, target, seen)
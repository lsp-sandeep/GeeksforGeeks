class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

class Solution:
    
    def inorderSearch(self, root, n1, n2, res):
        
        if root == None:
            return False
        
        leftCheck = self.inorderSearch(root.left, n1, n2, res)

        if root.data == n1.data or root.data == n2.data:
            rootCheck = True
        else:
            rootCheck = False

        rightCheck = self.inorderSearch(root.right, n1, n2, res)
        
        if (
            (leftCheck and rightCheck)
            or (leftCheck and rootCheck)
            or (rightCheck and rootCheck)
        ):
            res[0] = root
        
        return leftCheck or rightCheck or rootCheck
    
    def LCA(self, root, n1, n2):
        '''
        This function returns the least common ancestor of two nodes
        from a binary search tree (BST)
        
        Approach:
        1) Use inorder search to check if both the nodes are found in:
            > current node and left node
            > current node and right node
            > left node and right node
        2) If any of the above cases is met then the root is the LCA
        
        Time Complexity: O(n)
        Space Complexity: O(h)
        '''
        
        res = [None]
        
        self.inorderSearch(root, n1, n2, res)
        
        return res[0]
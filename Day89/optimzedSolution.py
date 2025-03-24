
class Node:

    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

class Solution:
    #Function to check whether a Binary Tree is BST or not.
    
    def helper(self, root, prev, prevDir):
        
        if(root == None):
            return True
        
        if(root.left != None and root.left.data > root.data):
            return False
        if(root.left != None and prev != None
            and prevDir == 'r' and root.left.data < prev.data):
            return False

        if(root.right != None and root.right.data < root.data):
            return False
        if(root.right != None and prev != None
            and prevDir == 'l' and root.right.data > prev.data):
            return False

        leftCheck = self.helper(root.left, root, 'l')
        rightCheck = self.helper(root.right, root, 'r')
        
        return leftCheck and rightCheck
    
    def isBST(self, root):

        return self.helper(root, None, "")
        

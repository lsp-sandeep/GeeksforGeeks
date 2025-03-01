class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

class Solution:

    def helper(self, root, k, aux):
        
        if(root == None):
            return
            
        self.helper(root.left, k, aux)
        aux[0] += 1
        if(aux[0] == k):
            aux[1] = root.data
        self.helper(root.right, k, aux)
        
        return

        
    def kthSmallest(self, root, k): 
        '''
        This funcitons returns the kth smallest element in the given BST 
        
        Approach:
        Use inorder traversal to count upto the kth occurance
        
        Time Complexity: O(k)
        Space Complexity: O(h)
        '''

        aux = [0, -1]

        self.helper(root, k, aux)

        return aux[1]
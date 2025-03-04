
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

class Solution:

    def inorder(self, root, aux):
        
        if root == None:
            return
        
        self.inorder(root.left, aux)
        
        if aux['prev'] != None and aux['prev'].data >= root.data:
            
            if aux['first'] == None:
                
                aux['first'] = aux['prev']
                aux['middle'] = root
            
            else:
                
                aux['last'] = root
        
        aux['prev'] = root

        self.inorder(root.right, aux)
        
        return
    
    def correctBST(self, root):
        '''
        This function returns the corrected BST
        for an input where exactly two nodes were swapped

        Approach:
        1) Inorder traversal check with prev and curr node
        2) If the check fails there are 2 scenarios
            > The swapped nodes are adjacent: Store the only fail
            > The swapped nodes are not adjacent: Store both the fails
        3) Swap the nodes at the end

        Time Complexity: O(n)
        Space Complexity: O(h)
        '''        
        aux = {
            'prev'  : None,
            'first' : None,
            'middle': None,
            'last'  : None
        }
        
        self.inorder(root, aux)
        
        if aux['last'] != None:
            
            aux['first'].data, aux['last'].data = (
                    aux['last'].data, aux['first'].data
                )
            
        else:
            
            aux['first'].data, aux['middle'].data = (
                    aux['middle'].data, aux['first'].data
                )

        return root
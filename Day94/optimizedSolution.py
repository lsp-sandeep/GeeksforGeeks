class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    #Function to serialize a tree and return a list containing nodes of tree.
    def serialize(self, root):

        res = []
        nodeQ = [root]
        
        while(len(nodeQ) > 0):

            n = len(nodeQ)

            for i in range(n):
                
                node = nodeQ.pop(0)

                res.append(
                    node.data if node != None else None
                )
                
                if node != None:

                    nodeQ.extend([node.left, node.right])

        return res

    #Function to deserialize a list and construct the tree.   
    def deSerialize(self, arr):

        root = Node(arr[0])
        nodeQ = [root]
        
        i = 1
        while i < len(arr):
            curr = nodeQ.pop(0)

            if curr != None:
                if arr[i] != None:
                    curr.left = Node(arr[i])
                    nodeQ.append(curr.left)
        
                if arr[i+1] != None:
                    curr.right = Node(arr[i+1])
                    nodeQ.append(curr.right)

                i += 2

        return root

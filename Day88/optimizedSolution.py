
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

class Solution:
    
    def treeSums(self, root, k, prefSums, currSum):
        
        if(root == None):
            return 0
        
        count = 0
        
        currSum += root.data
        
        if(currSum == k):
            count += 1
        
        count += prefSums.get(currSum - k, 0)
        
        prefSums[currSum] = prefSums.get(currSum, 0) + 1

        count += self.treeSums(root.left, k, prefSums, currSum)
        count += self.treeSums(root.right, k, prefSums, currSum)
        
        prefSums[currSum] = prefSums.get(currSum) - 1
        
        return count
    
    def sumK(self,root,k):
        
        prefSums = dict()
        
        count = self.treeSums(root, k, prefSums, 0)
        
        return count

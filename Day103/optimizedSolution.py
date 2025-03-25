class Solution:
    
    def getNextSmaller(self, arr):
        n = len(arr)
        nextS = []
        
        for i in range(n - 1, -1, -1):
            
            j, idx = i + 1, i + 1
            
            while j < n and arr[j] >= arr[i]:
                idx = nextS[n - j - 1]
                j = nextS[n - j - 1]
                
            nextS.append(idx)
        nextS.reverse()
        return nextS

    def getPrevSmaller(self, arr):
        n = len(arr)
        prevS = []
        
        for i in range(n):
            
            j, idx = i - 1, i - 1
            
            while j >= 0 and arr[j] >= arr[i]:
                idx = prevS[j]
                j = prevS[j]
                
            prevS.append(idx)
        
        return prevS

    def getMaxArea(self, arr):
        
        maxArea = -float('inf')
        nextS = self.getNextSmaller(arr)
        prevS = self.getPrevSmaller(arr)

        for i in range(len(arr)):
            area = arr[i] * (nextS[i] - prevS[i] - 1)
            maxArea = max(maxArea, area)
            
        return maxArea
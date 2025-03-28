
class Solution:
    
    def nextSmaller(self, arr):
        n = len(arr)
        nextS = []
        
        for i in range(n - 1, -1, -1):
            
            idx = i + 1
            
            while idx < n and arr[idx] >= arr[i]:
                idx = nextS[n - idx - 1]
            
            nextS.append(idx)
        
        nextS.reverse()
        
        return nextS

    def prevSmaller(self, arr):
        n = len(arr)
        prevS = []
        
        for i in range(n):
            
            idx = i - 1
            
            while idx >= 0 and arr[idx] >= arr[i]:
                idx = prevS[idx]
            
            prevS.append(idx)
        
        return prevS

    def maxOfMins(self, arr):
        n = len(arr)
        nextS = self.nextSmaller(arr)
        prevS = self.prevSmaller(arr)

        res = [0] * n 
        
        for i in range(n):
            w = nextS[i] - prevS[i] - 2

            res[w] = max(arr[i], res[w])

        prevMax = -float('inf')
        
        for i in range(n - 1, -1, -1):
            prevMax = max(prevMax, res[i])
            res[i] = prevMax

        return res
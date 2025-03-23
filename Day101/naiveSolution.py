class Solution:
    def nextLargerElement(self, arr):
    # Function to find the next greater element for each element of the array.

        for i in range(len(arr)-1):
            nextGreater = -1
            
            for j in range(i + 1, len(arr)):
                if arr[j] > arr[i]:
                    nextGreater = arr[j]
                    break

            arr[i] = nextGreater
            
        arr[-1] = -1    
        
        return arr
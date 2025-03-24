class Solution:

    def nextLargerElement(self, arr):
        '''
        Function to find the next greater element for each element of the array.
        
        Approach:
        1) Iterate the array from the end
        2) Keep track of each element in a stack
        3) Remove from the stack if the element is less than current element
        4) Update the element that greater at the current element after
            adding current element to stack
        5) Update the current element to -1 id stack becomes empty
        
        Time Complexity: O(n)
        Space Complexity: O(n)
        '''
        stack = []

        for i in range(len(arr)-1, -1, -1):
            nextG = -1
            
            while len(stack) > 0:
                top = stack[-1]
                if top > arr[i]:
                    nextG = top
                    break
                else:
                    stack.pop()

            stack.append(arr[i])
            arr[i] = nextG
        
        return arr
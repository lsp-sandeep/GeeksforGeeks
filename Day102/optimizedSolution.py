class Solution:
    def calculateSpan(self, arr):
        '''
        This function returns the span of a series of daily stock prices,
        where span is defined as the maximum number of consecutive days
        from the current day when the price is less than or equal to the
        current day.
        
        Approach:
        1) Iterate the array and compare with previous elements
        2) Increment the current span by the span of the previous
           element if lesser and jump by those many indices
        3) Break from the comparison once a greater element is found
        
        Time Complexity: O(n)
        Space Complexity: O(n)
        '''
        res = []

        for i in range(len(arr)):
            j, span = i - 1, 1

            while arr[j] <= arr[i] and j >= 0:
                span += res[j]
                j -= res[j]

            res.append(span)

        return res            

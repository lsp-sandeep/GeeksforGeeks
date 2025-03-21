class Solution:
    def maxLength(self, s):
        '''
        This function finds the longest valid substring
        
        Approach:
        1) Iterate the string from left to right
        2) Keep track of left and right paranthesis count
        3) if left and right counts are equal update the max length
        4) if left count is less than right count reset the counts
        5) Repeat the above steps by iterating right to left
        6) Reset the counts if right count is less than left
        7) Return the max len after the iterations
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        '''
        lCount = rCount = maxLen = 0
        
        for i in range(len(s)):
            if s[i] == '(':
                lCount += 1
            else:
                rCount += 1
            
            if lCount == rCount:
                maxLen = max(maxLen, lCount + rCount)
            elif lCount < rCount:
                lCount = rCount = 0
        
        lCount = rCount = 0

        for i in range(len(s)-1, -1, -1):
            if s[i] == '(':
                lCount += 1
            else:
                rCount += 1
            
            if lCount == rCount:
                maxLen = max(maxLen, lCount + rCount)
            elif rCount < lCount:
                lCount = rCount = 0

        return maxLen

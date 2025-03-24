class Solution:
    def findPermutation(self, s):
        '''
        This function returns all the unique permutations of the string
        
        Recursive Approach:
        1) Base case returns list of single character
        2) Iterative ignore each character and make a recursive call
        3) Append the ignored character to the end of the array
        
        Time Complexity: O(n*n!)
        Space Complexity: O(n!)
        '''
        result = []
        
        # Base Case
        if len(s) == 1:
            return [s[0]]
            
        for i in range(len(s)):
            # Ignore each character
            subs = s[:i] + s[i+1:]

            # Recursive call
            perms = self.findPermutation(subs)

            # Append the ignored character to the end
            for p in range(len(perms)):

                perms[p] = perms[p] + s[i]

            # Add the permutations to the result
            result.extend(perms)
        
        # Return the uniqur set of results
        return list(set(result))

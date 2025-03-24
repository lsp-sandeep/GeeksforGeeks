class Solution:
    
    def wordSearch(self, mat, word, r, c, w):
        
        m, n = len(mat), len(mat[0])

        if mat[r][c] != word[w]:
            return False

        if w == len(word) - 1:
            return True
            
        pos = []
        
        if r > 0:
            pos.append((r - 1, c))
        if c > 0:
            pos.append((r, c - 1))
        if r < m - 1:
            pos.append((r + 1, c))
        if c < n - 1:
            pos.append((r, c + 1))
        
        temp = mat[r][c]
        
        for p in pos:
            mat[r][c] = "."
            if self.wordSearch(mat, word, p[0], p[1], w + 1):
                return True
            mat[r][c] = temp
        
        return False
    
    def isWordExist(self, mat, word):
        '''
		This function returns if solution exists for a word search puzzle
		
		Approach:
		1) Iterate for each cell of matrix to start word search
		2) Recursively check adjacent cell for each next character
		3) Return true if all characters are covered else false
		
		Time Complexity: O(m*n*(3^w))
		Space Complexity: O(w)
		'''
        
        m, n = len(mat), len(mat[0])
        
        for r in range(m):
             for c in range(n):
                  if self.wordSearch(mat, word, r, c, 0):
                      return True

        return False

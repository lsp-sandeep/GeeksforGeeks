class Solution:
    
    def isSafe(self, num, idx, row, col, box):
        '''
        This function checks if the given num is aready used with
        the help of bitmask for row, col and box
        '''
        
        r = idx // 9; c = idx % 9
        
        if (
            (row[r] & (1 << num))
            or (col[c] & (1 << num))
            or (box[(r // 3) * 3 + c // 3] & (1 << num))
        ):
            return False
        
        return True

    def recursiveSudoku(self, mat, idx, row, col, box):
        '''
        This function iterates each safe digit for each cell recursively
        '''
        
        while idx < 81 and mat[idx // 9][idx % 9] != 0:
            
            idx += 1
        
        if idx == 81:
            
            return True

        r = idx // 9; c = idx % 9

        for num in range(1 ,10):

            if self.isSafe(num, idx, row, col, box):
                
                mat[r][c] = num
                
                row[r] |= (1 << num)
                col[c] |= (1 << num)
                box[(r // 3) * 3 + c // 3] |= (1 << num)
                
                res = self.recursiveSudoku(mat, idx + 1, row, col, box)
                
                if res:
                    return res

                mat[r][c] = 0

                row[r] &= ~(1 << num)
                col[c] &= ~(1 << num)
                box[(r // 3) * 3 + c // 3] &= ~(1 << num)
        
        return False
        
    
    #Function to find a solved Sudoku. 
    def solveSudoku(self, mat):
        '''
        This function return the solution for a valid sudoku puzzle
        
        Approach:
        1) Initialize bitmask of used digits for each row, col and box
        2) Iterate each safe digit for each cell via recursive call
        3) Return the matrix once the last cell is reached
        
        Time Complexity: O(9^(n*n))
        Space Complexity: O(n)
        '''
        
        n = len(mat)
        row = [0] * n
        col = [0] * n
        box = [0] * n
        
        for i in range(n):
            for j in range(n):
                if mat[i][j] != 0:
                    row[i] |= (1 << mat[i][j])
                    col[j] |= (1 << mat[i][j])
                    box[(i // 3) * 3 + j // 3] |= (1 << mat[i][j])
        
        res = self.recursiveSudoku(mat, 0, row, col, box)

class Solution:

    def nQueenRecursion(self, row, n, cols, posDiag, negDiag, board, res):
        '''
        This function performs:
        1) recursive call for each row
        2) iterates for each possible unvisited column
        3) Storing the board when last row is reached
        '''
        
        
        if row == n:
            res.append(board.copy())
            return
        
        for col in range(n):
            
            if cols[col] or posDiag[row + col] or negDiag[row - col + n - 1]:
                continue
            
            board.append(col + 1)
            
            cols[col] = True; posDiag[row + col] = True; negDiag[row - col + n - 1] = True;
            
            self.nQueenRecursion(row + 1, n, cols, posDiag, negDiag, board, res)
            
            board.pop()
        
            cols[col] = False; posDiag[row + col] = False; negDiag[row - col + n - 1] = False;
    
    def nQueen(self, n):
        '''
        This function returns the solution for the n-quees puzzle
        
        The n-queens puzzle is the problem of placing n queens on
        a (nxn) chesboard such that no two queens can attack each other
        
        Approach:
        1) Initialize a lists for tracking visited columns and diagonals
        2) Iterate for each unvisited column in each row till the last row
        3) Store the positions on the board each time the last row is reached
        
        Time Complexity: O(n!)
        Space Complexity: O(n)
        '''
        
        res = []
        board = []
    
        cols = [False] * n
        posDiag = [False] * (2*n - 1)
        negDiag = [False] * (2*n - 1)
        
        self.nQueenRecursion(0, n, cols, posDiag, negDiag, board, res)
        
        return res
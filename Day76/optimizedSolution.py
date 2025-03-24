class Solution:
    # Optimized Approach
    def power(self, b: float, e: int) -> float:
        '''
        This function returns the result of float b raised to the power of int e
        (without using the inbuilt operator)
        
        Recursive Approach:
        1) Base Case: if e is 0 return 1
        2) if e < 0 then invert the positive exponent
        3) Calculate the result of b raised to half of e using recursive call
        4) If e is even return by multiplying the above result with itself
        5) If e is odd return by multiplying b and the above result with itself
        '''
        
        # Base Case
        if e == 0:
            return 1
        
        # Negative exponent
        if e < 0:
            return 1 / self.power(b, -e)
        
        # Half exponent
        halfPower = self.power(b, e//2)
        
        # Handling even and odd cases
        if e % 2 == 0:
            return halfPower * halfPower
        else:
            return b * halfPower * halfPower
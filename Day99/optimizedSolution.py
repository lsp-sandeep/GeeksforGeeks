class Solution:
    def isBalanced(self, s):
        '''
        This function checks if paranthesis are balanced
        
        Approach:
        1) Check if the length is even
        2) Initialize a mapping of close to open paranthesis
        3) Initialize a stack of paranthesis and traverse the string:
            a) if the char is opening then add to the stack
            b) else if the stack is not empty and char is the
               closing of last element in stack then remove the last element
            c) other wise return as not balanced
        4) if the string is traversed to end
            a) if the length of stack is empty then it is balanced
            b) else it is not balanced
        
        Time Complexity: O(n)
        Space Complexity: O(n)
        '''
        if len(s) % 2 != 0:
            return False

        paraMap = {
            '}': '{',
            ')': '(',
            ']': '['
        }
        paraStack = []
        
        for p in s:
            if p not in paraMap:
                paraStack.append(p)
            elif len(paraStack) > 0 and paraMap.get(p, '') == paraStack[-1]:
                paraStack.pop()
            else:
                return False
        
        if len(paraStack) > 0:
            return False
        
        return True
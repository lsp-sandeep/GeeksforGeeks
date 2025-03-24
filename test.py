#%%
def spirallyTraverse(mat):
    # code here
    rows, cols = len(mat), len(mat[0])
    
    vis_mat = [[False] * cols for _ in range(rows)]

    dr = [0, 1,  0, -1]
    dc = [1, 0, -1,  0]

    r, c, idx = 0, 0, 0
    out = []
    
    for _ in range(rows * cols):
        
        out.append(mat[r][c])
        vis_mat[r][c] = True

        new_r = r + dr[idx]
        new_c = c + dc[idx]

        if not (0 <= new_r < rows) or not (0 <= new_c < cols) or vis_mat[new_r][new_c]:
            idx = (idx + 1) % 4
            r += dr[idx]
            c += dc[idx]
        else:
            r, c = new_r, new_c        

    return out
#%%
mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(spirallyTraverse(mat))
#%%

def maxLength(s):
    # code here
    maxLen, curLen = 0, 0
    paraStack, maxPara, curPara = [], [], []
    for c in s:
        if c == '(':
            paraStack.append(c)
            curPara.append(c)
        elif len(paraStack) > 0 and paraStack[-1] == '(':
            curPara.append(c)
            paraStack.pop()
            curLen += 2
        else:
            paraStack = []
            curLen = 0
            curPara = []
        
        if curLen > maxLen:
            maxLen = curLen
            maxPara = curPara
        
    print("".join(maxPara))

    return maxLen

#%%

input = '()()))())))))(())())))()))))()((()(((((((()(()()))()(()())))((()((((((()))))()(())(((((())((((((((()))((())()(()())()(()(()(()))))))))))))))()()((()((())))())()(())(()(()(()(()))))(()()((()(((()())))(()()())((())((((()()()()())()()()()))))(()()(()()((()(()))))))(())()(()))((())(()()()((())((((((()()))(()()()(()((())()()((((((())(((((())(((())))((((()()))()(())(())()))(()(())(((()(()())())(()())()((()()(()(()()()())((((()((()(()(((((())((()(((())(()()(())))))))))(()())((())()((()()()()()))))(((()))(()()())(()))()()))()))))()))))((())((())((()((())()))(()()))))(()))()))()()))))()(())()((())(()())()()()()()))()))()((((((()))))()())))))(()()(()())()((()(((()()))((()((()()(()()()()((())(())(()))())((()())))))())())()()(()())((())(((())(())(((()())()()(()(((())())()()(((()(()))())()()()((())((()()((((((((()()((()(((())()())))()()(()((()(())))))()((()))(()((()(())((()(())(((((('

maxLength(input)

#%%
class Node:

    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

def helper(self, root, prev, k):
    
    k+=1

    if(root == None or k > 10):
        return True

    print(root.data, prev.data if prev != None else None, end= " ")    
    if(
        (root.left != None and root.left.data > root.data)
        or (prev != None and root.left.data > prev.data)
        ):
        print(root.left != None and root.left.data > root.data, end= " ")
        print(prev != None and root.left.data > prev.data, end= " ")
        return False
        
    leftCheck = self.helper(root.left, root, k)

    if(
        (root.right != None and root.right.data < root.data)
        or (prev != None and root.right.data < prev.data)
        ):
        print(root.right != None and root.right.data < root.data, end= " ")
        print(prev != None and root.right.data < prev.data, end= " ")
        return False

    rightCheck = self.helper(root.right, root, k)
    
    return leftCheck and rightCheck

def isBST(self, root):

    return self.helper(root, None, 0)

#%%

root = Node(2)
root.left = Node(1)
root.right = Node(3)
root.right.right = Node(5)

print(isBST(root))

#%%

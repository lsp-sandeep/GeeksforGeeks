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

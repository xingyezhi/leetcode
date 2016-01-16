__author__ = 'lenovo'
# coding=utf-8

class Solution:
    # @param {character[][]} board
    # @return {boolean}
    def isValidSudoku(self, board):
        row=[0]*9
        column=[0]*9
        sub=[0]*9
        for i in range(len(board)):
            for j in range(len(board[0])):
                v=board[i][j]
                if v=='.':
                    continue
                else:
                    v=int(v)
                    if (1<<v)&row[i]:
                        return False
                    elif (1<<v)&column[j]:
                        return False
                    subIndex=(i/3)*3+j/3
                    if (1<<v)&sub[subIndex]:
                        return False
                    row[i]|=(1<<v)
                    column[j]|=(1<<v)
                    sub[subIndex]|=(1<<v)
        else:
            return True


sol=Solution()
print sol.isValidSudoku([".87654321","2........","3........","4........","5........","6........","7........","8........","9........"])
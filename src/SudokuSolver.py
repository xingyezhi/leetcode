__author__ = 'lenovo'
# coding=utf-8

class Solution:
    # @param {character[][]} board
    # @return {void} Do not return anything, modify board in-place instead.
    def __init__(self):
        self.row=[0]*9
        self.column=[0]*9
        self.sub=[0]*9
    def isValid(self,v,i,j):
        subindex=(i/3)*3+j/3
        if self.row[i]&(1<<v):
            return False
        elif self.column[j]&(1<<v):
            return False
        elif self.sub[subindex]&(1<<v):
            return False
        else:
            return True
    def getAnswer(self,board,posNode,index):
        if index==len(posNode):
            return True
        i,j=posNode[index][0],posNode[index][1]
        subindex=(i/3)*3+j/3
        for v in range(1,10):
            if self.isValid(v,i,j):
                self.row[i]|=(1<<v)
                self.column[j]|=(1<<v)
                self.sub[subindex]|=(1<<v)
                board[i][j]=str(v)
                if self.getAnswer(board,posNode,index+1):
                    return True
                else:
                    self.row[i]&=~(1<<v)
                    self.column[j]&=~(1<<v)
                    self.sub[subindex]&=~(1<<v)
                    board[i][j]='.'
        else:
            return False


    def solveSudoku(self, board):
        posNode=[]
        for i in range(len(board)):
            board[i]=list(board[i])
            for j in range(len(board[0])):
                if board[i][j]=='.':
                    posNode.append((i,j))
                else:
                    v=int(board[i][j])
                    self.row[i]|=(1<<v)
                    self.column[j]|=(1<<v)
                    subindex=(i/3)*3+j/3
                    self.sub[subindex]|=(1<<v)
        if self.getAnswer(board,posNode,0):
            for i in range(len(board)):
                board[i]=('').join(board[i])

sol=Solution()
print sol.solveSudoku(["..9748...","7........",".2.1.9...","..7...24.",".64.1.59.",".98...3..","...8.3.2.","........6","...2759.."])

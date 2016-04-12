__author__ = 'xingyezhi'
# encoding: utf-8

class Solution(object):
    def change(self,board,i,j): #'X'
        stack=[(i,j)]
        while len(stack)!=0:
            top=stack.pop()
            board[top[0]][top[1]]='Y'
            for v in self.local:
                x,y=top[0]+v[0],top[1]+v[1]
                if 0<=x<self.m and 0<=y<self.n and board[x][y]=='O':
                    stack.append((x,y))

    def solve(self, board):
        self.local=[[-1,0],[1,0],[0,-1],[0,1]]
        if len(board)==0:return
        self.m,self.n=len(board),len(board[0])
        for i in range(self.m):
            if board[i][0]=='O':
                self.change(board,i,0)
            if board[i][self.n-1]=='O':
                self.change(board,i,self.n-1)
        for j in range(self.n):
            if board[0][j]=='O':
                self.change(board,0,j)
            if board[self.m-1][j]=='O':
                self.change(board,self.m-1,j)
        for i in range(self.m):
            for j in range(self.n):
                if board[i][j]=='Y':
                    board[i][j]='O'
                else:board[i][j]='X'
sol=Solution()
sol.solve(
[
['X','X','X','X'],
['X' ,'O' ,'O','X'],
['X','X' ,'O', 'X'],
['X','O','X','X']
])
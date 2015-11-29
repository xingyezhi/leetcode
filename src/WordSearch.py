__author__ = 'xingyezhi'
# encoding: utf-8

class Solution(object):
    def dfs(self,i,j,k,map):
        if k==len(self.word)-1:
            return True
        for s in self.dir:
            x,y=i+s[0],j+s[1]
            if self.safe(x,y,map) and self.board[x][y]==self.word[k+1]:
                map[x][y]=True
                if self.dfs(x,y,k+1,map):
                    return True
                map[x][y]=False
        else:
            return False
    def safe(self,i,j,map):
        return 0<=i<self.m and 0<=j<self.n and (not map[i][j])
    def exist(self, board, word):

        m,n=len(board),len(board[0])
        self.board,self.word,self.m,self.n=board,word,m,n
        self.dir=[[-1,0],[1,0],[0,-1],[0,1]]
        for i in range(m):
            for j in range(n):
                if board[i][j]==word[0]:
                    map=[[False]*n for w in range(m)]
                    map[i][j]=True
                    if self.dfs(i,j,0,map):
                        return True
        else:
            return False


sol=Solution()

print sol.exist(["ABCE","SFCS","ADEE"],"ABCCED")
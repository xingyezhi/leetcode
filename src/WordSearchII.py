# coding=utf-8
__author__ = 'lenovo'

class TrieNode(object):
    def __init__(self,val):
        self.val=val
        self.leaf=False
        self.chirld=[None for i in range(26)]


class Solution(object):
    def insert(self, word,root):
        cur=root
        for i in word:
            index=ord(i)-97
            if cur.chirld[index]==None:
                newchirld=TrieNode(i)
                cur.chirld[index]=newchirld
            cur=cur.chirld[index]
        cur.leaf=True
    def dfs(self,i,j,board,root,tempstr,visit):
        if not (0<=i<len(board) and 0<=j<len(board[0])):
            return
        if visit[i][j]==True:return
        index=ord(board[i][j])-97
        if root.chirld[index]==None:return
        elif root.chirld[index].leaf:
            tempstr.append(board[i][j])
            self.result.append(''.join(tempstr))
            root.chirld[index].leaf=False
            tempstr.pop()
        visit[i][j]=True
        tempstr.append(board[i][j])
        self.dfs(i-1,j,board,root.chirld[index],tempstr,visit)
        self.dfs(i,j-1,board,root.chirld[index],tempstr,visit)
        self.dfs(i+1,j,board,root.chirld[index],tempstr,visit)
        self.dfs(i,j+1,board,root.chirld[index],tempstr,visit)
        visit[i][j]=False
        tempstr.pop()
    def findWords(self, board, words):
        root = TrieNode("")
        self.result=[]
        visit=[[False for i in range(len(board[0]))] for j in range(len(board))]
        for word in words:
            self.insert(word,root)
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(i,j,board,root,[],visit)
        return self.result
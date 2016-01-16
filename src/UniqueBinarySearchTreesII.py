# coding=utf-8
__author__ = 'lenovo'

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.map={}
        self.map[0]=[['*']]
        self.map[1]=[[0,'*','*']]
        self.map[2]=[[1,0,"*",'*','*'],[0,"*",1,'*','*']]
    def getTree(self,number,value):
        treelist=self.map[number]
        result=[]
        for i in treelist:
            temp=[]
            for j in i:
                temp.append(value[j] if j!='*' else j)
            result.append(temp)
        return result
    def generateTree(self,n,value):
        if self.map.has_key(n):
            return self.getTree(n,value)
        result=[]
        for i in range(len(value)-1,-1,-1):
            left,right=i,len(value)-i-1
            lefttree=[['*']] if left==0 else self.generateTree(left,value[:i])
            rihttree=[['*']] if right==0 else self.generateTree(right,value[i+1:])
            for x in lefttree:
                for y in rihttree:
                    temp=[value[i]]
                    temp.extend(x)
                    temp.extend(y)
                    result.append(temp)
        self.map[n]=result
        return result
#[9, 7, 6, 4, 0, '*', 1, '*', 2, '*', 3, '*', '*', 5, '*', '*', '*', 8, '*', '*', '*']
    def init_tree(self,list,i):
        if i==len(list) or list[i]=='*':
            return None,i
        root=TreeNode(list[i]+1)
        left,index=self.init_tree(list,i+1)
        right,rindex=self.init_tree(list,index+1)
        root.left=left
        root.right=right
        return root,rindex
    def printTree(self,treelist):
        result=[self.init_tree(tree,0)[0] for tree in treelist]
        return result

    def generateTrees(self, n):
        if n==0:return []
        tree=self.generateTree(n,range(n))
        return self.printTree(tree)
sol=Solution()
print len(sol.generateTrees(9))

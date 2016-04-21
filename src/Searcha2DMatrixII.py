# coding=utf-8
__author__ = 'lenovo'


class Solution(object):
    def searchMatrix(self, matrix, target):
        self.matrix=matrix
        self.target=target
        return self.Bsearch((0,0),(len(matrix)-1,len(matrix[0])-1))
    def Bsearch(self,left,right):
        print left,right
        print len(self.matrix),len(self.matrix[0])
        if not (0<=left[0]<=right[0]<len(self.matrix) and 0<=left[1]<=right[1]<len(self.matrix[0])):
            return False
        if left==right:
            return self.matrix[left[0]][left[1]]==self.target and True or False
        mid=[(left[i]+right[i])/2 for i in [0,1]]
        if self.matrix[mid[0]][mid[1]]==self.target:
            return True
        elif self.matrix[mid[0]][mid[1]]<self.target:
            return self.Bsearch((mid[0]+1,mid[1]+1),right) or self.Bsearch((left[0],mid[1]+1),(mid[0],right[1])) or self.Bsearch((mid[0]+1,left[1]),(right[0],mid[1]))
        else:
            return self.Bsearch(left,(mid[0]-1,mid[1]-1)) or self.Bsearch((left[0],mid[1]),(mid[0]-1,right[1])) or self.Bsearch((mid[0],left[1]),(right[0],mid[1]-1))

sol=Solution()
print sol.searchMatrix([
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
],20)
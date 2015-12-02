__author__ = 'lenovo'
# coding=utf-8

class Solution(object):
    def spiralOrder(self,matrix):
        result=[]
        r=len(matrix)
        if r==0:return result
        l=len(matrix[0])
        map=[[False for i in range(l)] for j in range(r)]
        x=y=counts=0
        result.append(matrix[0][0])
        map[0][0]=True
        counts+=1
        while counts<l*r:
            while y+1<l and (not map[x][y+1]):
                y+=1;counts+=1
                result.append(matrix[x][y])
                map[x][y]=True
            while x+1<r and (not map[x+1][y]):
                x+=1;counts+=1
                result.append(matrix[x][y])
                map[x][y]=True
            while y-1>=0 and (not map[x][y-1]):
                y-=1;counts+=1
                result.append(matrix[x][y])
                map[x][y]=True
            while x-1>=0 and (not map[x-1][y]):
                x-=1;counts+=1
                result.append(matrix[x][y])
                map[x][y]=True
        return result

        return result


sol=Solution()
print sol.spiralOrder([[2,5],[8,4],[0,-1]])
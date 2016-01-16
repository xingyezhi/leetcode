__author__ = 'lenovo'
# coding=utf-8

class Solution:
    # @param {integer} n
    # @return {string[]}
    def getString(self,stack,counts,strs):
        result=[]
        if counts<self.n:
            if stack==0:
                return self.getString(stack+1,counts+1,strs+'(')
            else:
                temp=self.getString(stack+1,counts+1,strs+'(')
                stack-=1
                temp2=self.getString(stack,counts,strs+')')
                for i in temp:
                    result.append(i)
                for i in temp2:
                    result.append(i)
                return result
        else:
            if stack==0:
                return [strs]
            else:
                for i in range(stack):
                    strs+=')'
                return [strs]



    def generateParenthesis(self, n):
        self.n=n
        return self.getString(0,0,"")

sol=Solution()
print sol.generateParenthesis(3)


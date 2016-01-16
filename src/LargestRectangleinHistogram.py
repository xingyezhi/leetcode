__author__ = 'lenovo'
# coding=utf-8

class Solution(object):
    def getLargest(self,stack):
        if len(stack)==0:return 0
        result,maxi=stack[0][1],stack[0][2]
        for mid in stack[1:]:
            result=max(mid[1]*(maxi-mid[0]+1),result)
        return result

    def largestRectangleArea(self, height):
        if len(height)==0:return 0
        result,stack=0,[]
        for i,v in enumerate(height):
            point,tempstack=i,[]
            while len(stack)!=0 and stack[-1][1]>=v:
                mid=stack.pop()
                point=mid[0]
                tempstack.append(mid)
            if len(tempstack)>0:result=max(v*(i-tempstack[-1][0]+1),result)
            result=max(result,self.getLargest(tempstack))
            stack.append((point,v,i))
            #print stack,result
        result=max(result,self.getLargest(stack[::-1]))
        return result

sol=Solution()
print sol.largestRectangleArea([6,4,2,0,3,2,0,3,1,4,5,3,2,7,5,3,0,1,2,1,3,4,6,8,1,3])
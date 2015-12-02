__author__ = 'lenovo'
# coding=utf-8

class Solution(object):
    def multiply_single(self,num1,num2):
        result=[]
        temp=0
        for k in num1[::-1]:
            mul=num2*k+temp
            temp=mul/10
            result.append(mul%10)
        if temp!=0:result.append(temp)
        return result[::-1]
    def add(self,num1,num2):
        result=[]
        temp=0
        for i in range(min(len(num1),len(num2))):
            c=num1[-(i+1)]+num2[-(i+1)]+temp
            result.append(c%10)
            temp=c/10
        if len(num1)!=len(num2):
            remain=num1[len(num1)-len(num2)-1::-1] if len(num1)>len(num2) else num2[len(num2)-len(num1)-1::-1]
            for i in remain:
                c=i+temp
                result.append(c%10)
                temp=c/10
        if temp!=0:result.append(temp)
       # print result[::-1]
        return result[::-1]
    def multiply(self, num1, num2):
        list1=[int(k) for k in num1]
        list2=[int(k) for k in num2]
        result=[]
        for k in range(len(num2)):
            temp=self.multiply_single(list1,list2[-(k+1)])
            temp.extend([0]*k)
        #    print "temp",temp
            result=self.add(result,temp)
        #    print "result",result
        for start in range(len(result)):
            if result[start]!=0:
                break
        result=''.join([str(k) for k in result[start:]])
        #print result
        return result

sol=Solution()
print sol.multiply("237","284")
t=[1,2,3,4]
print t[3:-1:-1]

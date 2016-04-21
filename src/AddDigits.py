# coding=utf-8
__author__ = 'lenovo'

# class Solution(object):
#     def addDigits(self, num):
#         return 0 if num==0 else 1+(num-1)%9

map={}
def F(A,B):
    if (A,B) in map:
        return map[(A,B)]
    if A==1:return 1
    elif B==1:return A
    result=0
    for i in range(A,0,-1):
        result+=F(i,B-1)
    map[(A,B)]=result
    return result

print F(3,2)

result=1
for i in range(1,55):
    result*=i
print result
print result/(F(28,27)**4)
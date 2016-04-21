# coding=utf-8
__author__ = 'lenovo'

result=100001

def dfs(count,p,temp,result):
    if count==6:
        temp+=p*100000
        result=min(temp,result)
        return
    for j in range(1,100001):
        dfs(count+1,p*(1-float(j)/100000),temp+float(j)/100000,result)
    return result

result=100001
print dfs(1,1,0,100001)


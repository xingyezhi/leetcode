__author__ = 'lenovo'
# coding=utf-8

def printResult(map,begin,sum):
    if sum==0:
        for key in map:
            print key,
        print
        return
    for i in range(begin,sum+1):
        if map.has_key(i):
            continue
        else:
            map[i]=1
            printResult(map,i+1,sum-i)
            map.pop(i)

printResult({},1,10)

# 1+9=10
# 1+2+7=10
# 1+2+3+4=10
# 1+3+6=10
# 1+4+5=10
# 2+8=10
# 2+3+5=10
# 3+7=10
# 4+6=10
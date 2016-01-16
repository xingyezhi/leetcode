__author__ = 'lenovo'
# coding=utf-8

class Solution(object):
    def countAndSay(self, n):
        start="1"
        for i in range(1,n):
            j,temp=0,""
            while j<len(start):
                counts=1
                v=start[j]
                j+=1
                while j<len(start) and start[j]==v:
                    counts+=1
                    j+=1
                temp+=str(counts)+v
            start=temp
        return start

sol=Solution()
print sol.countAndSay(4)
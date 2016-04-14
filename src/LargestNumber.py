__author__ = 'xingyezhi'
# encoding: utf-8
def cmpstr(s1,s2):
    r1=s1+s2
    r2=s2+s1
    return r1>r2
class Solution(object):
    def cmpstr(self,s1,s2):
        r1=s1+s2
        r2=s2+s1
        if r1>r2:return 1
        return -1
    def largestNumber(self, nums):
        strlist=[str(i) for i in nums]
        strlist.sort(cmp=self.cmpstr,reverse=True)
        for i in range(len(strlist)):
            if strlist[i]!='0':
                break
        if i==len(strlist):return '0'
        return ''.join(strlist[i:])
sol=Solution()
print sol.largestNumber([0,1,0])

x,y='3','30'
print (x+y)>(y+x)




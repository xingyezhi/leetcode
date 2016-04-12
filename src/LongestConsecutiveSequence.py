__author__ = 'xingyezhi'
# encoding: utf-8

class Solution(object):
    def longestConsecutive(self, nums):
        less,more,other,result={},{},{},0
        for i in nums:
            if other.has_key(i):
                continue
            other[i]=True
            if less.has_key(i-1):
                less[i]=less[i-1]+1
            else:
                less[i]=1
            if more.has_key(i+1):
                more[i]=more[i+1]+1
            else:
                more[i]=1
            if less.has_key(i+1) and less.has_key(i+more[i]-1):
                    less[i+more[i]-1]+=less[i]
            if more.has_key(i-1) and more.has_key(i-less[i]+1):
                    more[i-less[i]+1]+=more[i]
            print i,less,more
        for i in nums:
            result=max(result,more[i]+less[i]-1)
        return result

sol=Solution()
print sol.longestConsecutive([2])

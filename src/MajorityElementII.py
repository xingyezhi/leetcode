# coding=utf-8
__author__ = 'lenovo'

class Solution(object):
    def majorityElement(self, nums):
        count1,count2,n1,n2=0,0,1,2
        for n in nums:
            if n==n1:
                count1+=1
            elif n==n2:
                count2+=1
            elif count1==0:
                count1,n1=1,n
            elif count2==0:
                count2,n2=1,n
            else:
                count1-=1
                count2-=1
        return [n for n in (n1,n2) if nums.count(n)>len(nums)/3]


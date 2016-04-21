# coding=utf-8
__author__ = 'lenovo'

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        from collections import deque
        queue=deque()
        result=[0]*(len(nums)-k+1)
        cur=0
        for i in range(len(nums)):
            if len(queue)!=0 and queue[0]<=i-k:
                queue.popleft()
            while len(queue)!=0 and queue[-1]<i and nums[queue[-1]]<nums[i]:
                queue.pop()
            queue.append(i)
            if i>=k-1:
                result[cur]=queue[0]
                cur+=1
        result=[nums[i] for i in result]
        return result



sol=Solution()
sol.maxSlidingWindow([1,3,-1,-3,5,3,6,7],3)
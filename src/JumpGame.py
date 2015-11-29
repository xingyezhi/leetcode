__author__ = 'xingyezhi'
# encoding: utf-8
# class Solution(object):
#     def get_max(self,nums,start,end):
#         maxs=0
#         for i in range(start,end+1):
#             maxs=max(nums[i]+i,maxs)
#         return maxs
#     def canJump(self, nums):
#         if len(nums)==1:return True if nums[0]!=0 else False
#         i=number=0
#         max2=maxs=nums[0]
#         while(i<len(nums)):
#          #   print i
#             number+=1
#             if(maxs>=len(nums)-1):
#                 return True
#             max2=maxs
#             tempindex=self.get_max(nums,i,maxs)
#             #print tempindex
#             i,maxs=maxs+1,tempindex
#             if maxs==max2:
#                 return False
#
# sol=Solution()
# print sol.canJump([0])

class Solution(object):
    def canJump(self, nums):
        if nums[0]==0 and len(nums)!=1:
            return False
        e=maxs=nums[0]
        result=1
        for i in range(1,len(nums)-1):
            maxs=max(nums[i]+i,maxs)
            if i==e:
                if maxs==e:
                    return False
                result+=1
                e=maxs
        return True


sol=Solution()
print sol.canJump([2,3,1,1,4])
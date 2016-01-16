__author__ = 'lenovo'
# coding=utf-8

class Solution:
    # @param {integer[]} nums1
    # @param {integer[]} nums2
    # @return {float}
    def findMedianSortedArrays(self, nums1, nums2):
        l=len(nums1)+len(nums2)
        if l&1:
            return self.anOtherMethod(nums1,nums2,l/2+1)
        else:
            a=self.anOtherMethod(nums1,nums2,l/2)
            b=self.anOtherMethod(nums1,nums2,l/2+1)
            return (float(a)+float(b))/2

    def anOtherMethod(self,nums1,nums2,k):
        print "nums1",nums1
        print "nums2",nums2
        print "k",k
        if len(nums1)==0:
            return nums2[k-1]
        elif len(nums2)==0:
            return nums1[k-1]
        if k==1:
            return min(nums1[0],nums2[0])
        l1=min(k/2,len(nums1))
        l2=min(k-k/2,len(nums2))
        num1=nums1[l1-1]
        num2=nums2[l2-1]
        if num1==num2:
            return num1
        elif num1<num2:
            if len(nums1)>l1:
                return self.anOtherMethod(nums1[l1:],nums2,k-l1)
            else:
                return self.anOtherMethod([],nums2,k-l1)
        else:
            if len(nums2)>l2:
                return self.anOtherMethod(nums1,nums2[l2:],k-l2)
            else:
                return self.anOtherMethod(nums1,[],k-l2)

sol=Solution()
print sol.findMedianSortedArrays([1,2], [1,2])


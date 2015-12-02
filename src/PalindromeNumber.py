__author__ = 'lenovo'
# coding=utf-8
class Solution:
    # @param {integer} x
    # @return {boolean}
    def isPalindrome(self, x):
        if x<0:
            return False
        t=str(x)
        if t==t[::-1]:
            return True
        else:
            return False

sol=Solution();
print sol.isPalindrome(-454)



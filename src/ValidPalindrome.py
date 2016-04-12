__author__ = 'xingyezhi'
# encoding: utf-8

class Solution(object):
    def isPalindrome(self, s):
        s2=[]
        for i in s:
            if unicode.isdigit(i):
                s2.append(i)
            elif unicode.isalpha(i):
                s2.append(unicode.lower(i))
        for i in range(len(s2)/2):
            if s2[i]!=s2[len(s2)-1-i]:
                return False
        else:
            return True

sol=Solution()
print sol.isPalindrome("1234")
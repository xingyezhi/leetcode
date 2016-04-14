# coding=utf-8
__author__ = 'lenovo'

class Solution(object):
    def shortestPalindrome(self, s):
        l=len(s)
        result=None
        if l&1:
            mid=l/2
            if self.Palindrome(s,mid-1,mid+1):return s
        mid=(l)/2-1
        while mid>=0:
            print mid
            if self.Palindrome(s,mid,mid+1):
                return s[len(s)-1:mid:-1]+s[mid+1:]
            elif self.Palindrome(s,mid-1,mid+1):
                return s[len(s)-1:mid:-1]+s[mid]+s[mid+1:]
            mid-=1
    def Palindrome(self,s,left,right):
        while left>=0:
           # print s[left],s[right]
            if s[left]!=s[right]:return False
            left-=1
            right+=1
        return True

    def shortestPalindrome2(self, s):
        s2=s[::-1]
        news=s+s2
        vp=[0 for i in range(len(news))]
        j,k=1,0
        while j<len(vp):
            if k<=0 or news[j]==news[k]:
                if news[j]==news[k]:
                    k+=1
                    vp[j]=k
                else:
                    vp[j]=k
                j+=1
            else:
                k=vp[k-1]
        print news
        print vp
        vp[len(news)-1]=min(len(s2),vp[len(news)-1])
        return s2[:len(s2)-vp[len(news)-1]]+s
sol=Solution()
print sol.shortestPalindrome2("aabba")
print 1+(1==1)
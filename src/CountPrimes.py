# coding=utf-8
__author__ = 'lenovo'


class Solution(object):
    def countPrimes(self, n):
        prime=[1 for i in range(n)]
        for i in range(2,len(prime)):
            if prime[i]==1:
                j=2*i
                while j<n:
                    prime[j]=0
                    j+=i
        prime[0]=prime[1]=0
        return sum(prime)

sol=Solution()
print sol.countPrimes(8)

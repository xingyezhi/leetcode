__author__ = 'lenovo'
# coding=utf-8

class Solution(object):
    def __init__(self):
        self.map={}
    def isScramble(self, s1, s2):
        if len(s1)!=len(s2):return False
        if len(s1)==1:return s1==s2
        if self.map.has_key((s1,s2)):
            return self.map[(s1,s2)]
        for i in range(1,len(s1)):
            if self.isScramble(s1[:i],s2[:i]) and self.isScramble(s1[i:],s2[i:]):
                self.map[(s1,s2)]=True
                return True
            elif self.isScramble(s1[i:],s2[:len(s1)-i]) and self.isScramble(s1[:i],s2[len(s1)-i:]):
                self.map[(s1,s2)]=True
                return True
        else:
            self.map[(s1,s2)]=False
            return False


sol=Solution()
print sol.isScramble("abcdefghijklmnopq","efghijklmnopqcadb")
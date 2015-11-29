__author__ = 'xingyezhi'
# encoding: utf-8
class Solution(object):
    def numDecodings(self, s):
        self.map={}
        self.map['']=1
        if len(s)==0:return 0
        else:return self.numDecodings2(s)

    def numDecodings2(self, s):
        if self.map.has_key(s):return self.map[s]
        id=int(s[0])
        if id<1:return 0
        if len(s)==1:return 1
        id2=int(s[:2])
        if 1<=id2<=26:
            result=self.numDecodings2(s[2:])+self.numDecodings2(s[1:])
            self.map[s]=result
            return result
        else:
            result=self.numDecodings2(s[1:])
            self.map[s]=result
            return result



sol=Solution()
print sol.numDecodings("10")
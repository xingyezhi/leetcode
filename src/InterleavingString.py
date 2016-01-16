# coding=utf-8
__author__ = 'lenovo'

class Solution(object):
    def isInter(self,s1,s2,s3,a,b,c):
        if len(s1[a:])==0:
            return s2[b:]==s3[c:]
        elif len(s2[b:])==0:
            return s1[a:]==s3[c:]
        elif len(s3[c:])==0:
            return False
        if s1[a]==s2[b]:
            x,y=a,b
            while x<len(s1) and s1[x]==s1[a]:
                x+=1
            while y<len(s2) and s2[y]==s2[b]:
                y+=1
            if s3[c]!=s1[a]:return False
            else:
                z=c
                while z<len(s3) and s3[z]==s3[c]:
                    z+=1
                m,n,l=x-a,y-b,z-c
                if l<m and l<n:
                    return False
                else:
                   if l>=m:
                       flag1=self.isInter(s1,s2,s3,x,b+(l-m),z)
                       if flag1==True:return True
                   if l>=n:
                       flag1=self.isInter(s1,s2,s3,a+(l-n),y,z)
                       if flag1==True:return True
                   return False
        elif s1[a]==s3[c]:
            return self.isInter(s1,s2,s3,a+1,b,c+1)
        elif s2[b]==s3[c]:
            return self.isInter(s1,s2,s3,a,b+1,c+1)
        else:
            return False

    def isInterleave(self, s1, s2, s3):
        return self.isInter(s1,s2,s3,0,0,0)
        # i=j=k=0
        # while k<len(s3):
        #     if len(s1)==0:
        #         return s2[j:]==s3[k:]
        #     elif len(s2)==0:
        #         return s1[i:]==s3[k:]
        #     if s1[i]==s2[j]:
        #         x,y=i,j
        #         while s1[x]==s1[i]:
        #             x+=1
        #         while s2[y]==s2[j]:
        #             y+=1
        #         m,n=x-i,y-j

# a="abcd"
# print len(a[3:])
sol=Solution()
# print sol.isInterleave("aabcc","dbbca","aadbbbaccc")
print sol.isInterleave("bbbbbabbbbabaababaaaabbababbaaabbabbaaabaaaaababbbababbbbbabbbbababbabaabababbbaabababababbbaaababaa",
"babaaaabbababbbabbbbaabaabbaabbbbaabaaabaababaaaabaaabbaaabaaaabaabaabbbbbbbbbbbabaaabbababbabbabaab",
"babbbabbbaaabbababbbbababaabbabaabaaabbbbabbbaaabbbaaaaabbbbaabbaaabababbaaaaaabababbababaababbababbbababbbbaaaabaabbabbaaaaabbabbaaaabbbaabaaabaababaababbaaabbbbbabbbbaabbabaabbbbabaaabbababbabbabbab")

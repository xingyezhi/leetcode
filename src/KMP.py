# coding=utf-8
__author__ = 'lenovo'

class KMP(object):
        def maketxt(self,s):
            m=len(s)
            next=[0 for i in range(m)]
            next[0]=0
            k=0
            for q in range(1,m):
                while k>0 and s[q]!=s[k]:
                    k=next[k-1]
                if s[q]==s[k]:
                    k+=1
                next[q]=k
            return next
        def next(self, s):
            news=s
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
            return vp
        def compare(self,source,s):
            print source
            next=self.maketxt(source)
            print next
            next=self.next(source)
            print next
            i=j=0
            while j<len(s):
                if i==0 or source[i]==s[j]:
                    if source[i]==s[j]:
                        i+=1
                    j+=1
                else:
                    i=next[i-1]
                if i==len(source):
                    return j-i
            return -1

sol=KMP()
print sol.compare("ababcaabc","ababcaabc")
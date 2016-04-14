__author__ = 'xingyezhi'
# encoding: utf-8

class Solution(object):
    def bfs(self,wordList,beginWord,endWord):
        from collections import deque
        q=deque([beginWord,-1])
        result=1
        visit={}
        visit[beginWord]=True
        while len(q)!=0:
            s=q.popleft()
            if s==-1:
                if len(q)!=0:
                    result+=1
                    q.append(-1)
                    continue
                else:
                    break
            for i in range(len(s)):
                s1=list(s)
                for j in "abcdefghijklmnopqrstuvwxyz":
                    s1[i]=j
                    s2=''.join(s1)
                    if s2==endWord:
                        return result+1
                    if (s2 in wordList) and (not visit.has_key(s2)):
                        visit[s2]=True
                        q.append(s2)
        return 0
    def ladderLength(self, beginWord, endWord, wordList):
        wordList.add(beginWord)
        wordList.add(endWord)
        return self.bfs(wordList,beginWord,endWord)
sol=Solution()

a="ab"
b="bc"
print set(a+b)
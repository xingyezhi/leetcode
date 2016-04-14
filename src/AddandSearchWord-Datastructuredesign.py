# coding=utf-8
__author__ = 'lenovo'
class TrieNode(object):
    def __init__(self):
        self.val=None
        self.chirld=[None for i in range(26)]
        self.leaf=False
class WordDictionary(object):
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        cur=self.root
        for i in word:
            index=ord(i)-97
            if cur.chirld[index]==None:
                newchirld=TrieNode()
                newchirld.val=i
                cur.chirld[index]=newchirld
            cur=cur.chirld[index]
            cur.leaf=True

    def search(self, word):
        return self.dfs(self.root,word,0)
    def dfs(self,cur,word,index):
        if index==len(word):return cur.leaf
        if word[index]!='.':
            cindex=ord(word[index])-97
            if cur.chirld[cindex]==None:return False
            return self.dfs(cur.chirld[cindex],word,index+1)
        else:
            for i in range(26):
                if cur.chirld[i]!=None and self.dfs(cur.chirld[i],word,index+1):
                    return True
            return False


# Your WordDictionary object will be instantiated and called as such:
wordDictionary = WordDictionary()
wordDictionary.addWord("word")
print wordDictionary.search("word")
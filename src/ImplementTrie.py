# coding=utf-8
__author__ = 'lenovo'




class TrieNode(object):
    def __init__(self):
        self.val=None
        self.leaf=False
        self.chirld=[None for i in range(26)]


class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
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
        cur=self.root
        for i in word:
            index=ord(i)-97
            if cur.chirld[index]==None:return False
            cur=cur.chirld[index]
        return cur.leaf


    def startsWith(self, prefix):
        cur=self.root
        for i in prefix:
            index=ord(i)-97
            if cur.chirld[index]==None:return False
            cur=cur.chirld[index]
        return True

# Your Trie object will be instantiated and called as such:
trie = Trie()
trie.insert("somestring")
print trie.startsWith("somes")

print ord('a')
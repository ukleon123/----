import sys

class Node:
    def __init__(self, key, val = None):
        self.key = key
        self.val = val
        self.child = {}

class Trie:
    def __init__(self):
        self.root = Node(None)
    def insert(self, string):
        current = self.root
        for i in string:
            try:
                current = current.child[i]
            except:
                current.child[i] = Node(i)
                current = current.child[i]
        current.val = string
    def numDel(self, string):
        result = 0
        current = self.root
        for i in string:
            try:
                current = current.child[i]
            except:
                pass
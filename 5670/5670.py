import sys

class Node:
    def __init__(self, key, val = None):
        self.key = key
        self.val = val
        self.child = {}

class Trie:
    def __init__(self):
        self.root = Node(None)
    def insert(self, string : str):
        current = self.root
        for i in string:
            try:
                current = current.child[i]
            except:
                current.child[i] = Node(i)
                current = current.child[i]
        current.val = string
    def search(self, string : str) -> int:
        result = 1
        current = self.root
        for i in string:
            try:
                if current == self.root:
                    result = 1
                elif len(current.child) > 1:
                    result += 1
                elif current.val is not None:
                    result += 1
                current = current.child[i]
            except:
                return -1
        return result

if __name__ == "__main__":
    
    while True:
        try:
            result = 0
            cache = []
            trie = Trie()
            N = int(sys.stdin.readline())
            
            for i in range(N):
                string = sys.stdin.readline()[:-1]
                trie.insert(string)
                cache.append(string)

            for i in cache:
                result += trie.search(i)

            print("{:.2f}".format(round(result / N, 2)))
        except:
            break


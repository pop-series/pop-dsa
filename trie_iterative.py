class Node:
    def __init__(self, leaf=False):
        self.children = [None]*26
        self.leaf = leaf

_char_idx = lambda ch: ord(ch)-97

def insert(root, word):
    word = word.lower()
    for wchar in word:
        child = root.children[_char_idx(wchar)]
        if not child:
            child = Node()
            root.children[_char_idx(wchar)] = child
        root = child
    child.leaf = True

def search(root, query):
    query = query.lower()
    for qchar in query:
        child = root.children[_char_idx(qchar)]
        if not child:
            return False
        root = child
    return root.leaf


if __name__ == '__main__':
    troot = Node()
    for word in ["and", "ant", "do", "gEek", "dad", "ball", "monkey"]:
        print('insert', word)
        insert(troot, word)
    for query in ["do", "geek", "bat", "monk"]:
        print('search', query, search(troot, query))

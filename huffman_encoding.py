
'''from heapq import *

class Node:
    def __init__(self,val=0,char=""):
        self.val=val
        self.char=char
        self.left=None
        self.right=None

    def __lt__(self,other):
        return self.val<other.val

class HuffmanTree:
    def encoding(self,arr): # arr=[(val,char)]
        n=len(arr)
        nodes=[Node(arr[i][0],arr[i][1])for i in range(n)]
        heapify(nodes)
        while(len(nodes)>1):
            x=heappop(nodes)
            y=heappop(nodes)
            curr=Node(x.val+y.val)
            curr.left=x
            curr.right=y
            heappush(nodes,curr)
        return nodes[0]
    def dfs(self,root,prefix):
        if not root.left and not root.right:
            print(root.char,root.val,prefix)
            return
        if root.left:
            self.dfs(root.left,prefix+"0")
        if root.right:
            self.dfs(root.right,prefix+"1")
    def decoding(self,root):
        self.dfs(root,"")
h=HuffmanTree()
root=h.encoding([
    (21,"A"),(1,"B"),(3,"C"),(3,"D"),(6,"E"),(8,"F")
])
h.decoding(root)'''


from heapq import *

class Node:
    def __init__(self,val=0,char=""):
        self.val=val
        self.char=char
        self.left=None
        self.right=None
    def __lt__(self, other):
        if self.val<other.val:
            return self.val
        else:
            return other.val

class Huffman:
    def encoding(self,arr):# arr=[(val),(char)]
        n=len(arr)
        nodes=[Node(arr[i][0],arr[i][1])for i in range(n)]
        heapify(nodes)

        while(len(nodes)>1):
            x=heappop(nodes)
            y=heappop(nodes)
            curr=Node(x.val+y.val)
            curr.left=x
            curr.right=y
            heappush(nodes,curr)
        return nodes[0]
    def dfs(self,root,prefix):
        if not root.left and not root.right:
            print(root.val,root.char,prefix)
        if root.left:
            self.dfs(root.left,prefix+"0")
        if root.right:
            self.dfs(root.right,prefix+"1")

    def decoding(self,root):
        self.dfs(root,"")

h=Huffman()

root=h.encoding(
    [(21,"A"),(1,"B"),(3,"C"),(4,"D")]
)
h.decoding(root)




























class TreeNode:
    def __init__(self, key, val, left=None, right=None, parent=None):
        self.key=key
        self.payload=val
        self.leftChild=left
        self.rightChild=right
        self.parent=parent
    
    def hasLeftChild(self):
        return self.leftChild
    
    def hasRightChild(self):
        return self.rightChild
    
    def hasAnyChild(self):
        return self.rightChild or self.leftChild
    
    def hasBothChild(self):
        return self.rightChild and self.leftChild
    
    def isLeftChild(self):
        return self.parent and self.parent.leftChild
    
    def isRightChild(self):
        return self.parent and self.parent.rightChild
    
    def isRoot(self):
        return not self.parent
    
    def isLeaf(self):
        return not (self.rightChild or self.leftChild)

    def __str__(self):
        return "key: " + self.key + " val: " + str(self.payload) + " has left: " + ("true" if self.hasLeftChild() else "false")+ " has right: " + ("true" if self.hasRightChild() else "false")
    
    def findMin(self):
        current = self
        while current.hasLeftChild():
            current = current.leftChild
        return current
    
    def findMax(self):
        current = self
        while current.hasRightChild():
            current = current.rightChild
        return current    

class BinarySearchTree:
    def __init__(self):
        self.root=None
        self.size=0
    
    def lenght(self):
        return self.size
    
    def __len__(self):
        return self.size
    
    def _put(self, key, val, node):
        if val < node.payload:
            if node.hasLeftChild():
                self._put(key, val, node.leftChild)
            else:
                node.leftChild = TreeNode(key, val, None, None, node)
                return node.leftChild
        if val > node.payload:
            if node.hasRightChild():
                self._put(key, val, node.rightChild)
            else:
                node.rightChild = TreeNode(key, val, None, None, node)
                return node.rightChild
                
    def append(self, value=None):
        if not self.root:
            self.root=TreeNode("key"+str(value), value)
        else:
            self._put("key"+str(value), value, self.root)
        self.size += 1

    def clean(self):
        self.root=None
        self.size=0

    def _stampa(self, node):
        print(node)
        if node.hasLeftChild():
            self._stampa(node.hasLeftChild())
        if node.hasRightChild():
            self._stampa(node.hasRightChild())
        return ""

    def __str__(self):
        return self._stampa(self.root)

    def getMin(self):
        current = self.root
        while current.hasLeftChild():
            current = current.leftChild
        return current
    
    def getMax(self):
        current = self.root
        while current.hasRightChild():
            current = current.rightChild
        return current

    def getClassName(self):
        return "BinarySearchTree"
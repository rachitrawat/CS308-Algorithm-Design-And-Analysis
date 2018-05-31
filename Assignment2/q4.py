class TreeNode:
    def __init__(self, key, val, left=None, right=None, parent=None):
        self.key = key
        self.val = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent

    def hasLeftChild(self):
        return self.leftChild

    def hasRightChild(self):
        return self.rightChild

    def isRoot(self):
        return not self.parent

    def isExternal(self):
        return not (self.rightChild or self.leftChild)

    def isInternal(self):
        return self.rightChild or self.leftChild

    def height(self):
        if self is None:
            return 0
        else:
            return max(self.height(self.leftChild), self.height(self.rightChild)) + 1

    def numChildren(self):
        count = 0
        if self.hasLeft is not None:
            count += 1
        if self.hasRight is not None:
            count += 1
        return count

    def replaceNodeData(self,key,value,lc,rc):
        self.key = key
        self.val = value
        self.leftChild = lc
        self.rightChild = rc
        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self


class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def size(self, root):
        left_size = 0
        right_size = 0
        if root.leftChild:
            left_size = self.size(root.leftChild)
        else:
            0
        if root.rightChild:
            right_size = self.size(root.rightChild)
        else:
            0
        return left_size + 1 + right_size

    def put(self,key,val):
        if self.root:
            self._put(key,val,self.root)
        else:
            self.root = TreeNode(key,val)
        self.size = self.size + 1

    def _put(self,key,val,currentNode):
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                   self._put(key,val,currentNode.leftChild)
            else:
                   currentNode.leftChild = TreeNode(key,val,parent=currentNode)
        else:
            if currentNode.hasRightChild():
                   self._put(key,val,currentNode.rightChild)
            else:
                   currentNode.rightChild = TreeNode(key,val)

    def isEmpty(self):
        return self.root is None

    def __setitem__(self,k,v):
       self.put(k,v)

    def get(self,key):
       if self.root:
           res = self._get(key,self.root)
           if res:
                  return res.val
           else:
                  return None
       else:
           return None

    def _get(self,key,currentNode):
       if not currentNode:
           return None
       elif currentNode.key == key:
           return currentNode
       elif key < currentNode.key:
           return self._get(key,currentNode.leftChild)
       else:
           return self._get(key,currentNode.rightChild)

    def __getitem__(self,key):
       return self.get(key)

    def __contains__(self,key):
       if self._get(key,self.root):
           return True
       else:
           return False

    def root(self):
        return self.root

    def parent(self, node):
        parent = None
        if node.leftChild != None:
            return self.maximum(node.leftChild)
        parent = node.p
        while parent != None and node == parent.leftChild:
            node = parent
            parent = parent.p
        return parent

    def addLeft(self, node):
        if self.leftChild == None:
            self.leftChild = BinarySearchTree(node)
        else:
            t = BinarySearchTree(node)
            t.leftChild = self.leftChild
            self.leftChild = t

    def addRight(self, node):
        if self.rightChild == None:
            self.rightChild = BinarySearchTree(node)
        else:
            t = BinarySearchTree(node)
            t.rightChild = self.rightChild
            self.rightChild = t

    def depth(self, node):
        if self.root is None:
            max_height = 0
        else:
            max_height = max(self.height(self.root.leftChild), self.height(self.root.rightChild)) + 1
        node_depth = max_height - node.height()
        return node_depth


mytree = BinarySearchTree()
#print(mytree.isEmpty())
mytree[3]="bus"
mytree[4]="car"
#print(mytree.size)
mytree[6]="plane"

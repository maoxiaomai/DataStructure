# -*- coding: utf-8 -*-
# Binary Search Tree

# Tree Node
class TreeNode:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.data)

class OperationTree:

    def insert(self, root, value):
        if root == None:
            root = TreeNode(value)
        else:
            if value < root.data:
                root.left = self.insert(root.left, value)
            elif value > root.data:
                root.right = self.insert(root.right, value)
        return root

    def query(self, root, value):
        if root == None:
            return False
        if root.data == value:
            return True
        elif value < root.data:
            return self.query(root.left, value)
        elif value > root.data:
            return self.query(root.right, value)

    def findMin(self, root):
        while root.left:
            return self.findMin(root.left)
        return root

    def findMax(self, root):
        while root.right:
            return self.findMax(root.right)
        return root

    def delNode(self, root, value):
        '''删除二叉搜索树中值为val的点'''
        if root == None:
            print("The node doesn't exist.")
            return
        if value < root.data:
            root.left = self.delNode(root.left, value)
        elif value > root.data:
            root.right = self.delNode(root.right, value)
        else:
        # 分为三种情况
            if root.left and root.right:
                # 找到右子树的最小值结点
                right_min = self.findMin(root.right)
                root.data = right_min.data  # 把最小值赋给要删掉的结点
                # 把右子树中最小结点删除
                root.right = self.delNode(root.right, right_min.data)

            elif root.left == None and root.right == None:
                root = None
            elif root.left == None:
                root = root.right
            elif root.right == None:
                root = root.left
        return root


    def printTree(self, root):
        # 打印BST，中序打印
        if root == None:
            return
        self.printTree(root.left)
        print(root.data, end=' ')
        self.printTree(root.right)




if __name__ == '__main__':
    List = [17, 5, 35, 2, 11, 29, 38, 9, 16, 8]
    root = None
    op = OperationTree()
    for var in List:
        root = op.insert(root, var)
    op.printTree(root)
    print('')
    print('查询树中值为11的节点:', op.query(root, 11))
    print('查询树中值为11的节点:', op.query(root, 100))
    print('树中最小值为:', op.findMin(root).data)
    print('树中最大值为:', op.findMax(root).data)
    print('删除树中值为16的节点:', end=' ')
    root = op.delNode(root, 16)
    op.printTree(root)
    print('')
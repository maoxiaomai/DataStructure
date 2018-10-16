# -*- coding: utf-8-*- #
# define class of Node

class Node:
    '''
    data: the info that node saved
    _next: save the next node object
    '''
    def __init__(self, data, pnext=None):
        self.data = data
        self._next = pnext

    def __repr__(self):
        '''
        用来定义Node的字符输出
        print为输出data
        '''
        return str(self.data)

class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def is_empty(self):
        '''
        判断该链表是否为空
        :return: boolean
        '''
        return self.length == 0

    def append(self, this_node):
        '''
        在链表末添加node/值,如果是node对象直接添加，否则先转换为node对象
        :param this_node: 数据或node对象
        :return: None
        '''
        if isinstance(this_node, Node):
            pass
        else:
            this_node = Node(data=this_node)
        if self.is_empty():
            # 链表为空的情况，将头指针指向当前Node
            self.head = this_node
        else:
            current_node = self.head
            while current_node._next: # 找到最后一个结点（最后一个结点不指向任何结点，为空）
                current_node = current_node._next
            current_node._next = this_node  # 将最后一个结点指向新的结点
        self.length += 1

    def insert(self, value, index):
        '''
        链表的插入操作
        :param value: 要插入的值
        :param index: 位置
        :return: None
        '''
        if type(index) is int:
            if index > self.length:
                # 索引值超出范围，退出
                print("Index value is out of range.")
                return
            else:
                # 获得当前node对象和head
                this_node = Node(data=value) # 要插入的node，用this_node指向
                current_node = self.head
                # 当插入位置为0
                if index == 0:
                    self.head = this_node
                    this_node._next = current_node
                    return

                # 先找到第index-1个节点，用current_node指向
                while index - 1:
                    current_node = current_node._next
                    index -= 1

                # 这两条语句顺序很关键
                # 将当前节点与后一个节点拆开，this_node指向后一个节点，前一个节点指向this_node
                this_node._next = current_node._next
                current_node._next = this_node
                self.length += 1
        else:
            print("The index value is not int.")
            return

    def delete(self, index):
        '''
        删除链表中某个index位置的节点
        :param index: 位置索引
        :return: None
        '''
        if type(index) is int:
            if index < 0 or index >= self.length:
                # 索引值超出范围直接提示并且退出
                print("Index out of range.")
                return
            else:
                current_node = self.head
                if index == 0:
                    self.head = current_node._next
                    del current_node
                else:
                    # (1) 先找到链表的第index-1个node，用current_node指向
                    j = 1
                    while True:
                        current_node = current_node._next
                        j += 1
                        if index == j:
                            break

                    del_node = current_node._next  # (2) 用指针del_node指向要被删除的结点（即current_node的下一个node）
                    current_node._next = del_node._next  # (3) 修改指针，将current_node指向的下一个结点改为del_node的下一个结点
                    del del_node  # (4) 释放del_node所指向的空间

                self.length -= 1
                return

        else:
            print("Index is not int.")
            return
    def update(self, index, value):
        '''
        为链表中某个位置的节点修改值
        :param index: 位置索引
        :param value: 要修改的值
        :return: None
        '''
        if type(index) is int:
            if self.is_empty():
                print("Error: List is empty")
                return
            elif index < 0 or index >= self.length:
                print("Index value is out of range.")
                return
            else:
                #
                new_node = Node(data=value)
                current_node = self.head
                if index == 0:
                    new_node._next = current_node._next
                    self.head = new_node
                else:
                    j = 1
                    while True:
                        current_node = current_node._next
                        j += 1
                        if j == index:
                            break
                    new_node._next = current_node._next._next
                    current_node._next = new_node
                    del current_node._next
                    return
        else:
            print("Index is not int.")
            return

    def get_value(self, index):
        '''
        获取链表中某个位置节点的值
        :param index:
        :return: 该结点的值
        '''
        if type(index) is int:
            if self.is_empty() or index < 0 or index >= self.length:
                print("Index value is out of range.")
                return
            else:
                current_node = self.head
                if index == 0:
                    return current_node.data
                else:
                    j = 0
                    while current_node._next and j < index:
                        current_node = current_node._next
                        j += 1
                    return current_node.data
        else:
            print("Index is not int.")
            return

    def get_index(self, value):
        '''
        查找value第一次出现的位置
        :param value:
        :return:
        '''
        j = 0
        if self.is_empty():
            print("The list is empty.")
            return

        current_node = self.head
        while current_node:
            if str(current_node.data) == value:
                return j
            current_node = current_node._next
            j += 1
        if j == self.length:
            print("The value %s doesn't exit." %value)
            return



    def __repr__(self):
        if self.is_empty():
            return "Empty linked list"
        node = self.head
        node_list = ''
        while node:
            node_list += str(node.data) + ' '
            node = node._next
        return node_list


if __name__ == '__main__':
    node1 = Node(data='NODE1')
    node2 = Node(data='NODE2')
    linked_list = LinkedList()
    # linked_list.append(node1)
    print(linked_list.length)
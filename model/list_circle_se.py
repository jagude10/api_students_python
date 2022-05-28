from .node import Node

class ListSEC:
    def __init__(self):
        self.head = None
        self.last = None

    def empty(self):
        return self.head == None

    def addtostart(self,data):
        if self.empty():
            self.head = self.last = Node(data)
            self.last.next = self.head
        else:
            temp = Node(data)
            temp.next = self.head
            self.head = temp
            self.last.next = self.head
        self.count = +1
    def addtoend(self,data):
        if self.empty():
            self.head = self.last = Node(data)
            self.last.next = self.head
        else:
            temp = self.last
            self.last = temp.next = Node(data)
            self.last.next = self.head
        self.count = +1
    def tour(self):
        temp = self.head
        while temp.next != self.head:
            temp.data = temp.next



class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head=None

    def insert_end(self, data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            return self.head


        self.head.next=self.insert_end(data)
        self.head=self.head.next
        
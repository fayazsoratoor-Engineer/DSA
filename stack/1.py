class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("pop from empty stack")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("peek from empty stack")

    def size(self):
        return len(self.items)

    def display(self):
        return self.items

    def count(self, item):
        return self.items.count(item)
    def index(self, item):
        if item in self.items:
            return self.items.index(item)
        else:
            raise ValueError(f"{item} is not in stack")


    def reverse(self):
        return self.items.reverse()

    def clear(self):
        self.items.clear()
s1=Stack()
s1.push(1)
s1.push(2)
s1.push(3)
print(s1.display())
s1.pop()
print(s1.display())



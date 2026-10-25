from collections import deque

class Queue:
    def __init__(self):
        self.items = deque()

    def enqueue(self, value):
        self.items.append(value)

    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        return self.items.popleft()

    def peek(self):
        if self.is_empty():
            return "Queue is empty"
        return self.items[0]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def display(self):
        print(list(self.items))

    def clear(self):
        self.items.clear()


q = Queue()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

q.display()
print("Front:", q.peek())
print("Removed:", q.dequeue())
print("Size:", q.size())
q.display()
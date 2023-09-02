class Item:
    def __init__(self, value):
        self.value = value,
        self.next = None

class Stack:
    def __init__(self, head):
        self.head = head

    def push(self, value):
        value.next = self.head
        self.head = value   

    def pop(self):
        self.head = self.head.next

    def top(self):
        return self.head
    
a1 = Item(1)
a2 = Item(2)
a3 = Item(3)
a4 = Item(4)

myStack = Stack(a1)
myStack.push(a2)
myStack.push(a3)
myStack.push(a4)

print(myStack.top().value)

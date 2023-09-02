import math


class node():
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList():
    def __init__(self, head):
        self.head = head

    def append(self, newElement):
        currentNode = self.head
        while True:
            if currentNode.next == None:
                currentNode.next = newElement
                return
            else:
                currentNode = currentNode.next

    def insert(self, newElement, position):
        currentNode = self.head
        count = 1
        while True:
            if count == position:
                newElement.next = currentNode.next
                currentNode.next = newElement
                return
            else:
                currentNode = currentNode.next
                count += 1

    def getPosition(self, position):
        currentNode = self.head
        count = 1

        while True:
            if currentNode.next == None:
                return node(-1)
            if count == position:
                return currentNode
            else:
                currentNode = currentNode.next
                count += 1

    def delete(self, value):
        if self.head.value == value:
            self.head = self.head.next
            return
        
        currentNode = self.head
        while currentNode.next != None:
           if currentNode.next.value == value:
               currentNode.next = currentNode.next.next
               return currentNode
           else:
               currentNode = currentNode.next

    def getCountRec(self, node):
        if not node:  # Base case
            return 0
        else:
            return 1 + self.getCountRec(node.next)
    
    def lenght(self):
        return self.getCountRec(self.head)
    
    def getMiddle(self):
        middle = math.ceil((self.lenght()/2))
        return self.getPosition(middle)
    
    def getMiddle2(self):
        step1 = self.head
        step2 = self.head

        while True:
            if step2.next == None:
                return step1
            else:
                step1 = step1.next
                step2 = step2.next.next

    def ocurrences(self, key):
        currentNode = self.head
        count = 0
        while(currentNode is not None):
            if key == currentNode.value:
                count += 1
            currentNode = currentNode.next
        return count
        
            

n1 = node(1)
n2 = node(2)
n3 = node(3)
n4 = node(4)
n5 = node(3)
n6 = node(6)
n7 = node(3)


linked = LinkedList(n1)
linked.append(n2)
linked.append(n3)
linked.append(n4)
linked.append(n5)
linked.append(n6)
linked.append(n7)

#print(linked.getMiddle().value)
#print(linked.getMiddle2().value)
print(linked.ocurrences(3))

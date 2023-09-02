
class Queue:
    def __init__(self, head):
        self.fila = [head]

    def dequeue(self):
        self.fila.__delitem__(0)

    def enqueue(self, value):
        self.fila.append(value)

BuyBread = Queue("kahilo")
BuyBread.enqueue("ana")
BuyBread.enqueue("cristina")
BuyBread.enqueue("lídia")
print(BuyBread.fila)
BuyBread.dequeue()
BuyBread.dequeue()
print(BuyBread.fila)
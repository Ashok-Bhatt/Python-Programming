class deque:

    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items == []
    
    def count(self):
        return len(self.items)
    
    def addFront(self, data):
        self.items.insert(0,data)

    def addRear(self, data):
        self.items.append(data)

    def removeFront(self):
        self.items.pop(0)

    def removeRear(self):
        self.items.pop()

d = deque()

d.addRear(3)
d.addFront(2)
print(d.count())
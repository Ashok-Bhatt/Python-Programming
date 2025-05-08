import array as arr
class queue:
    def __init__(self):
        self.queue = arr.array("i",[])

    def ENQUE(self,element):
        self.queue.append(element)

    def DEQUE(self):
        if not self.is_empty():
            self.queue.pop()
        else:
            print("Queue is empty")

    def DISPLAY(self):
        if not self.is_empty():
            print("QUEUE: ", end="")
            for element in reversed(self.queue):
                print(element, end=" ")
            print()
        else:
            print("Queue is empty")
    def is_empty(self):
        return len(self.queue) == 0
    
q = queue()
while True:
    print("\nEnter the number as per your requirement:")
    print("1.enqueue    2.dequeue   3.display    4.Is queue empty?")
    
    choice = int(input("Enter your choice:"))
    if choice==1:
        element = int(input("Enter the element:"))
        q.ENQUE(element)
    elif choice==2:
        q.DEQUE()
    elif choice==3:
        q.DISPLAY()
    elif choice==4:
        print(q.is_empty())
    else:
      break
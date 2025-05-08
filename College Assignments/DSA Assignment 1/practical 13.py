class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
 
 
class Stack:

    def __init__(self):
        self.head = None
 
    def isempty(self):
        if self.head == None:
            return True
        else:
            return False
 
    def push(self, data):
        if self.head == None:
            self.head = Node(data)
        else:
            newnode = Node(data)
            newnode.next = self.head
            self.head = newnode

    def pop(self):
        if self.isempty():
            return None
        else:
            poppednode = self.head
            self.head = self.head.next
            poppednode.next = None
            return poppednode.data

    def peek(self):
        if self.isempty():
            return None
        else:
            return self.head.data

    def display(self):
        iternode = self.head
        if self.isempty():
            print("Stack Underflow")
        else:
            print("Current element:",end="  ")
            while(iternode != None):
                print(iternode.data, end = "  ")
                iternode = iternode.next
                # if(iternode != None):
                #     print(" -> ", end = "")
            return

MyStack = Stack()

while True:
    print("\n\nEnter the number as per your requirement:")
    print("1.Push element    2.Pop element    3.Display Peek    4.Is stack empty?    5.Display all elements of the stack")
    
    choice = int(input("Enter your choice:"))
    if choice==1:
        element = int(input("Enter the element:"))
        MyStack.push(element)
    elif choice==2:
        print("Popped Element:",MyStack.pop())
    elif choice==3:
        print("Top Element:",MyStack.peek())
    elif choice==4:
        print("Is Stack Empty:",MyStack.isempty())
    elif choice==5:
        MyStack.display()
    else:
        break
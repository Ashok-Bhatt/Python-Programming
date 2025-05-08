import array as arr

class Stack:
    def __init__(self):
        self.stack = arr.array("i",[])

    def push(self, element):
        self.stack.append(element)
        print(f"{element} pushed to stack")

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            print("Stack is empty")

    def peep(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            print("Stack is empty")

    def change(self, index, element):
        if index >= len(self.stack):
            print("Index out of range")
        else:
            self.stack[index] = element
            print(f"Element at index {index} changed to {element}")

    def display(self):
        if not self.is_empty():
            print("Stack: ", end="")
            for element in reversed(self.stack):
                print(element, end=" ")
            print()
        else:
            print("Stack is empty")

    def is_empty(self):
        return len(self.stack) == 0
    
s = Stack()
while True:
    print("\nEnter the number as per your requirement:")
    print("1.push    2.pop    3.peep    4.change    5.display")
    
    choice = int(input("\nEnter your choice:"))
    if choice==1:
        element = int(input("Enter the element:"))
        s.push(element)
    elif choice==2:
        s.pop()
    elif choice==3:
        print("Top element:",s.peep())
    elif choice==4:
        element = int(input("Enter the element:"))
        index = int(input("Enter the index:"))
        s.change(element,index)
    elif choice==5:
        s.display()
    else:
      break
class Node:
  def __init__(self,data = None, next = None,prev = None):
    self.data = data
    self.next = next
    self.prev = prev

class ddlinkedlist:
  def __init__(self):
    self.head = None

  def print_forward(self):
    if self.head is None:
      print("Linked list is empty")
      return
    liststr = []
    itr = self.head
    while itr:
      liststr.append(itr.data)
      itr = itr.next
    print(liststr)

  def insert_at_beg(self,data):
    node = Node(data,self.head,None)
    if self.head is None:
      self.head = node
    else:
      self.head.prev = node
      self.head = node

  def insert_at_end(self,data):
   if self.head is None:
     node = Node(data,None,None)
     self.head = node
     return
   itr = self.head
   while itr.next:
     itr = itr.next
   node = Node(data,None,itr)
   itr.next = node

  def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

  def get_length(self):
    count = 0
    itr = self.head
    while itr:
      count+=1
      itr = itr.next
    return count

  def remove_at(self,index):
    if self.get_length() == 0:
      self.head = self.head.next
      self.head.prev = None
      return

    if index<0 or index >= self.get_length():
      raise Exception("Invalid index")


    count = 0
    itr = self.head
    while itr:
      if count == index:
        itr.prev.next = itr.next
        if itr.next:
          itr.next.prev = itr.prev
        break
      itr = itr.next
      count+=1

  def remove_at_end(self):
    if self.get_length() == 0:
      self.head = self.head.next
      self.head.prev = None
      return
    
    count = 0
    itr = self.head
    while itr:
      if count == self.get_length()-1:
        itr.prev.next = itr.next
        if itr.next:
          itr.next.prev = itr.prev
        break
      itr = itr.next
      count+=1

d=ddlinkedlist()

d.insert_values([1,2,3,4,5])
print("Current Elements:",end=" ")
d.print_forward()

while True:
    print("\nEnter the number as per your requirement:")
    print("1.Insert node at front    2.Insert node at end    3.Delete last node    4.Delete node at specified position")
    
    choice = int(input("\nEnter your choice:"))
    if choice==1:
        element = int(input("Enter the element:"))
        d.insert_at_beg(element)
    elif choice==2:
        element = int(input("Enter the element:"))
        d.insert_at_end(element)
    elif choice==3:
        d.remove_at_end()
    elif choice==4:
        index = int(input("Enter the index:"))
        d.remove_at(index)
    else:
      break
    print("\tCurrent Elements:",end="")
    d.print_forward()
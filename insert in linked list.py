class Node:
    def __init__(self, data):
        self.data = data
        self.next  = None
class linkedlist:
    def __init__(self):
        self.head = None
    def insertnode(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node

    def insertatindex(self,data,index):
        if (index == 0):
            self.insertnode(data)
            return

        position = 0
        current_node = self.head
        while (current_node != None and position+1 !=  index):
            position = position + 1
            current_node = current_node.next

        if current_node != None:
            new_node = Node(data)
            new_node.next  = current_node.next
            current_node.next = new_node
        else:
            print("index not present")

    def insertatend(self, data):
         new_node = Node(data)
         if self.head is None:
             self.head = new_node
             return
         current_node = self.head
         while(current_node.next):
             current_node = current_node.next

         current_node.next = new_node    

    def printll(self):
        current_node = self.head
        while (current_node != None):
            print(current_node.data)
            current_node = current_node.next

a= linkedlist()
a.insertnode("yakshi")
a.insertatindex("panwar",1)
a.insertatend("8722171")
a.printll()
            
            
            
        

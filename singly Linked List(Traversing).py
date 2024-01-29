#Defines the structure of the node in which is has a data and also the address to the next node
class Node :
    def __init__(self,data=None):
        self.data = data
        self.next = None


#created a class Linkedlist in which we have head as none as initially the head is none
class LinkedList:
    def __init__(self):
        self.head = None

#To print the elements in the linked list we used the n.data and n.next
    def print(self):
        if self.head is None:
            print("Linkedlist is empty")

        else:
            n = self.head
            while n is not None:
                print(n.data)
                n = n.next

#creating an object of the class to print the Linked List elements 
LL = LinkedList()
LL.print()







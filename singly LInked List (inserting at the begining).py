class Node:
    def __init__(self,data=None):
        self.data = data
        self.next = None





class LinkedList:
    def __init__(self):
        self.head = None

    def print(self):
        if self.head is None:
            print("linkedlist is empty")

        else:
            n = self.head
            while n is not None:
                print(n.data)
                n = n.next

    #creates a new node with node class and assigns the data into it after that the
    #head of the current node is assigned to the reference(next) of the new node then
    # the new node is set as the head.
    def addbegin(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node


LL = LinkedList()
LL.addbegin(30)
LL.addbegin(20)
LL.addbegin(10)
LL.print()



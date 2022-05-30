class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DLL:
    def __init__(self):
        self.head = None
    
    def insertAtBeginning(self, data):
        node = Node(data)
        if(self.head == None):
            self.head = node
            self.head.next = None
            self.head.prev = None
        else:
            temp = self.head
            node.next = temp
            node.prev = None
            temp.prev = node
            self.head = node
    
    def insertAtEnd(self, data):
        node = Node(data)
        if(self.head == None):
            self.head = node
            self.head.next = self.head
            self.head.prev = None
        else:
            temp = self.head
            while(temp.next is not None):
                temp = temp.next
            temp.next = node
            node.next = None
            node.prev = temp
    
    def deleteBeginning(self):
        temp = self.head.next
        temp.prev = None
        self.head = temp

    def deleteEnd(self):
        cur = self.head
        while(cur.next is not None):
            cur = cur.next
        cur.prev.next = None
    
    def printLinkedList(self):
        cur = self.head
        while(cur is not None):
            print(cur.data)
            cur = cur.next
    
    def reverseLinkedList(self):
        prev = None
        cur = self.head

        while(cur is not None):
            temp = cur.next
            cur.next = cur.prev
            cur.prev = temp
            prev = cur
            cur = temp
        self.head = prev


if(__name__ == '__main__'):
    dll = DLL()
    dll.insertAtBeginning(1)
    dll.insertAtBeginning(2)
    dll.insertAtBeginning(3)
    dll.printLinkedList()
    print("")
    dll.insertAtEnd(5)
    dll.insertAtEnd(8)
    dll.insertAtEnd(9)
    dll.printLinkedList()
    print("")
    dll.reverseLinkedList()
    dll.printLinkedList()
    print("")
    dll.deleteBeginning()
    dll.printLinkedList()
    print("")
    dll.deleteEnd()
    dll.printLinkedList()
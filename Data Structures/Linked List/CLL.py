class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CLL:
    def __init__(self):
        self.head = None
        self.tail = None

    
    def insertAtBeginning(self, data):
        node = Node(data)
        if(self.head == None):
            self.head = node
            self.head.next = self.head
            self.tail = self.head
        else:
            temp = self.head
            node.next = temp
            self.head = node
            self.tail.next = self.head
    
    def insertAtEnd(self, data):
        node = Node(data)
        if(self.head == None):
            self.head = node
            self.head.next = self.head
            self.tail.next = self.head
        else:
            temp = self.head
            while(temp.next is not self.head):
                temp = temp.next
            temp.next = node
            node.next = self.head
            self.tail = node
    
    def deleteBeginning(self):
        temp = self.head.next
        self.head = temp
        self.tail.next = self.head

    def deleteEnd(self):
        prev = None
        cur = self.head
        while(cur.next is not self.head):
            prev = cur
            cur = cur.next
        self.tail = prev
        prev.next = self.head
    
    def printLinkedList(self):
        cur = self.head
        while(cur.next is not self.head):
            print(cur.data)
            cur = cur.next
        print(cur.data)
        print(cur.next.data)
    
    def reverseLinkedList(self):
        prev = None
        cur = self.head
        self.tail = self.head

        while(cur.next is not self.head):
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp

        cur.next = prev
        prev = cur
        self.head = prev
        self.tail.next = self.head        


if(__name__ == '__main__'):
    cll = CLL()
    cll.insertAtBeginning(1)
    cll.insertAtBeginning(2)
    cll.insertAtBeginning(3)
    cll.printLinkedList()
    print("")
    cll.insertAtEnd(5)
    cll.insertAtEnd(8)
    cll.insertAtEnd(9)
    cll.printLinkedList()
    print("")
    cll.reverseLinkedList()
    cll.printLinkedList()
    print("")
    cll.deleteBeginning()
    cll.printLinkedList()
    print("")
    cll.deleteEnd()
    cll.printLinkedList()
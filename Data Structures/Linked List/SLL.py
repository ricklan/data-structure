class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SLL:
    def __init__(self):
        self.head = None
    

    def insertAtBeginning(self, data):
        node = Node(data)
        if(self.head == None):
            self.head = node
            self.head.next = None
        else:
            head = self.head
            node.next = head
            self.head = node
    
    def insertAtEnd(self, data):
        node = Node(data)
        if(self.head == None):
            self.head = node
            self.head.next = None
        else:
            cur = self.head
            while(cur.next is not None):
                cur = cur.next
            cur.next = node
            node.next = None
    
    def printLinkedList(self):
        cur = self.head
        while(cur is not None):
            print(cur.data, cur)
            cur = cur.next
    
    def reverseLinkList(self):
        prev = None
        cur = self.head
        while(cur is not None):
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        self.head = prev

    def deleteBeginning(self):
        nextNode = self.head.next
        self.head = nextNode

    def deleteEnd(self):
        cur = self.head
        prev = None

        while(cur.next is not None):
            prev = cur
            cur = cur.next
        
        prev.next = None

if(__name__ == '__main__'):
    sll = SLL()
    sll.insertAtBeginning(1)
    sll.insertAtBeginning(2)
    sll.insertAtBeginning(3)
    sll.insertAtEnd(5)
    sll.insertAtEnd(8)
    sll.insertAtEnd(9)
    sll.printLinkedList()
    print()
    sll.reverseLinkList()
    sll.printLinkedList()
    print()
    sll.deleteBeginning()
    sll.printLinkedList()
    print()
    sll.deleteEnd()
    sll.printLinkedList()
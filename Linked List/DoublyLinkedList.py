from Node import Node

class DLL:
    def __init__(self):
        self.head = None
    
    def insert(self, data):
        node = Node(val=data)
        if(self.head is None):
            self.head = node
            self.head.next = None
            self.head.prev = None
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = node
            node.prev = cur
    
    def printLinkedList(self):
        string = "None"
        cur = self.head
        while(cur is not None):
            string += f" <-- {cur.data} --> "
            cur = cur.next
        string += "None"
        print(string)
    
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
    dll.insert(1)
    dll.insert(2)
    dll.insert(3)
    dll.insert(5)
    dll.insert(8)
    dll.insert(9)
    dll.printLinkedList()
    print()
    dll.reverseLinkedList()
    dll.printLinkedList()

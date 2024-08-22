from Node import Node


class CLL:
    def __init__(self):
        self.head = None

    def insert(self, data):
        node = Node(data)
        if self.head == None:
            self.head = node
            self.head.next = self.head
        else:
            cur = self.head
            while cur.next is not self.head:
                cur = cur.next
            cur.next = node
            node.next = self.head

    def printLinkedList(self):
        string = "<-- "
        cur = self.head
        while cur.next is not self.head:
            string += f"{cur.data} --> "
            cur = cur.next
        string += f"{cur.data} --> "
        print(string)

    def reverseLinkedList(self):
        prev = None
        cur = self.head
        self.tail = self.head

        while cur.next is not self.head:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp

        cur.next = prev
        prev = cur
        self.head = prev
        self.tail.next = self.head


if __name__ == "__main__":
    cll = CLL()
    cll.insert(1)
    cll.insert(2)
    cll.insert(3)
    cll.insert(5)
    cll.insert(8)
    cll.insert(9)
    cll.printLinkedList()
    print()
    cll.reverseLinkedList()
    cll.printLinkedList()

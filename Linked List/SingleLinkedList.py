from Node import Node


class SLL:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(val=data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def printLinkedList(self):
        cur = self.head
        string = ""
        while cur is not None:
            string += f"{cur.data} --> "
            cur = cur.next
        string += str(None)
        print(string)

    def reverseLinkList(self):
        prev = None
        cur = self.head
        while cur is not None:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        self.head = prev


if __name__ == "__main__":
    sll = SLL()
    sll.insert(1)
    sll.insert(2)
    sll.insert(3)
    sll.insert(5)
    sll.insert(8)
    sll.insert(9)
    sll.printLinkedList()
    print()
    sll.reverseLinkList()
    sll.printLinkedList()

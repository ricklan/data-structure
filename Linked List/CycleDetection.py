from Node import Node


def cycle_detection(head: Node) -> bool:
    fast_pointer = head
    slow_pointer = head

    while fast_pointer is not None and fast_pointer.next is not None:
        fast_pointer = fast_pointer.next.next
        slow_pointer = slow_pointer.next

        if fast_pointer == slow_pointer:
            return True

    return False


if __name__ == "__main__":
    head1 = Node(0)
    head2 = Node(0)
    cur1 = head1
    cur2 = head2
    cycle_node = None
    for i in range(1, 10):
        node1 = Node(i)
        node2 = Node(i)

        if i == 5:
            cycle_node = node1

        cur1.next = node1
        cur1 = cur1.next

        cur2.next = node2
        cur2 = cur2.next

    cur1.next = cycle_node
    print(cycle_detection(head1))
    print(cycle_detection(head2))

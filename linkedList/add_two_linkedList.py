class Node(object):
    def __init__(self,value):
        self.value = value
        self.next = None


class LinkedList(object):
    def __init__(self):
        self.head = None
        self.curr = None

    def addNode(self,node):
        if self.head is None:
            self.head = self.curr = node

        else:
            self.curr.next = node
            self.curr = node

    def iterate_List(self):
        self.curr = self.head
        while self.curr is not None:
            print (self.curr.value)
            self.curr = self.curr.next

    def reverseLinkedList(self):
        newhead = None
        while self.head is not None:
            nxt = self.head.next
            self.head.next = newhead
            newhead = self.head
            self.head = nxt
        self.head = newhead


def add_two_linked_list(l1,l2,newlist):
    p = l1.head
    q = l2.head
    initial_carry = 0
    while p is not None or q is not None:
        p_value = 0
        q_value = 0
        if p is not None:
            p_value = p.value
            p = p.next

        if q is not None:
            q_value = q.value
            q = q.next

        carry_temp = initial_carry
        next_value = p_value + q_value + carry_temp
        initial_carry = next_value / 10
        remainder = next_value % 10
        newlist.addNode(Node(remainder))
    if initial_carry > 0:
        newlist.addNode(Node(initial_carry))

    newlist.reverseLinkedList()



if __name__ == '__main__':
    n1 = Node(9)
    n2 = Node(8)
    n3 = Node(4)
    n4 = Node(3)
    n5 = Node(9)
    n6 = Node(8)
    n7 = Node(4)
    n8 = Node(3)


    l1 = LinkedList()
    l1.addNode(n1)
    l1.addNode(n2)
    l1.addNode(n3)
    l1.addNode(n4)

    l2 = LinkedList()
    l2.addNode(n5)
    l2.addNode(n6)
    l2.addNode(n7)
    l2.addNode(n8)


    l3 = LinkedList()

    l1.reverseLinkedList()
    l2.reverseLinkedList()
    # l1.iterate_List()
    # l2.iterate_List()
    add_two_linked_list(l1,l2,l3)
    l3.iterate_List()

    # l2.iterate_List()
    # l2.reverseLinkedList()
    # print(' in reverse order')
    # l1.iterate_List()











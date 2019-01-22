
class Node(object):
    def __init__(self,value):
        self.value = value
        self.next = None


class LinkedList(object):
    def __init__(self):
        self.head = None
        self.count = 0
        self.curr = None

    def addNode(self,node):
        if self.head is None:
            self.head = self.curr = node

        else:
            self.curr.next = node
            self.curr = node

        self.count = self.count + 1


def find_intersetion_point( l1, l2):
    while l1.count > l2.count:
        l1.head = l1.head.next
        l1.count = l1.count - 1

    while l2.count > l1.count:
        l2.head = l2.head.next
        l2.count = l2.count - 1

    while l1.head is not None:
        print (id(l1.head.next), (l1.head.value))
        print (id(l2.head.next), (l2.head.value))
        if id(l1.head) == id(l2.head):
            print 'intersection point is' + str(l1.head.value)
            return
        l1.head = l1.head.next
        l2.head = l2.head.next

    print ('No intersection point found')




if __name__ == '__main__':
    n1 = Node(3)
    n2 = Node(4)
    n3 = Node(5)
    n4 = Node(8)
    n5 = Node(10)
    n6 = Node(6)
    n7 = Node(3)
    n8 = Node(2)
    n9 = Node(10)

    n10 = Node(40)
    n11 = Node(30)
    n12 = Node(50)

    n13 = Node(6)
    n14 = Node(3)
    n15 = Node(2)
    n16 = Node(10)

    l1 = LinkedList()
    l1.addNode(n1)
    l1.addNode(n2)
    l1.addNode(n3)
    l1.addNode(n4)
    l1.addNode(n5)
    l1.addNode(n6)
    l1.addNode(n7)
    l1.addNode(n8)
    l1.addNode(n9)

    l2 = LinkedList()

    l2.addNode(n10)
    l2.addNode(n11)
    l2.addNode(n12)
    l2.addNode(n6)
    l2.addNode(n7)
    l2.addNode(n8)
    l2.addNode(n9)
    #find_intersetion_point(l1,l2)

    l3 = LinkedList()

    l3.addNode(n10)
    l3.addNode(n11)
    l3.addNode(n12)
    l3.addNode(n13)
    l3.addNode(n14)
    l3.addNode(n15)
    l3.addNode(n16)

    find_intersetion_point(l1, l3)




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
        curr = self.head
        while self.curr is not None:
            print (self.curr.value)
            curr = curr.next

    def create_cycle_node(self,n1):
        self.curr.next = n1



def detect_cycle(l1):
    p = l1.head
    q = l1.head

    while q.next is not None:
        p = p.next
        q = q.next.next
        if q is None:
            return None

        if id(p) == id(q):
            print('cycle exists')
            return p
    return None

def starting_point_of_cycle(l1):
    starting_point = detect_cycle(l1)
    p = starting_point
    q = l1.head
    if starting_point is not None:
        while id(p) != id(q):
            p = p.next
            q = q.next
        print ('start of cycle ' + str(p.value))
        return p

    return None

def size_of_cycle(l1):
    starting_point = detect_cycle(l1)
    if starting_point is None:
        return 0
    p = starting_point
    q = starting_point.next
    count = 1
    while id(p) != id(q):
        q = q.next
        count = count + 1
    return count

def remove_cycle(l1):
    starting_point = starting_point_of_cycle(l1)
    if starting_point is None:
        return
    p = starting_point
    q = starting_point
    while id(p) != id(q.next):
        q = q.next
    q.next = None
    return


if __name__ == '__main__':
    n1 = Node(20)
    n2 = Node(4)
    n3 = Node(5)
    n4 = Node(8)
    n5 = Node(10)
    n6 = Node(6)
    n7 = Node(3)
    n8 = Node(2)
    n9 = Node(10)

    l1 = LinkedList()
    l1.addNode(n1)
    #l1.addNode(n2)
    # l1.addNode(n3)
    # l1.addNode(n4)
    # l1.addNode(n5)
    # l1.addNode(n6)
    # l1.addNode(n7)
    # l1.addNode(n8)
    # l1.addNode(n9)
    l1.create_cycle_node(n1)
    print(starting_point_of_cycle(l1))
    print (size_of_cycle(l1))
    print(remove_cycle(l1))
    print(starting_point_of_cycle(l1))










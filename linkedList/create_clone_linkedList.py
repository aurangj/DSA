
# create_clonelist is not working pls check some thing missing.

class Node(object):
    def __init__(self,value):
        self.value = value
        self.next = None
        self.random = None


class LinkedList(object):
    def __init__(self):
        self.head = None
        self.curr = None

    def addNode(self,node,random):
        if self.head is None:
            self.head = self.curr = node

        else:
            self.curr.next = node
            self.curr.random = random
            self.curr = node

    def iterate_List(self):
        self.curr = self.head
        while self.curr is not None:
            print (self.curr.value)
            self.curr = self.curr.next


    def insert_clone_node(self):
        self.curr = self.head
        while self.curr is not None:
            node_clone = Node(self.curr.value)
            node_clone.next = self.curr.next
            self.curr.next = node_clone
            self.curr = self.curr.next.next


    def create_clonelist(self):
        curr = self.head
        while curr.next is not None:
            print ('looping')
            curr.next.random = curr.random.next
            curr.next = curr.next.next


def getCloneList(l1):

    l2 = LinkedList()
    curr = l1.head
    l1.head = None
    count = 1
    while curr is not None:
        if count % 2 == 0:
            if l2.head is None:
                l2.head = curr
            else:
                l2.head.next = curr
        else:
            if l1.head is None:
                l1.head = curr
            else:
                l1.head.next = curr
        curr = curr.next

        count = count + 1

    return l2

if __name__ == '__main__':
    n1 = Node(2)
    n2 = Node(3)
    n3 = Node(6)
    n4 = Node(1)
    n5 = Node(9)


    l1 = LinkedList()
    l1.addNode(n1,n3)
    l1.addNode(n2,n4)
    l1.addNode(n3,n5)
    l1.addNode(n4,n1)
    l1.addNode(n5,n2)

    l1.insert_clone_node()
    #l1.iterate_List()
    l1.create_clonelist()
    l1.iterate_List()
    #new_list = getCloneList(l1)
    #new_list.iterate_List()







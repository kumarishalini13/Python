class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self , new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printkth(self,k):
        p = self.head
        q = self.head

        while(k >0 and p is not None):
            p = p.next
            k -=1
        if p is None:
            print("out of range")
            return -1

        while p is not None:
            p = p.next
            q = q.next
        print(q.data)

llist = LinkedList()
llist.push(20)
llist.push(4)
llist.push(15)
llist.push(35)
llist.printkth(8)






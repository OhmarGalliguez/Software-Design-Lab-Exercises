"""class node: #SLL
    def __init__(self,data=None):
        self.data=data
        self.next=None
class linked_list:
    def __init__(self):
        self.head = node()
    def append(self,data):
        new_node = node(data)
        cur = self.head
        while cur.next!=None:
            cur = cur.next
        cur.next = new_node
    def length(self):
        cur = self.head
        total = 0
        while cur.next!=None:
            total+=1
            cur = cur.next
        return total
    def display(self):
        elems=[]
        cur_node = self.head
        while cur_node.next!=None:
            cur_node=cur_node.next
            elems.append(cur_node.data)
            print(elems)
    def get(self, index):
        if index>=self.length():
            print ("ERROR: 'Get' index out of range!")
            return None
        cur_idx=0
        cur_node=self.head
        while True:
            cur_node=cur_node.next
            if cur_idx==index: return cur_node.data
            cur_idx+=1
my_list = linked_list()
my_list.display()
my_list.append("Ohmar") #0
my_list.append("D.") #1
my_list.append("Galliguez") #2
my_list.display()
print("The Element at the 0th index: ", my_list.get(0))"""

"""class Node:#CLL
    def __init__(self, data):
        self.data = data;
        self.next = None;
class CreateList:
    def __init__(self):
        self.head = Node(None);
        self.tail = Node(None);
        self.head.next = self.tail;
        self.tail.next = self.head;
    def append(self, data):
        newNode = Node(data);
        if self.head.data is None:
            self.head = newNode;
            self.tail = newNode;
            newNode.next = self.head;
        else:
            self.tail.next = newNode;
            # New node will become new tail.
            self.tail = newNode;
            self.tail.next = self.head;
    def display(self):
        current = self.head;
        if self.head is None:
            print("List is empty");
            return;
        else:
            print("Nodes of the circular linked list: ");
            print(current.data),
            while (current.next != self.head):
                current = current.next;
                print(current.data),


class CircularLinkedList:
    my_list = CreateList();
    my_list.append("Ohmar");
    my_list.append("D.");
    my_list.append("Galliguez");
    my_list.display();"""

class Node:# DLL
    def __init__(self):
        self.data = None
        self.next = None
        self.prev = None
def append(slp_ref, new_data):
    new_node = Node()
    new_node.data = new_data
    new_node.next = (slp_ref)
    new_node.prev = None
    if ((slp_ref) != None):
        (slp_ref).prev = new_node
    (slp_ref) = new_node
    return slp_ref
def findIncrease(node):
    res = 0
    while (node != None):
        res = res + 1
        node = node.next
    return res
SLP = None
SLP.append(1);
SLP.append(4);
SLP.append(3);
SLP.append(2);
print(findIncrease(SLP))
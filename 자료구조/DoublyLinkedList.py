class Node:
    def __init__(self, data):
        self.prev = None
        self.next = None
        self.data = data

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.num = 0

    def push_front(self, data):
        new_node = Node(data)

        if self.num == 0:
            self.head = new_node
            self.tail = new_node

        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        
        self.num += 1

    def push_back(self, data):
        new_node = Node(data)

        if self.num == 0:
            self.head = new_node
            self.tail = new_node

        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

        self.num += 1

    # def push(self, iter, data):


    def begin(self):
        return self.head

    def end(self):
        return self.end


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value):
        new_node =  Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

        self.length += 1
        return True
    def pop(self):
        if self.length == 0:
            return None
        
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            temp = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        return temp

    def prepend(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        temp = self.head
        if self.length == 0:
            return None
        
        if self.length == 1:
            self.head = None
            self.tail = None
        else:   
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
        self.length -= 1
        return temp
    
    def get(self, index):
        if index < 0:
            return None
        
        if self.length == 0:
            self.head = None
            self.tail = None
        else:
            temp = self.head
            for _ in range(index):
                temp = temp.next
            return temp
        
    def set_value(self, index, value):
        temp = self.head
        for _ in range(index):
            temp = temp.next

        if temp:
            temp.value = value
            return True
    
    def insert(self, index, value):
        new_node = Node(value)
        temp = self.head

        if index <= 0 or index > self.length:
            return None
        if index == 0:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        if index == self.length:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        for _ in range(index - 1):
            temp = temp.next

        before = temp
        after = before.next

        new_node.prev = before
        new_node.next = after
        before.next = new_node
        after.prev = new_node

        self.length += 1
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            temp = self.head
            self.head = self.head.next
            self.head.prev = None
            temp.next = None

        if index == self.length:
            temp = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None

        temp = self.head
        for _ in range(index):
            temp = temp.next

        temp.next.prev = temp.prev
        temp.prev.next = temp.next
        temp.prev = None
        temp.next = None

        self.length -= 1
        return temp.value

    def reserve(self):
        temp = None
        current = self.head
        print(f'temp before: {temp}')

        temp = current.prev
        print(f'temp after: {temp}')
        current.prev = current.next
        print(f'current.prev: {current.prev.value}')
        current.next = temp
        current = current.prev



        
my_double_linked_list = DoublyLinkedList(1)
my_double_linked_list.append(2)
my_double_linked_list.append(3)
my_double_linked_list.reserve()



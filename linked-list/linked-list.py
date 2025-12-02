class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.lenght = 1
        
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.lenght += 1
        return True
    
    def pop(self):
        if self.lenght == 0:
            return None
        
        temp = self.head
        pre = self.head

        while (temp.next):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.lenght = self.lenght - 1
        if self.lenght == 0:
            self.head = None
            self.tail = None
        return temp.value
    
    def prepend(self, value):
        new_node = Node(value)
        if self.lenght == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.lenght += 1
        return True
    
    def pop_first(self):
        if self.lenght == 0:
            print("we've no values to pop")
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None

        if self.lenght == 0:
            self.tail = None

        return temp
    
    def get(self, index):
        if index < 0 or index >= self.lenght:
            return None

        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
        
    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    
    def insert(self, index, value):
        new_node = Node(value)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
        elif index == self.lenght:
            self.tail.next = new_node
            self.tail = new_node
        else:
            temp = self.head
            for _ in range(index):
                temp = temp.next

            new_node.next = temp.next
            temp.next = new_node
        self.lenght += 1
        return True 
    
    def remove(self, index):
        temp = self.head
        if index == 0:
            self.head = self.head.next
            temp.next = None
        elif index == self.lenght - 1:
            while temp.next.next is not None:
                temp = temp.next
            temp.next = None
        else:
            for _ in range(index - 1):
                temp = temp.next
            temp.next = temp.next.next
        self.lenght -= 1
        
    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None

        for _ in range(self.lenght):
            after = temp.next
            temp.next = before
            before = temp
            temp = after
    
    def middle_node(self):
        fast = self.head
        slow = self.head
        while (fast.next):
            fast = fast.next.next
            slow = slow.next

        return slow.value
    
    def reverse_at_index(self, start_index, end_index):
        dummy_node = Node(0)
        dummy_node.next = self.head
        previous_node = dummy_node

        for i in range(start_index):
            print("index value:", i)
            previous_node = previous_node.next
            print("inside-loop value:", previous_node.value)
        current_node = previous_node.next
        print("out-of-loop value from current node:", current_node.value)

   
        node_to_move = current_node.next
        current_node.next = node_to_move.next
        node_to_move.next = previous_node.next
        previous_node.next = node_to_move

        print("previos nodes next:", previous_node.value)

        print("first line:", node_to_move.value)
        print("second line:", current_node.value)
        print("third line:", node_to_move.value)
        print("fourth line:", previous_node.value)


my_linked_list = LinkedList(1)

my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)
my_linked_list.reverse_at_index(2, 5)

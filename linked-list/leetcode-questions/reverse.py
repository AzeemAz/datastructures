from node_creation_script import LinkedList

class Reverse:
    def __init__(self, linked_list):
        self.linked_list = linked_list   

    def reverse(self, start_index, end_index):
        prev = None
        curr = self.linked_list.head 
        for i in range(start_index, end_index):
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        self.linked_list.head = prev

my_linked_list = LinkedList(1)
reverse_nodes = Reverse(my_linked_list)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
reverse_nodes.reverse()
my_linked_list.print_list()

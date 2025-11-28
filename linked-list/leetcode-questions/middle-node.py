from node_creation_script import LinkedList

class MiddleNode:
    def __init__(self, linked_list):
        self.head = linked_list.head

    def find_middle_node(self):
        fast = self.head
        slow = self.head

        while(fast is not None and fast.next is not None):
            slow = slow.next
            fast = fast.next.next
        
        return slow

my_linked_list = LinkedList(1)
middle_node_finder = MiddleNode(my_linked_list)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
print("middle node is:", middle_node_finder.find_middle_node().value)
my_linked_list.print_list()
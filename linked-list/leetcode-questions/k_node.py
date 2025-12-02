from node_creation_script import LinkedList

class K_node:
    def __init__(self, linked_list):
          self.head = linked_list.head

    def finding_k_node(self, k):
        slow = self.head
        fast = self.head

        for i in range(k):
            if fast is None:
                return None
            fast = fast.next
        
        while(fast):
            fast = fast.next
            slow = slow.next
        
        return slow.value

my_linked_list = LinkedList(1)
has_loop_finder = K_node(my_linked_list)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
print(has_loop_finder.finding_k_node(2))
my_linked_list.print_list()
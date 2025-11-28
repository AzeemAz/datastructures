from node_creation_script import LinkedList

class hasLoop:
    def __init__(self, linked_list):
        self.head = linked_list.head
        self.tail = linked_list.tail

    def has_loop(self):
        slow = self.head
        fast = self.head
        self.tail.next = self.head

        while(fast is not None and fast.next is not None):
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                print("ponting to the same node.")
                return True
        print("No loop found.")
        return False




my_linked_list = LinkedList(1)

has_loop_finder = hasLoop(my_linked_list)
print(has_loop_finder.has_loop())
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.print_list()
from node_creation_script import LinkedList

class RemoveDuplicate:
    def __init__(self, linked_list):
          self.head = linked_list.head

    def remove_duplicate(self):
        current = self.head
        runner = self.head

        while current:
            runner = current
            while runner.next:
                if current.value == runner.next.value:
                    runner.next = runner.next.next
                else:
                    runner = runner.next 
            current = current.next
        return current
            
         
    

my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.print_list()
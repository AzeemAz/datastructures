class Stack:
    stack_list = []
    def push(self, value):
        return self.stack_list.append(value)
    
    def print_stack(self):
        for i in range(len(self.stack_list)):
            print(self.stack_list[i])

my_stack = Stack()
my_stack.push("Hello")
my_stack.print_stack()
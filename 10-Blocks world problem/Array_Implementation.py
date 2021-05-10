class Stack():

    def __init__(self):
        self.array = []

    def peek(self):
        return self.array[len(self.array)-1]

    def push(self, data):
        self.array.append(data)
        return

    def pop(self):
        if len(self.array)!= 0:
            self.array.pop()
            return
        else:
            print("Stack Empty")
            return
    def print_stack(self):
        for i in range(len(self.array)-1, -1, -1):
            print(self.array[i])
        return



my_stack = Stack()
my_stack.push("BLOCK A")
my_stack.push("BLOCK B")
my_stack.push("BLOCK C")
my_stack.push("BLOCK D")
my_stack.print_stack()

my_stack.pop()
my_stack.pop()
my_stack.print_stack()

print(my_stack.peek())

print(my_stack.__dict__)
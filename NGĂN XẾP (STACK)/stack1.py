class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.items[-1]

    def size(self):
        return len(self.items)

stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)

print("Stack size:", stack.size())  # Output: 3

print("Top item:", stack.peek())  # Output: 3

item = stack.pop()
print("Popped item:", item)  # Output: 3

print("Is stack empty?", stack.is_empty())  # Output: False

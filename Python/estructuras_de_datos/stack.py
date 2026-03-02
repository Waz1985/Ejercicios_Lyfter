class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            raise RuntimeError("Stack is empty")
        
        value = self.top.value
        self.top = self.top.next
        return value
    
    def print_stack(self):
        current = self.top
        while current is not None:
            print(current.value)
            current = current.next

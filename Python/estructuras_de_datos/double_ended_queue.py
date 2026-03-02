class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class Deque:
    def __init__(self):
        self.head = None
        self.tail = None

    def push_left(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def push_right(self, value):
        new_node = Node(value)

        if self.tail is None:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def pop_left(self):
        if self.head is None:
            raise RuntimeError("Deque is empty")

        value = self.head.value

        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None

        return value

    def pop_right(self):
        if self.tail is None:
            raise RuntimeError("Deque is empty")

        value = self.tail.value

        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None

        return value

    def print_deque(self):
        current = self.head
        while current is not None:
            print(current.value)
            current = current.next

d = Deque()

d.push_left(10)
d.push_right(20)
d.push_left(5)
d.push_right(30)

d.print_deque()

print(d.pop_left())
print(d.pop_right())
print(d.pop_left())
print(d.pop_right())
d.print_deque()
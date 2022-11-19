class Node:
    def __init__(self, element=None, next_node=None):
        self.element = element
        self.next_node = next_node

class Stack:
    def __init__(self):
        self.stack = None

    def push(self, element):
        node = Node(element, self.stack)
        self.stack = node

    def pop(self):
        element = self.stack.element
        self.stack = self.stack.next_node
        return element
        
    def is_empty(self):
        return self.stack == None
    def __str__(self):
        if self.stack is None:
            return None
        node = self.stack
        result = "["
        while node is not None:
            result += str(node.element) + " "
            node = node.next_node
        return result[:-1] + "]"

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, element):
        if self.head is None:
            self.head = self.tail = Node(element)
        else:
            node = Node(element)
            self.tail.next_node = node
            self.tail = node

    def dequeue(self):
        element = self.head.element
        if self.tail == self.head:
            self.tail = self.head = None
        else:
            self.head = self.head.next_node
        return element

    def is_empty(self):
        return self.head is None

    def __str__(self):
        if self.head is None:
            return None
        node = self.head
        result = "["
        while node is not None:
            result += str(node.element) + " "
            node = node.next_node
        return result[:-1] + "]"

def is_palindrome(s):
    stack = Stack()
    queue = Queue()
    for c in s:
        stack.push(c)
        queue.enqueue(c)
    while not stack.is_empty():
        if stack.pop() != queue.dequeue():
            return False
    return True

print(is_palindrome("racecar"))
print(is_palindrome("noon"))
print(is_palindrome("python"))
print(is_palindrome("madam"))


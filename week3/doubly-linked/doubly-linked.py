class Node:
    # A doubly-linked node.
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    # A doubly-linked list.
    def __init__(self):
        # Create an empty list.
        self.tail = None
        self.head = None
        self.count = 0

    def iter(self):
        # Iterate through the list.
        current = self.head
        while current:
            val = current.data
            current = current.next
            yield val

    def size(self) -> int:
        # Returns the number of elements in the list
        return self.count

# I did get help with setting up these functions with research and attempting to understand
# all the different areas of this assignement. 

    def addFirst(self, data) -> None:
        # Add a node at the front of the list
        newNode = Node(data)
        if(self.head == None):
            self.head = newNode
            return
        else:
            self.head.prev = newNode
            newNode.next = self.head
            self.head = newNode
        # words.addFirst(firstItem)
        print(words)

    def addLast(self, data) -> None:
        # Add a node at the end of the list
        # pass
        newNode = Node(data)
        if(self.head == None):
            self.head = newNode
            return
        else:
            temp = self.head
            while(temp.next != None):
                temp = temp.next
            temp.next = newNode
            newNode.prev = temp
          
    def addAtIndex(self, data, index):
        # Add a node to the list at the given index position
        # If index equals to the length of linked list, the node will be appended to the end of linked list
        # If index is greater than the length, the data will not be inserted.
        # This function does not replace the data at the index, but pushes everything else down.
        newNode = Node(data)
        if(index < 1):
            print('\n postion should be >= 1.')
        elif(index == 1):
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode
        else:
            temp = self.head
            for i in range(1, index-1):
                if(temp != None):
                    temp = temp.next

            if(temp != None):
                newNode.next = temp.next
                newNode.prev = temp
                temp.next = newNode
                if(newNode.next != None):
                    newNode.next.prev = newNode
            else:
                print("\n The previous node is null.")

    def indexOf(self, data):
        # Search through the list. Return the index position if data is found, otherwise return -1    
        # pass
        temp = self.head
        found = 0
        i = 0
        if(temp != None):
            while(temp != None):
                
                if(temp.data == data):
                    found +=1
                    break
                temp = temp.next
                i +=1
            if(found == 1):
                print(i)
            else:
                print(data, "is not found in the list.")
        else:
            print("The list is empty.")

    def add(self, data) -> None:
        # Append an item to the end of the list
        self.addLast(data)

    def clear(self) -> None:
        # Remove all of the items from the list
        self.head = None
        self.tail = None
        self.count = 0

    def deleteAtIndex(self, index) -> None:
        # Delete the node at the index-th in the linked list, if the index is valid.

        if (index > (self.count-1)):
            return
            
        curr = self.head
        prev = self.head

        for n in range(index):
            prev = curr
            curr = curr.next
            
        prev.next = curr.next
        curr.prev = prev
        self.count -= 1

        if (curr == self.head):
            self.head = curr.next
            curr.prev = None
        elif (curr == self.tail):
            prev.next = None
            self.tail = prev       

        return

    def delete(self, data) -> None:
        # Delete a node from the list who's value matches the supplied value
        current = self.head
        prev = self.head
        while current:
            if current.data == data:
                if current == self.tail:
                    prev.next = None
                    self.tail = prev
                elif current == self.head:
                    current.next.prev = None
                    self.head = current.next
                else:
                    prev.next = current.next
                    current.next = prev
                self.count -= 1
                return
            prev = current
            current = current.next

    def __getitem__(self, index):
        if index > self.count - 1:
            raise Exception("Index out of range.")
        current = self.head
        for n in range(index):
            current = current.next
        return current.data

    def __setitem__(self, index, value):
        if index > self.count - 1:
            raise Exception("Index out of range.")
        current = self.head
        for n in range(index):
            current = current.next
        current.data = value

    def __str__(self):
        myStr = ""
        for node in self.iter():
             myStr += str(node)+ " "
        return myStr

words = DoublyLinkedList()
words.add(data='May') 
words.add(data='the')
words.add(data='force')
words.add(data='be')
words.add(data='with')
words.add(data='you')
words.add(data='!')

print(words)

words.indexOf('with')

words.delete('you')
words.addAtIndex('us', 6)
words.delete('!')
words.addAtIndex('all', 7)
words.addAtIndex('!', 8)
print(words)

# add "all" before "!"
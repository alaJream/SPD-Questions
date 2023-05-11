# Sort linked list containing 0’s, 1’s, and 2’s in a single traversal

# Given a linked list containing 0's, 1's, and 2's, sort the linked list by doing a single traversal of it.

# For example,

# Input:  0 —> 1 —> 2 —> 2 —> 1 —> 0 —> 0 —> 2 —> 0 —> 1 —> 1 —> 0 —> NULL
 
# Output: 0 —> 0 —> 0 —> 0 —> 0 —> 1 —> 1 —> 1 —> 1 —> 2 —> 2 —> 2 —> NULL


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

    def printList(self):
        ptr = self.head
        while ptr:
            print(ptr.data, end=" -> ")
            ptr = ptr.next
        print("NULL")

    def sortList(self):
        count = [0, 0, 0]
        ptr = self.head
        while ptr:
            count[ptr.data] += 1
            ptr = ptr.next

        i = 0
        ptr = self.head
        while ptr:
            if count[i] == 0:
                i += 1
            else:
                ptr.data = i
                count[i] -= 1
                ptr = ptr.next

llist = LinkedList()
llist.push(0)
llist.push(1)
llist.push(0)
llist.push(2)
llist.push(1)
llist.push(1)
llist.push(2)
llist.push(1)
llist.push(2)

print("Linked List before sorting")
llist.printList()

llist.sortList()

print("\nLinked List after sorting")
llist.printList()

# Rearrange linked list so that it has alternating high and low values
# Google Translate Icon
# Given a linked list of integers, rearrange it such that every second node of the linked list is greater than its left and right nodes. In other words, rearrange the linked list node in alternating high-low.

# Assume no duplicate nodes are present in the linked list. Several lists might satisfy the constraints; we need to print any one of them. For example,

# Input:  1 —> 2 —> 3 —> 4 —> 5 —> 6 —> 7
# Output: 1 —> 3 —> 2 —> 5 —> 4 —> 7 —> 6
 
 
# Input:  9 —> 6 —> 8 —> 3 —> 7
# Output: 6 —> 9 —> 3 —> 8 —> 7
 
 
# Input:  6 —> 9 —> 2 —> 5 —> 1 —> 4
# Output: 6 —> 9 —> 2 —> 5 —> 1 —> 4


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

    def rearrange(self):
        ptr = self.head
        if ptr is None:
            return
        while ptr.next is not None:
            if ptr.data > ptr.next.data:
                ptr.data, ptr.next.data = ptr.next.data, ptr.data
            if ptr.next.next is None:
                break
            if ptr.next.data < ptr.next.next.data:
                ptr.next.data, ptr.next.next.data = ptr.next.next.data, ptr.next.data
            ptr = ptr.next.next

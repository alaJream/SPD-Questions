# given two sorted linked lists, merge them so that the resulting linked list is also sorted
# head1->4->8->15->19->Null
# head2->7->9->10->16->Null

# expected result: 
# head1->4->7->8->9->10->15->16->19->Null

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def sorted_merge(head1, head2):
    result = Node(0)

    last = result
    while head1 is not None and head2 is not None:
        if head1.data <= head2.data:
            last.next = head1
            head1 = head1.next
        else:
            last.next = head2
            head2 = head2.next

        last = last.next

    if head1 is not None:
        last.next = head1

    elif head2 is not None:
        last.next = head2

    return result.next

def printList(node):
    while node:
        print(node.data, end = " ")
        node = node.next

head1 = Node(4)
head1.next = Node(8)
head1.next.next = Node(15)
head1.next.next.next = Node(19)

head2 = Node(7)
head2.next = Node(9)
head2.next.next = Node(10)
head2.next.next.next = Node(16)

merged_head = sorted_merge(head1, head2)

printList(merged_head)

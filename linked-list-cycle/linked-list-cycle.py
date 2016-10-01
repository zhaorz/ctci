"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as:

    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""

class Node(object):
    def __init__(self, data = None, next_node = None):
        self.data = data
        self.next = next_node

def has_cycle(head):
    if head == None or head.next == None:
        return False
    tortoise = head
    hare = head.next

    while tortoise != None:
        if tortoise == hare:
            return True
        if tortoise.next == None:
            return False
        if hare.next == None or hare.next.next == None:
            return False

        tortoise = tortoise.next
        hare = hare.next.next

    return False

class LinkedList:
    def __init__(self, val):
        self.val = val
        self.next = None


def print_ll(head):
    while (head != None):
        print(head.val, end=' ')
        head = head.next
    print()


def append(head, val):
    node = LinkedList(val)
    while (head.next != None):
        head = head.next
    head.next = node


def reverse(head):
    prev = None
    while (head != None):
        temp = head.next
        head.next = prev
        prev = head
        head = temp
    return prev


head = LinkedList(1)
print_ll(head)
append(head, 2)
print_ll(head)
head = reverse(head)
print_ll(head)
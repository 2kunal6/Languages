class Node:
    def __init__(self, data):
        self.val = data
        self.next = None

def print_ll(head):
    while(head != None):
        print(head.val)
        head = head.next

def insert_at_begin(head, data):
    new_node = Node(data)
    if(head == None):
        head = new_node
    else:
        new_node.next = head
        head = new_node
    return head

head = None
print_ll(head)
head = insert_at_begin(head, 5)
print_ll(head)

# practice other methods
# insert_at_index
# insert_at_end
# update_node
# remove_first_node
# remove_last_node
# remove_node_at_index
# remove_nodes_with_value
# size_of_ll


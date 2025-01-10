class node:
    def __init__(self, value):  # it  is a constructor to initialize the node with a value
        self.value = value
        self.next = None

class singlylinkedlist:
    def __init__(self):  # this constructor is to initialize the linked list
        self.head = None

    def append(self, value):
        new_node = node(value)  # now create a new node
        if not self.head:6
            self.head = new_node  # now we'll set it as the head if the list is empty
            return
        last_node = self.head
        while last_node.next:  # then traverse the list to find the last node
            last_node = last_node.next
        last_node.next = new_node  # now link the new node at the end

    def display(self):
        current_node = self.head
        while current_node:  # then print each node's value followed by "->" if there is a next node
            print(current_node.value, end=" -> " if current_node.next else "\n")
            current_node = current_node.next

    def remove_n_after_m(self, m, n):
        current_node = self.head
        while current_node:
            # now we have to skip the first m nodes
            for _ in range(m - 1):
                if not current_node:
                    return
                current_node = current_node.next

            if not current_node:
                return
            
            # now remove the next n nodes
            temp_node = current_node.next
            for _ in range(n):
                if not temp_node:
                    break
                temp_node = temp_node.next

            current_node.next = temp_node  # here we're link the current node to the node after the deleted ones
            current_node = temp_node

# below is the example usage:

linked_list = singlylinkedlist()
values = [9, 1, 3, 5, 9, 4, 10, 1]  # this is sample data for the linked list
for value in values:
    linked_list.append(value)

print("original linked list:") 
linked_list.display()

m, n = 2, 1  # parameters ---> skip m nodes ---> remove n nodes after that...
linked_list.remove_n_after_m(m, n)

print(f"modified linked list after skipping {m} nodes and removing {n} nodes:")
linked_list.display()
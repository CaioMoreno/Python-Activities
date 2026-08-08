class LinkedList():
    class Node():
        def __init__(self, element):
            self.element = element
            self.next = None
            self.previous = None

    def __init__(self):
        self.length = 0
        self.head = None

    def is_empty(self):
        return self.length == 0

    def add(self, element):
        node = self.Node(element)

        if self.is_empty():
            self.head = node
        else:
            current_node = self.head

            while current_node.next is not None:
                current_node = current_node.next

            current_node.next = node
            node.previous = current_node

        self.length += 1

    def remove(self, element):
        current_node = self.head

        while current_node is not None and current_node.element != element:
            current_node = current_node.next

        if current_node is None:
            return

        # Removing the head
        if current_node.previous is None:
            self.head = current_node.next

            if self.head is not None:
                self.head.previous = None

        # Removing a node in the middle/end
        else:
            current_node.previous.next = current_node.next

            if current_node.next is not None:
                current_node.next.previous = current_node.previous

        self.length -= 1

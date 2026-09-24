class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def addFirst(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def addLast(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def removeFirst(self):
        if self.head is None:
            return None

        removed_data = self.head.data
        self.head = self.head.next

        if self.head is None:
            self.tail = None

        return removed_data

    def removeLast(self):
        if self.head is None:
            return None

        if self.head == self.tail:
            removed_data = self.head.data
            self.head = None
            self.tail = None
            return removed_data

        current = self.head

        while current.next != self.tail:
            current = current.next

        removed_data = self.tail.data
        current.next = None
        self.tail = current

        return removed_data

    def peekFirst(self):
        if self.head is None:
            return None

        return self.head.data

    def peekLast(self):
        if self.tail is None:
            return None

        return self.tail.data

    def toList(self):
        result = []
        current = self.head

        while current is not None:
            result.append(current.data)
            current = current.next

        return result

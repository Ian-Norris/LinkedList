class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def get_data(self):
        return self.data

    def __str__(self):
        return self.data


class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        if self.head is None:
            return True
        else:
            return False

    def size(self):
        count = 0
        cur_node = self.head
        while cur_node is not None:
            count += 1
            cur_node = cur_node.next
        return count

    def add(self, item):
        new_item = Node(item)

        new_item.next = self.head
        self.head = new_item

    def append(self, item):
        new_item = Node(item)

        if self.head is None:
            self.head = new_item
            return

        last_item = self.head
        while last_item.next is not None:
            last_item = last_item.next
        last_item.next = new_item

    def pop(self, pos=None):
        cur_node = self.head
        previous_node = None
        cur_location = 0

        size = self.size()
        if pos is None:
            #If only one item in list it will just make the make head None
            if size == 1:
                self.head = None
                return
            #Stops the loop at node right before the last node
            while cur_location < size-1:
                previous_node = cur_node
                cur_node = cur_node.next
                cur_location += 1
            previous_node.next = None
            return cur_node.data


        next_node = None
        if pos >= size:
            return 'Position given was larger then data structure'
        if pos == 0:
            self.head = cur_node.next
            return cur_node.data
        while cur_location < pos:
            previous_node = cur_node
            cur_node = cur_node.next
            next_node = cur_node.next
            if cur_location == pos-1:
                previous_node.next = next_node
            cur_location += 1
        return cur_node.data

    def search(self, item):
        cur_item = self.head
        while cur_item is not None:
            if cur_item.data == item:
                return True
            cur_item = cur_item.next
        return False

    def remove(self, item):
        cur_node = self.head
        previous_node = self.head

        if item == self.head.data:
            self.head = self.head.next
            return

        while cur_node is not None:
            if cur_node.data == item:
                previous_node.next = cur_node.next
                return
            previous_node = cur_node
            cur_node = cur_node.next

    def __iter__(self):
        current = self.head
        while current is not None:
            yield current
            current = current.next

    def print_list(self):
        cur_node = self.head
        while cur_node is not None:
            print(cur_node.data)
            cur_node = cur_node.next

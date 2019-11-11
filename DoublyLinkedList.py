class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

    def __str__(self):
        return self.data


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def get_head(self):
        return self.head

    def get_tail(self):
        return self.tail

    def is_empty(self):
        if self.head is None:
            return True
        else:
            return False

    def size(self):
        cur_node = self.head
        count = 0
        while cur_node is not None:
            count += 1
            cur_node = cur_node.next
        return count

    def add(self, item):
        new_node = Node(item)
        if self.head is None:
            new_node.previous = None
            new_node.next = None
            self.head = new_node
            self.tail = new_node
        else:
            first_node = self.head
            first_node.previous = new_node
            new_node.previous = None
            new_node.next = first_node
            self.head = new_node

    def append(self, item):
        new_node = Node(item)
        if self.head is None:
            new_node.previous = None
            new_node.next = None
            self.head = new_node
            self.tail = new_node
        else:
            last_node = self.tail
            last_node.next = new_node
            new_node.previous = last_node
            self.tail = new_node

    def pop(self, pos=None):
        size = self.size()

        #Exception for only one value in the list
        if size == 1:
            cur_node = self.head
            self.head = None
            self.tail = None
            return cur_node
        if pos is None or pos == size-1:
            last_node = self.tail
            new_last_node = self.tail.previous
            new_last_node.next = None
            self.tail = new_last_node
            return last_node
        else:
            cur_node = self.head
            prev_node = None
            next_node = None
            cur_pos = 0

            #Exception for if pos is the head of list
            if pos == 0:
                self.head = cur_node.next
                return cur_node
            #this loop is starting at index 1 | NOT STARTING AT HEAD
            while cur_pos < size:
                prev_node = cur_node
                cur_node = cur_node.next
                next_node = cur_node.next
                if cur_pos == pos-1:
                    prev_node.next = next_node
                    next_node.previous = prev_node
                    return cur_node

    def search(self, item):
        cur_item = self.head
        while cur_item is not None:
            if cur_item.data == item:
                return True
            cur_item = cur_item.next
        return False

    def remove(self, item):
        size = self.size()
        cur_pos = 0
        cur_node = self.head
        prev_node = None
        next_node = None

        while cur_pos < size:
            next_node = cur_node.next
            prev_node = cur_node.previous

            if cur_node.data == item:
                #Checks if the item found was the last item in list
                if next_node is None:
                    self.pop()
                    return
                # Checks if the item found was the first item in list
                elif prev_node is None:
                    self.pop(0)
                    return
                prev_node.next = next_node
                next_node.previous = prev_node
                return
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


class Node:
    def __init__(self, value: int):
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.length = 0
        self.lookup = {}
        self.reverse_lookup = {}
        self.head = None
        self.tail = None

    def get(self, key: int) -> int:
        if key in self.lookup:
            self.detach(self.lookup[key])
            self.prepend(self.lookup[key])
            return self.lookup[key].value
        
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.lookup:
            self.lookup[key].value = value
            self.detach(self.lookup[key])
            self.prepend(self.lookup[key])
            return
        node = Node(value)
        self.lookup[key] = node
        self.reverse_lookup[node] = key
        self.prepend(node)
        self.trim_cache()

    def detach(self, node: Node):
        if self.head == node:
            if self.head.next:
                self.head = self.head.next
                self.head.prev = None
                self.length -= 1
                return

            self.head = None
            self.tail = None
            self.length -= 1
            return
        
        if self.tail == node:
            tail = self.tail.prev
            self.tail = tail
            self.tail.next = None
            self.length -= 1
            return

        node.prev.next = node.next
        node.next.prev = node.prev
        self.length -= 1

    def prepend(self, node: Node):
        if self.length == 0:
            self.head = node
            self.tail = node
            node.prev = None
            node.next = None
            self.length += 1
            return
        
        node.next = self.head
        node.prev = None
        self.head.prev = node
        self.head = node
        self.length += 1

    def trim_cache(self):
        if self.length <= self.capacity:
            return

        key = self.reverse_lookup[self.tail]
        del self.lookup[key]
        del self.reverse_lookup[self.tail]
        self.detach(self.tail)
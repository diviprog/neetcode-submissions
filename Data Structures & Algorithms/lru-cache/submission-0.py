class LRUCache:
    class _Node:
        __slots__ = ("key", "val", "prev", "next")
        def __init__(self, key=0, val=0):
            self.key = key
            self.val = val
            self.prev = None
            self.next = None

    def __init__(self, capacity: int):
        self.cap = capacity
        self.map = {}  # key -> _Node
        # sentinel head/tail to avoid edge-case checks
        self.head = self._Node()
        self.tail = self._Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    # --- internal DLL helpers ---
    def _add_front(self, node):
        # insert right after head (most recently used position)
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def _remove(self, node):
        p, n = node.prev, node.next
        p.next = n
        n.prev = p

    def _move_to_front(self, node):
        self._remove(node)
        self._add_front(node)

    def _pop_lru(self):
        # node just before tail is least recently used
        lru = self.tail.prev
        if lru is self.head:
            return None
        self._remove(lru)
        return lru

    # --- API ---
    def get(self, key: int) -> int:
        node = self.map.get(key)
        if not node:
            return -1
        self._move_to_front(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        node = self.map.get(key)
        if node:
            node.val = value
            self._move_to_front(node)
            return

        if self.cap == 0:
            return  # capacity 0: ignore inserts (or you could choose to noop)

        new_node = self._Node(key, value)
        self.map[key] = new_node
        self._add_front(new_node)

        if len(self.map) > self.cap:
            lru = self._pop_lru()
            if lru:
                del self.map[lru.key]
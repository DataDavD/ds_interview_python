from typing import Any, Optional


class Node:
    def __init__(self, data):
        self.data: Any = data
        self.next_element: Optional[Node] = None


class DNode:
    def __init__(self, data):
        self.data: Any = data
        self.next_element: Optional[DNode] = None
        self.prev_element: Optional[DNode] = None

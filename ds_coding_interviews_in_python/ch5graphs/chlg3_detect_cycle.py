from typing import List

from ds_coding_interviews_in_python.ch5graphs.graph import Graph


def detect_cycle(g: Graph):
    # visited list to keep track of the nodes that have been visited
    # since the beginning of the algorithm
    visited = [False] * g.vertices
    # rec_node_stack keeps track of the nodes which are part of
    # the current recursive call
    rec_node_stack = [False] * g.vertices
    for node in range(g.vertices):
        # DFS recursion call
        if detect_cycle_rec(g, node, visited, rec_node_stack):
            return True
    return False


def detect_cycle_rec(g: Graph, node: int, visited: List[bool], rec_node_stack: List[bool]):
    # Node was already in recursion stack. Cycle found.
    if rec_node_stack[node]:
        print(f"returning True for node={node}")
        return True
    # It has been visited before this recursion
    if visited[node]:
        print(f"returning False for node={node}")
        return False
    # Mark current node as visited and
    # add to recursion stack
    visited[node] = True
    rec_node_stack[node] = True
    head = g.array[node].get_head()
    while head is not None:
        # Pick adjacent node and call it recursively
        adjacent = head.data
        print(f"printing adjacent={adjacent}")
        # If the node is visited again in the same recursion => Cycle found
        if detect_cycle_rec(g, adjacent, visited, rec_node_stack):
            return True
        head = head.next_element
    # remove the node from the recursive call
    rec_node_stack[node] = False
    return False

from typing import Any

from ds_coding_interviews_in_python.ch4stackqueue.stack import MyStack
from ds_coding_interviews_in_python.ch5graphs.graph import Graph


def dfs_mother_helper(g: Graph, source: Any) -> int:
    vertices_reach = 0
    num_v = g.vertices
    if num_v == 0:
        return -1

    # Create Stack(Implemented in previous lesson) for Depth First Traversal
    # and Push source in it
    stack = MyStack()
    stack.push(source)
    visited = set()
    # Traverse while the stack is not empty
    while not stack.is_empty():
        # Pop a vertex from stack and add it to the result
        curr_node = stack.pop()
        # Get adjacent vertices to the current node from the array
        # and if they are not already visited then push them onto the Stack
        temp = g.array[curr_node].get_head()
        while temp is not None:
            if temp.data not in visited:
                stack.push(temp.data)
                # visit the vertex
                visited.add(temp.data)
                vertices_reach += 1
            temp = temp.next_element

    return vertices_reach + 1  # +1 is to include source itself


def mother_vertex_naive(g: Graph) -> int:
    """
    Returns mother vertex of graph. Time complexity is O(V(V+E)) since at worst
    we are looping for each vertex through each vertex and edge.

    :param g: Graph
    :return: number of mother vertex
    """
    # Traverse Graph using DFS and mother is vertex is vertex whose DFS
    # traversal results is equal to total number of vertices
    num_v_reached = 0
    for i in range(g.vertices):
        num_v_reached = dfs_mother_helper(g, i)
        if int(num_v_reached) + 1 == g.vertices:
            return i
    return -1  # return -1 if no vertex is mother/doesn't traverse all nodes

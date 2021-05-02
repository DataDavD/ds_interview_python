from typing import Any, Dict, List, Optional, Set, Tuple, Union

from ds_coding_interviews_in_python.ch4stackqueue.myqueue import MyQueue
from ds_coding_interviews_in_python.ch5graphs.graph import Graph


def bfs_simple(g: Graph, source: Any) -> str:
    """
    Bread first search algo. Time complexity is O(V+E) for the number of edges and vertices
    we traverse (since at worst case have to traverse all V and E). The space complexity is O(V)
    since we have to keep track of at worse case we have to hold all vertices while traversing
    the Graph.
    V is vertices and E is edges

    :param g: Graph
    :param source: starting node
    :return: str of path
    """
    result: str = ""
    num_v: int = g.vertices
    if num_v == 0:
        return result

    queue = MyQueue()
    queue.enqueue(source)
    # Create list to hold visited vertices
    # and make a node visited whenever you enqueue it into the queue
    visited = set()
    while not queue.is_empty():
        # Dequeue a vertex from the queue
        vertex = queue.dequeue()
        result += str(vertex)
        # print(str(vertex) + " ", end="")

        # If not visited, mark as visited and enqueue it
        temp = g.array[vertex].get_head()
        while temp:
            if temp.data not in visited:
                visited.add(temp.data)
                queue.enqueue(temp.data)
            temp = temp.next_element

    return result


def bfs_simple_dict(graph: Dict[Any, Any], start_node: Any) -> str:
    result = ""
    if len(graph) == 0:
        return "graph is empty"
    visited = set()
    visited.add(start_node)
    queue = [start_node]

    while queue:
        s = queue.pop(0)
        result += s

        for neighbor in graph[s]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return result


def bfs_helper(g: Graph, source: Any, visited: List[bool]) -> Tuple[str, List[bool]]:
    result = ""
    # Create Queue(implemented in previous lesson) for Breadth First Traversal
    # and enqueue source in it
    queue = MyQueue()
    queue.enqueue(source)
    visited[source] = True  # Mark as visited
    # Traverse while queue is not empty
    while not queue.is_empty():
        # Dequeue a vertex/node from queue and add it to result
        curr_node = queue.dequeue()
        result += str(curr_node)
        # Get adjacent vertices to the current_node from the list,
        # and if they are not already visited then enqueue them in the Queue
        temp = g.array[curr_node].get_head()
        while temp is not None:
            if not visited[temp.data]:
                queue.enqueue(temp.data)
                visited[temp.data] = True  # Visit the current Node
            temp = temp.next_element
    return result, visited


def bfs(g: Graph, source: int) -> str:
    result: str = ""
    num_v: int = g.vertices
    if num_v == 0:
        return result

    visited = list()
    for i in range(num_v):
        visited.append(False)
    # start from the source
    result, visited = bfs_helper(g, source, visited)
    # visit the remaining nodes
    for i in range(num_v):
        if not visited[i]:
            result_new, visited = bfs_helper(g, i, visited)
            result += result_new

    return result


def dfs_simple_dict(
    graph: Dict[Any, Any],
    start_node: Any,
    visited: Optional[Union[List[Any], Set[Any]]] = None,
    result: str = "",
) -> Tuple[Optional[Union[List[Any], Set[Any]]], str]:
    """
    DFS algo implementation

    :param graph: Dict[Any, AnyP
    :param start_node: Any: starting node for DFS algo traversal
    :param visited: Optional[Union[List[Any], Set[Any]]]
    :param result: str result of path taken during DFS
    :return: final visited and result
    """
    if len(graph) == 0:
        return visited, result
    if isinstance(visited, list):
        visited = set(visited)
    if visited is None:
        visited = set()

    visited.add(start_node)
    result += str(start_node)
    print(start_node)

    for next_val in set(graph[start_node]) - visited:
        if next_val not in visited:
            visited, result = dfs_simple_dict(graph, next_val, visited, result)
    return visited, result

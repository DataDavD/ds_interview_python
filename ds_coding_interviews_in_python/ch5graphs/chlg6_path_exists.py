from ds_coding_interviews_in_python.ch4stackqueue.myqueue import MyQueue
from ds_coding_interviews_in_python.ch5graphs.graph import Graph


def path_exists(g: Graph, source: int, dest: int) -> bool:
    """
    Finds if a path exists from a source vertex to a destination vertex in a
    directed Graph.
    Since we are essentially using BFS (and can also use DFS), the time complexity
    is the same: O(V+E)

    :param g: Graph
    :param source: source vertex
    :param des: destination vertex
    :return:
    """
    visited = set()
    queue = MyQueue()
    queue.enqueue(source)

    while not queue.is_empty():
        vertex = queue.dequeue()
        if vertex == dest:
            return True

        adjacent = g.array[vertex].get_head()
        while adjacent:
            if adjacent.data not in visited:
                visited.add(adjacent.data)
                queue.enqueue(adjacent.data)
            adjacent = adjacent.next_element

    # destination not found in search
    return False

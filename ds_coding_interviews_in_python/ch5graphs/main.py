from typing import Any

from ds_coding_interviews_in_python.ch4stackqueue.myqueue import MyQueue
from ds_coding_interviews_in_python.ch5graphs.graph import Graph


def bfs_simple(g: Graph, source: Any) -> str:
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


def bfs_simple_dict(graph, start_node):
    visited = [start_node]
    queue = [start_node]
    result = ""

    while queue:
        s = queue.pop(0)
        result += s

        for neighbor in graph[s]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)

    return result

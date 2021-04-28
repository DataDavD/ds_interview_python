from ds_coding_interviews_in_python.ch4stackqueue.myqueue import MyQueue
from ds_coding_interviews_in_python.ch5graphs.graph import Graph

g = Graph(4)
g.add_edge(0, 1)
g.add_edge(0, 2)
print(g.array[0].to_list())
g.add_edge(1, 3)
g.add_edge(2, 3)
g.print_graph()

print(g.array[1].get_head().data)


def bfs(g: Graph, source: int) -> str:
    result: str = ""
    num_v: int = g.vertices
    if num_v == 0:
        return result

    queue = MyQueue()
    queue.enqueue(source)
    # Create list to hold visited vertices
    visited = set()
    while not queue.is_empty():
        # Dequeue a vertex from the queue
        vertex = queue.dequeue()
        result += str(vertex)
        print(str(vertex) + " ", end="")

        # If not visited, mark as visited and enqueue it
        temp = g.array[vertex].get_head()
        while temp:
            visited.add(temp)
            queue.enqueue(temp)
            temp = temp.next_element

    return result

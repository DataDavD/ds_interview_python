from typing import List

from ds_coding_interviews_in_python.ch3linkedlists.linkedlist import LinkedList


class Graph:
    def __init__(self, vertices: int):
        # Total number of vertices
        self.vertices: int = vertices
        # Defining a list which can hold mutliple Linked Lists
        # equal to the number of vertices in the graph
        self.array: List[LinkedList] = list()
        # Create a new LinkedList for each vertex/index of the list
        for i in range(vertices):
            temp_list = LinkedList()
            self.array.append(temp_list)

    def print_graph(self) -> None:
        print(">>Adjency List of Directed Graph<<")
        print()
        for i in range(self.vertices):
            print("|", i, end=" | => ")
            temp = self.array[i].get_head()
            while temp:
                print("[", temp.data, end=" | -> ")
                temp = temp.next_element
            print("None")

    def add_edge(self, source, dest):
        if source < self.vertices and dest < self.vertices:
            # Since we are implementing a directed graph, (1,0) is not equal to (0,1)
            self.array[source].insert_at_tail(dest)

            # Uncomment the following line for undirected graph
            # self.array[dest].insert_at_head(source)

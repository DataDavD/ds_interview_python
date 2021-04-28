from ds_coding_interviews_in_python.ch5graphs.graph import Graph

g = Graph(4)
g.add_edge(0, 1)
g.add_edge(0, 2)
print(g.array[0].to_list())
g.add_edge(1, 3)
g.add_edge(2, 3)
g.print_graph()

print(g.array[1].get_head().data)

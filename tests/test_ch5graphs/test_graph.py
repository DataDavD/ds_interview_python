from ds_coding_interviews_in_python.ch5graphs.graph import Graph
from ds_coding_interviews_in_python.ch5graphs.main import bfs


def test_bfs() -> None:
    g = Graph(4)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 3)
    assert bfs(g, 0) == "0213"

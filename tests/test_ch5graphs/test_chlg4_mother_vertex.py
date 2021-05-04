from ds_coding_interviews_in_python.ch5graphs.chlg4_mother_vertex import mother_vertex_naive
from ds_coding_interviews_in_python.ch5graphs.graph import Graph


def test_mother_vertex_naive() -> None:
    g = Graph(4)
    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(3, 0)
    g.add_edge(3, 1)
    assert mother_vertex_naive(g) == 0

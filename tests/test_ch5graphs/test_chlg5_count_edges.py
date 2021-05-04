from ds_coding_interviews_in_python.ch5graphs.chlg5_count_edges import (
    num_edges_iter,
    num_edges_list_compr,
)
from ds_coding_interviews_in_python.ch5graphs.graph import Graph


def test_num_edges_iter_1() -> None:
    g = Graph(9)
    g.add_edge(0, 2)
    g.add_edge(0, 5)
    g.add_edge(2, 3)
    g.add_edge(2, 4)
    g.add_edge(5, 3)
    g.add_edge(5, 6)
    g.add_edge(3, 6)
    g.add_edge(6, 7)
    g.add_edge(6, 8)
    g.add_edge(6, 4)
    g.add_edge(7, 8)
    g.print_graph()
    assert num_edges_iter(g) == 5


def test_num_edges_iter_2() -> None:
    g2 = Graph(7)
    g2.add_edge(1, 2)
    g2.add_edge(1, 3)
    g2.add_edge(3, 4)
    g2.add_edge(3, 5)
    g2.add_edge(2, 5)
    g2.add_edge(2, 4)
    g2.add_edge(4, 6)
    g2.add_edge(4, 5)
    g2.add_edge(6, 5)
    assert num_edges_iter(g2) == 4


def test_num_edges_list_comp_1() -> None:
    g = Graph(9)
    g.add_edge(0, 2)
    g.add_edge(0, 5)
    g.add_edge(2, 3)
    g.add_edge(2, 4)
    g.add_edge(5, 3)
    g.add_edge(5, 6)
    g.add_edge(3, 6)
    g.add_edge(6, 7)
    g.add_edge(6, 8)
    g.add_edge(6, 4)
    g.add_edge(7, 8)
    g.print_graph()
    assert num_edges_list_compr(g) == 5


def test_num_edges_compr_2() -> None:
    g2 = Graph(7)
    g2.add_edge(1, 2)
    g2.add_edge(1, 3)
    g2.add_edge(3, 4)
    g2.add_edge(3, 5)
    g2.add_edge(2, 5)
    g2.add_edge(2, 4)
    g2.add_edge(4, 6)
    g2.add_edge(4, 5)
    g2.add_edge(6, 5)
    assert num_edges_list_compr(g2) == 4

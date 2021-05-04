from ds_coding_interviews_in_python.ch5graphs.chlg6_path_exists import path_exists
from ds_coding_interviews_in_python.ch5graphs.graph import Graph


def test_path_exist_true() -> None:
    g1 = Graph(9)
    g1.add_edge(0, 2)
    g1.add_edge(0, 5)
    g1.add_edge(2, 3)
    g1.add_edge(2, 4)
    g1.add_edge(5, 3)
    g1.add_edge(5, 6)
    g1.add_edge(3, 6)
    g1.add_edge(6, 7)
    g1.add_edge(6, 8)
    g1.add_edge(6, 4)
    g1.add_edge(7, 8)
    assert path_exists(g1, 0, 7) is True


def test_path_exist_false() -> None:
    g2 = Graph(4)
    g2.add_edge(0, 1)
    g2.add_edge(1, 2)
    g2.add_edge(1, 3)
    g2.add_edge(2, 3)
    assert path_exists(g2, 3, 0) is False

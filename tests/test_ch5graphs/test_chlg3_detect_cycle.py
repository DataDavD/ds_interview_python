from ds_coding_interviews_in_python.ch5graphs.chlg3_detect_cycle import detect_cycle
from ds_coding_interviews_in_python.ch5graphs.graph import Graph


def test_detect_cyle_true() -> None:
    g_cycle = Graph(4)
    g_cycle.add_edge(0, 1)
    g_cycle.add_edge(1, 2)
    g_cycle.add_edge(1, 3)
    g_cycle.add_edge(3, 0)
    assert detect_cycle(g_cycle) is True


def test_detect_cyle_false() -> None:
    g_non_cycle = Graph(3)
    g_non_cycle.add_edge(0, 1)
    g_non_cycle.add_edge(1, 2)
    assert detect_cycle(g_non_cycle) is False

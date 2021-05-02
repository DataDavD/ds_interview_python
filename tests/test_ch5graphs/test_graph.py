from ds_coding_interviews_in_python.ch5graphs.graph import Graph
from ds_coding_interviews_in_python.ch5graphs.main import (
    bfs,
    bfs_simple,
    bfs_simple_dict,
    dfs_simple_dict,
)


def test_bfs_simple() -> None:
    g = Graph(4)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 3)
    assert bfs_simple(g, 0) == "0123"


def test_bfs_simple_empty() -> None:
    g = Graph(0)
    assert bfs_simple(g, 0) == ""


def test_bfs() -> None:
    g = Graph(4)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 3)
    assert bfs(g, 0) == "0123"


def test_bfs_empty() -> None:
    g = Graph(0)
    assert bfs(g, 0) == ""


# Test file has been having issues with internal Black bugs
# so for time being all code below has Black formatting turned off
# fmt: off
def test_dfs_simple_dict_sets() -> None:
    # fmt: off
    graph = {
        "A": {"B", "C"},
        "B": {"D", "E"},
        "C": {"F"},
        "D": set(),
        "E": {"F"},
        "F": {"G"},
        "G": set()
    }
    visited, path = dfs_simple_dict(graph, "A")
    assert path == "ABEFGDC" or "ACFGBED"


def test_dfs_simple_dict_lists() -> None:
    # fmt: off
    graph = {
        "A": ["B", "C"],
        "B": ["D", "E"],
        "C": ["F"],
        "D": list(),
        "E": ["F"],
        "F": ["G"],
        "G": list()
    }
    visited, path = dfs_simple_dict(graph, "A")
    assert path == "ABEFGDC" or "ACFGBED"


def test_dfs_simple_dict_empty() -> None:
    graph = dict()
    visited, path = dfs_simple_dict(graph, "A")
    assert path == ""


def test_bfs_simple_dict_empty() -> None:
    graph = dict()
    assert bfs_simple_dict(graph, "A") == "graph is empty"


def test_bfs_simple_dict() -> None:
    # fmt: off
    graph = {
        "A": ["B", "C"],
        "B": ["D", "E"],
        "C": ["F"],
        "D": [],
        "E": ["F"],
        "F": []
    }
    assert bfs_simple_dict(graph, "A") == "ABCDEF"

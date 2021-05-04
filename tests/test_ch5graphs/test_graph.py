from typing import Any, Dict

from ds_coding_interviews_in_python.ch5graphs.graph import Graph
from ds_coding_interviews_in_python.ch5graphs.graph_search import (
    bfs,
    bfs_simple,
    bfs_simple_dict,
    dfs,
    dfs_simple,
    dfs_simple_dict,
    dfs_simple_other,
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


def test_bfs_simple_dict_empty() -> None:
    graph: Dict[Any, Any] = dict()
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
    graph: Dict[Any, Any] = dict()
    visited, path = dfs_simple_dict(graph, "A")
    assert path == ""


def test_dfs_simple_lists() -> None:
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
    visited, path = dfs_simple(graph, "A")
    assert path == "ABEFGDC" or "ACFGBED"


def test_dfs_simple_empty() -> None:
    graph: Dict[Any, Any] = dict()
    visited, path = dfs_simple(graph, "A")
    assert path == ""


def test_dfs() -> None:
    g = Graph(7)
    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 4)
    g.add_edge(2, 5)
    g.add_edge(3, 6)
    assert dfs(g, 0) == "0136254"


def test_dfs_empty() -> None:
    g = Graph(0)
    assert dfs(g, 0) == ""


def test_dfs_simple_other() -> None:
    g = Graph(7)
    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 4)
    g.add_edge(2, 5)
    g.add_edge(3, 6)
    assert dfs_simple_other(g, 0) == "0136254"


def test_dfs_simple_other_empty() -> None:
    g = Graph(0)
    assert dfs_simple_other(g, 0) == ""

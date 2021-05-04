from ds_coding_interviews_in_python.ch5graphs.graph import Graph


def num_edges_iter(g: Graph) -> int:
    """
    Count the number of edges in an undirected Graph. We do this by
    summing up the size of all the adjacency lists of each vertex.
    Time complexity is O(V+E).

    :param g: Graph
    :return: int
        number of unique edges in a graph
    """
    # just sum up the size of all the adjacency lists for each vertex
    result = 0
    for i in range(g.vertices):
        temp = g.array[i].get_head()
        while temp is not None:
            result += 1
            temp = temp.next_element

    # halve the total sum to get the number of edge as it is an undirected graph
    return result // 2


def num_edges_list_compr(g: Graph) -> int:
    """
    Count the number of edges in an undirected Graph. We do this by
    summing up the size of all the adjacency lists of each vertex.
    Time complexity is O(V+E).

    :param g: Graph
    :return: int
        number of unique edges in a graph
    """
    return sum([len(g.array[i]) for i in range(g.vertices)]) // 2

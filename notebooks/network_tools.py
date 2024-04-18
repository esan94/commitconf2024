"""
The provided script includes several functions for generate or analyze networks.

Author: Esteban Sánchez
e-mail: emsg94@gmail.com
"""
from pandas import DataFrame, MultiIndex
from numpy import mean as npmean
from numpy import std as npstd
from numpy import median as npmedian
from networkx import (
    Graph, DiGraph, connected_components, 
    strongly_connected_components, weakly_connected_components, 
    all_pairs_shortest_path_length, eccentricity, density, 
    degree_centrality, in_degree_centrality, out_degree_centrality, 
    betweenness_centrality, closeness_centrality, eigenvector_centrality,
)
from typing import Dict, Union, Optional, List
from heapq import nlargest, nsmallest


def generate_network_relations(dataframe: DataFrame) -> Dict[str, Dict[str, Dict]]:
    """
    Generate network relations based on a DataFrame with a MultiIndex.

    Parameters
    ----------
    dataframe : pd.DataFrame
        DataFrame with a MultiIndex representing relations between nodes.

    Returns
    -------
    Dict[str, Dict[str, Dict]]
        Dictionary containing network relations with nodes as keys and attributes as values.

    Raises
    ------
    TypeError
        If the `dataframe` index is not a MultiIndex.

    Examples
    --------
    >>> import pandas as pd
    >>> df = pd.DataFrame(
    ...     {
    ...         'Node1': ['A', 'A', 'B'],
    ...         'Node2': ['B', 'C', 'C'],
    ...         'Attribute': [1, 2, 3]
    ...     }
    ... )
    >>> df.set_index(['Node1', 'Node2'], inplace=True)
    >>> generate_network_relations(df)
    {
        'A': {
            'B': {'Attribute': 1},
            'C': {'Attribute': 2}
        },
        'B': {
            'C': {'Attribute': 3}
        }
    }

    Notes
    -----
    - The function assumes that the DataFrame's index represents the relations between nodes using a MultiIndex.
    - All columns in the DataFrame will be considered as attributes for the relations.
    - The generated network relations are returned as a nested dictionary structure.
    """
    if not isinstance(dataframe.index, MultiIndex):
        raise TypeError((
            "To create a network is mandatory to have relation between nodes. "
            "Please provide the relations as a multiindex index in the `dataframe` argument. "
            "All columns will be attributes for the relations."
        ))
    network_relations_aux = dataframe.to_dict(orient="index")
    attributes = dataframe.columns
    network_relations = {}
    for key, value in network_relations_aux.items():
        if key[0] in network_relations.keys():
            network_relations[key[0]][key[1]] = {
                att_name: value.get(att_name) for att_name in attributes
            }
        else:
            network_relations[key[0]] = {
                key[1]: {
                    att_name: value.get(att_name) for att_name in attributes
                    }
                }
    del network_relations_aux
    return network_relations


def create_subgraph_by_filter_edge_att(graph: Union[Graph, DiGraph], is_mt: bool=True, graph_type: str="undirect", **kwargs) -> Union[Graph, DiGraph]:
    """
    Create a subgraph by filtering the edges of a graph based on the specified attributes.

    Parameters
    ----------
    graph : nx.Graph or nx.DiGraph
        The input graph.
    is_mt : bool, optional
        Flag indicating whether the comparison operator for filtering should be '>=' (True) or '<=' (False).
        Default is True.
    graph_type : str, optional
        The type of the output graph. Possible values are 'direct' for directed graph or 'undirect' for undirected graph.
        Default is 'undirect'.
    **kwargs
        The attribute-value pairs used to filter the graph edges. Multiple attribute-value pairs can be passed.

    Returns
    -------
    nx.Graph or nx.DiGraph
        A subgraph containing only the edges that satisfy the specified attribute conditions.

    Raises
    ------
    ValueError
        If no attribute-value pairs are provided to filter the graph.
        If an invalid value is provided for the `graph_type` parameter.

    Examples
    --------
    Suppose we have the following undirected graph `G`:

    >>> import networkx as nx
    >>> G = nx.Graph()
    >>> G.add_edge('A', 'B', weight=3)
    >>> G.add_edge('A', 'C', weight=2)
    >>> G.add_edge('B', 'C', weight=3)
    >>> G.add_edge('C', 'D', weight=5)

    We can use the `create_subgraph_by_filter_edge_att` function to create a subgraph based on attribute filtering:

    >>> subgraph = create_subgraph_by_filter_edge_att(G, weight=3, graph_type="direct")
    >>> print(subgraph.edges())

    [('A', 'B'), ('B', 'C')]

    Notes
    -----
    - The function creates a subgraph from the input graph by filtering the edges based on the specified attribute conditions.
    - The `is_mt` flag determines the comparison operator to use for filtering. If True, '>=' is used; otherwise, '<=' is used.
    - The attribute-value pairs are passed as keyword arguments, where the attribute name is specified as the keyword,
      and the value is the desired condition for filtering.
    - The resulting subgraph contains only the edges that satisfy all the specified attribute conditions.
    - The `graph_type` parameter determines the type of the output graph. It can be set to 'direct' for a directed graph
      or 'undirect' for an undirected graph. By default, it is set to 'undirect'.
    """
    if not len(kwargs):
        raise ValueError((
            "Please provide any attribute to filter the graph. "
            "Pass the arguments through **kwargs arguments."
        ))
    logic_operator = ">=" if is_mt else "<="
    conditions = [
        f"(att.get('{att_name}') {logic_operator} {att_value})" for att_name, att_value in kwargs.items()
        ]
    filtered_edges = [
        (nfrom, nto, att) for nfrom, nto, att in graph.edges(data=True) if eval(' and '.join(conditions))
        ]
    if graph_type == "direct":
        output = DiGraph(incoming_graph_data=filtered_edges)
    elif graph_type == "undirect":
        output = Graph(incoming_graph_data=filtered_edges)
    else:
        raise ValueError((
            f"You have passed graph_type={graph_type} and the possible values are 'direct' or 'undirect'."
        ))
    return output


def get_k_connected_components(network: Union[Graph, DiGraph], k: int, k_type: str="largest", connection_type: Optional[str]=None) -> List[set]:
    """
    Get the k largest or smallest connected components in a graph.

    Parameters
    ----------
    network : Graph or DiGraph
        The input graph.
    k : int
        The number of connected components to retrieve.
    k_type : str, optional
        The type of connected components to retrieve. Possible values are 'largest' or 'smallest'.
        Default is 'largest'.
    connection_type : str, optional
        The type of connection to consider for directed graphs. Possible values are 'strong' or 'weak'.
        This parameter is only applicable when the input graph is a directed graph (DiGraph).
        Default is None.

    Returns
    -------
    List[set]
        A list of sets representing the k largest or smallest connected components in the graph.

    Raises
    ------
    ValueError
        If an invalid value is provided for the `k_type` parameter.
        If the input graph is a directed graph (DiGraph) and the `connection_type` parameter is not specified
        or has an invalid value.

    Examples
    --------
    Suppose we have the following undirected graph `G`:

    >>> import networkx as nx
    >>> G = nx.Graph()
    >>> G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 5)])
    >>> G.add_edges_from([(6, 7), (7, 8), (8, 9)])
    >>> G.add_edges_from([(10, 11), (11, 12)])

    We can use the `get_k_connected_components` function to retrieve the two largest connected components:

    >>> largest_components = get_k_connected_components(G, k=2, k_type="largest")
    >>> for component in largest_components:
    ...     print(component)

    {1, 2, 3, 4, 5}
    {6, 7, 8, 9}

    Notes
    -----
    - The function retrieves the k largest or smallest connected components in the input graph.
    - The `network` parameter can be an undirected graph (Graph) or a directed graph (DiGraph).
    - The `k` parameter specifies the number of connected components to retrieve.
    - The `k_type` parameter determines whether to retrieve the largest or smallest connected components.
      It can be set to 'largest' or 'smallest'. By default, it is set to 'largest'.
    - For undirected graphs (Graph), the connected components are determined using `connected_components` function.
    - For directed graphs (DiGraph), the `connection_type` parameter must be specified to determine the type of connection.
      It can be set to 'strong' for strongly connected components or 'weak' for weakly connected components.
      By default, it is set to None.
    - The function returns a list of sets, where each set represents the connected components.
    - The connected components are sorted based on their size, either in descending order (largest) or ascending order (smallest).
    """
    if k_type == "largest":
        top_func = nlargest
    elif k_type == "smallest":
        top_func = nsmallest
    else:
        raise ValueError((
            f"You have passed k_type={k_type} and the possible values are 'largest' or 'smallest'."
        ))
    if network.is_directed():
        if connection_type is None:
            raise ValueError((
                "When the network is DiGraph you have to specify one of "
                "the following `connection_type`: 'strong' or 'weak'."
            ))
        elif connection_type == "strong":
            components_func = strongly_connected_components
        elif connection_type == "weak":
            components_func = weakly_connected_components
        else:
            raise ValueError((
                f"You have passed connection_type={connection_type} "
                "and the possible values are 'strong' or 'weak'. "
                "This argument is used only when the network is directed."
            ))
    else:
        components_func = connected_components
    
    return top_func(n=k, iterable=components_func(network), key=len)


def get_basic_statistics(network: Union[Graph, DiGraph]) -> dict:
    """
    Compute basic statistics for the input graph.

    Parameters
    ----------
    network : nx.Graph or nx.DiGraph
        The input graph.

    Returns
    -------
    dict
        A dictionary containing the basic statistics of the graph.

    Examples
    --------
    Suppose we have the following undirected graph `G`:

    >>> import networkx as nx
    >>> G = nx.Graph()
    >>> G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 5)])

    We can use the `get_basic_statistics` function to compute the basic statistics of the graph:

    >>> statistics = get_basic_statistics(G)
    >>> print(statistics)

    {
        'graph_type': 'undirect',
        'num_nodes': 5,
        'num_edges': 4,
        'density': 0.4,
        'centrality': {1: 0.25, 2: 0.5, 3: 0.5, 4: 0.5, 5: 0.25},
        'ncn': [2, 3, 3, 3, 2],
        'mean_ncn': 2.6,
        'median_ncn': 3.0,
        'max_ncn': 3,
        'min_ncn': 2,
        'std_ncn': 0.4898979485566356,
        'mean_sp': [1.5, 1.0, 1.0, 1.0, 1.5],
        'mean_net_sp': 1.2,
        'diameter': 2,
        'betweeness_centrality': {1: 0.0, 2: 0.0, 3: 0.0, 4: 0.0, 5: 0.0},
        'closeness_centrality': {1: 0.625, 2: 0.8333333333333334, 3: 0.8333333333333334, 4: 0.8333333333333334, 5: 0.625},
        'eig_centrality': {1: 0.27195717623444435, 2: 0.4679223045021113, 3: 0.4679223045021113, 4: 0.4679223045021113, 5: 0.27195717623444435}
    }

    Notes
    -----
    - The function computes basic statistics for the input graph, including graph type, number of nodes, number of edges,
      density, centrality measures, node closeness, shortest path statistics, diameter, and betweenness centrality.
    - The `network` parameter can be an undirected graph (Graph) or a directed graph (DiGraph).
    - The function returns a dictionary containing the computed statistics.
    """
    graph_type = "direct" if network.is_directed() else "undirect"
    summary_dict = {
        "graph_type": graph_type,
        "num_nodes": network.number_of_nodes(),
        "num_edges": network.number_of_edges(),
        "density": density(network),
    }
    degrees = [("", network.degree())] if graph_type == "undirect" else [
        ("", network.degree()), ("_in", network.in_degree()), ("_out", network.out_degree())
    ]
    degrees_centrality = [("", degree_centrality(network))] if graph_type == "undirect" else [
        ("", degree_centrality(network)), 
        ("_in", in_degree_centrality(network)), 
        ("_out", out_degree_centrality(network))
    ]
    for centrality_suffix, d_centrality in degrees_centrality:
        summary_dict[f"centrality{centrality_suffix}"] = d_centrality
    for degree_suffix, degree in degrees:
        number_close_nodes = [ncn for _, ncn in degree]
        summary_dict[f"ncn{degree_suffix}"] = number_close_nodes
        summary_dict[f"mean_ncn{degree_suffix}"] = npmean(number_close_nodes)
        summary_dict[f"median_ncn{degree_suffix}"] = npmedian(number_close_nodes)
        summary_dict[f"max_ncn{degree_suffix}"] = max(number_close_nodes)
        summary_dict[f"min_ncn{degree_suffix}"] = min(number_close_nodes)
        summary_dict[f"std_ncn{degree_suffix}"] = npstd(number_close_nodes)
        summary_dict[f"mean_ncn{degree_suffix}"] = npmean(number_close_nodes)
    shorter_paths = dict(all_pairs_shortest_path_length(network))
    mean_shorter_paths = [
        npmean(list(filter(lambda e: e!=0, sp_values.values()))) for sp_values in shorter_paths.values()
    ]
    summary_dict["sp"] = shorter_paths
    summary_dict["mean_sp"] = mean_shorter_paths
    summary_dict["mean_net_sp"] = npmean(mean_shorter_paths)
    summary_dict["diameter"] = max(eccentricity(network, sp=shorter_paths).values())
    summary_dict["betweeness_centrality"] = betweenness_centrality(network)
    summary_dict["closeness_centrality"] = closeness_centrality(network)
    summary_dict["eig_centrality"] = eigenvector_centrality(network)
    return summary_dict

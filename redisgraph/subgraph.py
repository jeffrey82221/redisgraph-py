from itertools import chain
from .node import Node
from .edge import Edge

class Subgraph:
    """
    A subgraph = nodes + edges 
    """
    def __init__(self, nodes=None, edges=None):
        """
        Create subgraph
        """
        if nodes:
            if not isinstance(nodes, list):
                raise TypeError("nodes must be list")
                
        if edges:
            if not isinstance(nodes, list):
                raise TypeError("edges must be list")

        self._nodes = frozenset(nodes or [])
        self._edges = frozenset(edges or [])
        self._nodes |= frozenset(chain.from_iterable(e.nodes for e in self._edges))
        
    def __str__(self):
        res = 'Nodes:\n'
        nodes_res = []
        for n in self._nodes:
            nodes_res.append(str(n))
        res += ",".join(nodes_res)
        res += '\nEdges:\n'
        edges_res = []
        for e in self._edges:
            edges_res.append(str(e))
        res += ",".join(edges_res)
        return res

    def __eq__(self, rhs):
        return self.nodes() == rhs.nodes() and self.edges() == rhs.edges()

from itertools import chain

class Subgraph:
    """
    A subgraph = nodes + edges 
    """
    def __init__(self, nodes=None, edges=None):
        """
        Create subgraph
        """
        if nodes:
            if not (isinstance(nodes, list) or isinstance(nodes, set) or isinstance(nodes, frozenset)):
                raise TypeError("nodes must be list, set, or frozenset")
                
        if edges:
            if not (isinstance(edges, list) or isinstance(edges, set) or isinstance(edges, frozenset)):
                raise TypeError("edges must be list, set, or frozenset")

        self._nodes = frozenset(nodes or [])
        self._edges = frozenset(edges or [])
        self._nodes |= frozenset(chain.from_iterable(e.nodes() for e in self._edges))
    
    def nodes(self):
        return self._nodes

    def edges(self):
        return self._edges

    def nodes_count(self):
        return len(self._nodes)

    def edge_count(self):
        return len(self._edges)

    def labels(self):
        """ Return the set of all node labels in this subgraph.
        """
        return frozenset(chain.from_iterable(node.labels for node in self._nodes))

    def relations(self):
        """ Return the set of all edge relations in this subgraph.
        """
        return frozenset(e.relation for e in self._edges)

    def __str__(self):
        res = ''
        if self._nodes:
            res += 'Nodes:\n'
            nodes_res = []
            for n in self._nodes:
                nodes_res.append(str(n))
            res += ",".join(nodes_res)
        if self._edges:
            res += '\nEdges:\n'
            edges_res = []
            for e in self._edges:
                edges_res.append(str(e))
            res += ",".join(edges_res)
        return res

    def __eq__(self, rhs):
        return self.nodes() == rhs.nodes() and self.edges() == rhs.edges()

    def __hash__(self):
        value = 0
        for n in self.nodes():
            value ^= hash(n)
        for e in self.edges():
            value ^= hash(e)
        return value

    def __or__(self, rhs):
        return Subgraph(set(self.nodes()) | set(rhs.nodes()), set(self.edges()) | set(rhs.edges()))
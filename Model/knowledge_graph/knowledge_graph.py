"""
Add nodes.
Add edges.
Remove nodes.
Remove edges.
Retrieve nodes by ID.
Retrieve edges by ID.
"""
import networkx as nx
from edge import Edge
from node import Node
from errors import *

class KnowledgeGraph:
    def __init__(self):
        self.graph = nx.DiGraph()
    def add_node(self, node):
        if not isinstance(node, Node): raise ValueError(f"Argument 2 expected instance of 'Node' got '{type(node)}'")
        if self.retrieve_node(node.id): raise DuplicateNodeError("Failed to create node. Node with the same ID already exists!")
        self.graph.add_node(node.id, attr=node)
    def remove_node(self, node_id):
        self.graph.remove_node(node_id)
    def retrieve_node(self, node_id):
        node = self.graph.nodes.get(node_id)
        return node and node["attr"] or None

    def add_edge(self, edge):
        if not isinstance(edge, Edge): raise TypeError(f"Argument 2 expected instance of 'Edge' got '{type(edge)}'")
        if not self.retrieve_node(edge.source_node_id) or not self.retrieve_node(edge.target_node_id): 
            msg = f"To create an edge, both nodes must exist. Invalid nodeId: {not self.retrieve_node(edge.source_node_id) and edge.source_node_id or edge.target_node_id}"
            raise NodeNotFoundError(msg)
        if self.retrieve_edge(edge.source_node_id, edge.target_node_id): raise DuplicateEdgeError(f"Edge between '{edge.source_node_id}' and '{edge.target_node_id}' already exists!")
        self.graph.add_edge(edge.source_node_id, edge.target_node_id, attr=edge)
    def remove_edge(self, source_node_id=None, target_node_id=None, edge_id=None):
        if edge_id:
            return
        if source_node_id == None or target_node_id == None: raise ValueError("Must provide either a source AND target node OR an edge id!")
        if self.retrieve_node(source_node_id) == None or self.retrieve_node(target_node_id) == None: raise NodeNotFoundError(f"Failed to find either {source_node_id} or {target_node_id}!")
        if self.retrieve_edge(source_node_id=source_node_id, target_node_id=target_node_id) == None: raise EdgeNotFoundError(f"Failed to find edge connecting {source_node_id} and {target_node_id}")

        self.graph.remove_edge(source_node_id, target_node_id)
        return
    def retrieve_edge(self, source_node_id=None, target_node_id=None, edge_id=None):
        if source_node_id and self.retrieve_node(source_node_id) and target_node_id and self.retrieve_node(target_node_id):
            edge = self.graph.edges[source_node_id, target_node_id]
            return edge and edge["attr"]
        elif edge_id:
            return
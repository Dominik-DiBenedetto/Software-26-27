import networkx as nx
from knowledge_graph import KnowledgeGraph
from edge import Edge
from node import Node

"""
Unique node IDs - Duplicates
Valid edge endpoints - Ensure edge node endpoints exist
Valid relationship types - check relationship types
No invalid self-referencing edges - make sure things arent depending on/referencing themselves
No prerequisite cycles - make sure if a is prereq of b that b isnt pre req of a
"""

class GraphValidator:
    def __init__(self, graph: KnowledgeGraph):
        if not isinstance(graph, KnowledgeGraph): raise TypeError("Graph must be of type KnowledgeGraph")
        self.graph = graph
    def check_duplicate_nodes(self):
        pass
    def validate_edge_endpoints(self):
        pass
    def validate_relationship_types(self):
        pass
    def check_self_referencing(self):
        pass
    def check_prereq_cycles(self):
        pass
    def validate_all(self):
        self.check_duplicate_nodes()
        self.validate_edge_endpoints()
        self.validate_relationship_types()
        self.check_self_referencing()
        self.check_prereq_cycles()


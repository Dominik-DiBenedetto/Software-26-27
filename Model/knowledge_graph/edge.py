""" 
A relationship between two nodes.
"""
import dataclasses
from enums import relationship_type

@dataclasses.dataclass
class Edge:
    source_node_id: str
    target_node_id: str
    description: str
    relationship: relationship_type.RelationshipType
    conditions: list
    equation: str
    metadata: dict
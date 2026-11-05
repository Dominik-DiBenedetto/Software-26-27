"""
This file will be used to manually create my first knowledge graph. It will
cover basic kinematics.
"""

from knowledge_graph import KnowledgeGraph
from node import Node
from edge import Edge
from enums import category, relationship_type

KG = KnowledgeGraph()

node1 = Node("KIN_POSITION", "Position", 
"The location of an object in space.",
category.Category.KINEMATICS, [], [], 1, {})

edge1 = Edge("KIN_POSITION", "KIN_DISPLACEMENT", "Relates position to displacement",
relationship_type.RelationshipType.PREREQUISITE, [],"",{})

node2 = Node("KIN_DISPLACEMENT", "Displacement", 
"The net change in position of an object, measured as the shortest straight-line distance from its initial position to its final position, along with a specific direction.",
category.Category.KINEMATICS, [], [], 1, {})

edge2 = Edge("KIN_DISPLACEMENT", "KIN_VELOCITY", "Relates displacement to velocity",
relationship_type.RelationshipType.PREREQUISITE, [],"",{})

node3 = Node("KIN_VELOCITY", "Velocity", 
"The change of displacement over time; the first derivative of position.",
category.Category.KINEMATICS, ["velocity = displacement / time"], [], 1, {})

KG.add_node(node1)
KG.add_node(node2)
KG.add_node(node3)
KG.add_edge(edge1)
KG.add_edge(edge2)

predecessors = KG.get_predecessors("KIN_VELOCITY")
print(predecessors)

outgoing_edges = KG.get_outgoing_edges("KIN_DISPLACEMENT")
print(outgoing_edges)
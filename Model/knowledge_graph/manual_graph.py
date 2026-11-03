"""
This file will be used to manually create my first knowledge graph. It will
cover basic kinematics.
"""

from knowledge_graph import KnowledgeGraph
from node import Node
from edge import Edge
from enums import category, relationship_type

KG = KnowledgeGraph()

node1 = Node("KIN_DISPLACEMENT", "Displacement", 
"The net change in position of an object, measured as the shortest straight-line distance from its initial position to its final position, along with a specific direction.",
category.Category.KINEMATICS, [], [], 1, {})

edge = Edge("KIN_DISPLACEMENT", "KIN_VELOCITY", "Relates displacement to velocity",
relationship_type.RelationshipType.PREREQUISITE, [],"",{})

node2 = Node("KIN_VELOCITY", "Velocity", 
"The change of displacement over time; the first derivative of position.",
category.Category.KINEMATICS, ["velocity = displacement / time"], [], 1, {})

KG.add_node(node1)
KG.add_node(node2)
KG.add_edge(edge)

print(KG.graph.nodes())

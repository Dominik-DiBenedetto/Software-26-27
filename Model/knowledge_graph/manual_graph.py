"""
This file will be used to manually create my first knowledge graph. It will
cover basic kinematics.
"""

import networkx as nx
G = nx.Graph()

nodes = [
    (1, {
        "concept": "speed",
        "definition": "the first derivative of position.",
        "related_equations": ["f'(x)", "distance/time", "displacement/time", "d/t"],
        "prerequisites": ["distance vs displacement", ]
    })
]

G.add_nodes_from(nodes)
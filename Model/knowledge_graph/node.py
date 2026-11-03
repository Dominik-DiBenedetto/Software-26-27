"""
Node - an individual concept
Node should contain:
    Concept name.
    Definition.
    Relevant equations.
    Prerequisite concepts.
    Common misconceptions.
    Examples.
"""
import uuid, dataclasses
from enums.category import Category

@dataclasses.dataclass
class Node:
    id: str
    name: str
    definition: str
    category: Category
    equations: [str]
    examples: [str]
    difficulty: int
    metadata: dict
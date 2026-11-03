import enum

class RelationshipType(enum.Enum):
    PREREQUISITE = enum.auto()
    DERIVED_FROM = enum.auto()
    CAUSES = enum.auto()
    PROPORTIONAL_TO = enum.auto()
    INVERSELY_PROPORTIONAL_TO = enum.auto()
    PART_OF = enum.auto()
    CONTRASTS_WITH = enum.auto()

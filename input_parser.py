# The input file must respect the expected structure and syntax:
# • The first line must define the number of drones using nb_drones: <positive_integer>.
# • The program must be able to handle any number of drones.
# • There must be exactly one start_hub: zone and one end_hub: zone.
# • Each zone must have a unique name and valid integer coordinates.
# • Zone names can use any valid characters except dashes and spaces.


# • Connections must link only previously defined zones using connection: <zone1>-<zone2>
# [metadata].

# • The same connection must not appear more than once (e.g., a-b and b-a are con-
# sidered duplicates).

# • Any metadata block (e.g., [zone=... color=...] for zones, [max_link_capacity=...]
# for connections) must be syntactically valid.

# • Zone types must be one of: normal, blocked, restricted, priority. Any invalid
# type must raise a parsing error.

# • Capacity values (max_drones for zones, max_link_capacity for connections) must
# be positive integers.

# • The max_drones capacity is ignored on the start_hub and end_hub zones: these
# have no capacity limit (all drones may start in the start zone, and any number of
# drones may be delivered to the end zone). If such metadata is present on those two
# zones, it is ignored and is not a validation error.

# • Any other parsing error must stop the program and return a clear error message
# indicating the line and cause.

# The first line defines the number of drones using nb_drones: <number>.

# • Zone definition on each line using type prefixes:
# ◦ start_hub: <name> <x> <y> [metadata] marks the starting zone.
# ◦ end_hub: <name> <x> <y> [metadata] marks the end zone.
# ◦ hub: <name> <x> <y> [metadata] defines a regular zone.
# ◦ The connection syntax forbids dashes in zone names (see below).

# • All metadata is optional and enclosed in brackets [...] with default values:
# ◦ zone=<type> (default: normal)
# ◦ color=<value> (default: none)
# ◦ max_drones=<number> (default: 1) - Maximum drones that can occupy this
# zone simultaneously
# ◦ Tags inside brackets can appear in any order.

# • Zone types:
# ◦ normal – Standard zone with 1 turn movement cost (default)
# ◦ blocked – Inaccessible zone. Drones must not enter or pass through this zone.
# Any path using it is invalid.
# ◦ restricted – A sensitive or dangerous zone. Movement to this zone costs 2
# turns.
# ◦ priority – A preferred zone. Movement to this zone costs 1 turn but should
# be prioritized in pathfinding.

# • Colors:
# ◦ Colors are optional and can be used for visual representation (terminal output
# or graphical display).
# ◦ Accepted values for color are any valid single-word strings (e.g., red, blue,
# gray). There is no fixed list of allowed colors.
# ◦ When colors are specified, the implementation should provide visual feedback
# through colored terminal output or graphical representation.

# • Connections are defined using connection: <name1>-<name2> [metadata]:
# ◦ Define a bidirectional connection (edge) between two zones.
# ◦ The connection syntax forbids dashes in zone names.
# ◦ Optional metadata can be specified in brackets [...]:
# ∗ max_link_capacity=<number> (default: 1) - Maximum drones that can
# traverse this connection simultaneously
# Comments start with ’#’ and are ignored.


# Include docstrings in functions and classes following PEP 257 
# to document purpose, parameters, and returns.

import readline
import sys
from contextlib import contextmanager
from collections.abc import Generator
from typing import IO, Any


@contextmanager
def read_input(file: str, mode: str) -> Generator[IO[Any], None]:
    f: IO[Any] = open(file, mode)
    try:
        yield f
    finally:
        f.close()


def parse_file(file: str) -> None:
    with read_input(file, 'r') as r:
        lines = r.readlines()
    print(lines)
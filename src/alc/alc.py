from collections import deque
from dataclasses import dataclass, field
import sys

@dataclass
class Node:
    neighbors: set[int] = field(default_factory=set)

class NodeGraph:
    def __init__(self, size: int) -> None:
        self.nodes: list[Node] = [Node() for _ in range(size)]
        self.size = size

    def add_binding(self, first_index: int, second_index: int) -> None:
        self.nodes[first_index].neighbors.add(second_index)
        self.nodes[second_index].neighbors.add(first_index)

    def add_bindings(self, first_index: int, second_indexes: list[int] | set[int]) -> None:
        for second_index in second_indexes:
            self.add_binding(first_index, second_index)

    def remove_binding(self, first_index: int, second_index: int) -> None:
        self.nodes[first_index].neighbors.discard(second_index)
        self.nodes[second_index].neighbors.discard(first_index)

    def remove_bindings(self, first_index: int, second_indexes: list[int] | set[int]) -> None:
        for second_index in second_indexes:
            self.remove_binding(first_index, second_index)

def get_missing_nodes_on_bfs_path(first_particle: NodeGraph) -> list[int]:
    queue = deque()
    visited = [False] * first_particle.size
    visit_order: list[int] = []

    visited[0] = True
    queue.append(0)
    while queue:
        current_index = queue.popleft()
        for node_index in first_particle.nodes[current_index].neighbors:
            if not visited[node_index]:
                visited[node_index] = True
                queue.append(node_index)
                if node_index not in first_particle.nodes[0].neighbors:
                    visit_order.append(node_index)
    return visit_order

def solve(first_particle: NodeGraph, second_particle: NodeGraph) -> None:
    sum_of_changes: int = 0

    leader_node_0_bindings_added: list[int] = get_missing_nodes_on_bfs_path(first_particle)
    sum_of_changes += len(leader_node_0_bindings_added)
    first_particle.add_bindings(0, leader_node_0_bindings_added)

    first_particle_bindings_added: list[set[int]] = []
    for index in range(1, first_particle.size):
        need_to_be_added: set[int] = second_particle.nodes[index].neighbors.difference(first_particle.nodes[index].neighbors)
        need_to_be_added.discard(index)
        sum_of_changes += len(need_to_be_added)
        first_particle_bindings_added.append(need_to_be_added)
        first_particle.add_bindings(index, need_to_be_added)

    first_particle_bindings_removed: list[set[int]] = []
    for index in range(1, first_particle.size):     
        need_to_be_removed: set[int] = first_particle.nodes[index].neighbors.difference(second_particle.nodes[index].neighbors)
        # Node 0 was choosen as leader so it will be removed as last
        need_to_be_removed.discard(0)
        need_to_be_removed.discard(index)
        sum_of_changes += len(need_to_be_removed)
        first_particle_bindings_removed.append(need_to_be_removed)
        first_particle.remove_bindings(index, need_to_be_removed)

    leader_node_0_bindings_removed: set[int] = first_particle.nodes[0].neighbors.difference(second_particle.nodes[0].neighbors)
    leader_node_0_bindings_removed.discard(0)
    sum_of_changes += len(leader_node_0_bindings_removed)
    first_particle.remove_bindings(0, leader_node_0_bindings_removed)

    print(sum_of_changes)
    for binding in leader_node_0_bindings_added:
        print(f"+ 1 {binding + 1}")

    for index, bindings in enumerate(first_particle_bindings_added):
        for binding in bindings:
            print(f"+ {index + 2} {binding + 1}")

    for index, bindings in enumerate(first_particle_bindings_removed):
        for binding in bindings:
            print(f"- {index + 2} {binding + 1}")

    for binding in leader_node_0_bindings_removed:
        print(f"- 1 {binding + 1}")

def main() -> None:
    tokens: list[str] = []
    for line in sys.stdin:
        stripped = line.strip()
        if not stripped: break
        tokens += stripped.split()
    tokens_iter = iter(tokens)

    number_of_atoms: int = int(next(tokens_iter))

    first_particle: NodeGraph = NodeGraph(number_of_atoms)
    first_particle_number_of_bindings: int = int(next(tokens_iter))
    for _ in range(first_particle_number_of_bindings):
        first_atom_index: int = int(next(tokens_iter)) - 1
        second_atom_index: int = int(next(tokens_iter)) - 1
        first_particle.add_binding(first_atom_index, second_atom_index)

    second_particle: NodeGraph = NodeGraph(number_of_atoms)
    second_particle_number_of_bindings: int = int(next(tokens_iter))
    for _ in range(second_particle_number_of_bindings):
        first_atom_index: int = int(next(tokens_iter)) - 1
        second_atom_index: int = int(next(tokens_iter)) - 1
        second_particle.add_binding(first_atom_index, second_atom_index)

    solve(first_particle, second_particle)

if __name__ == "__main__":
    main()
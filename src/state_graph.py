
from dataclasses import dataclass
from typing import List, Dict, Tuple, Optional
from enum import Enum


@dataclass
class Trit:
    value: int  # -1, 0, +1


@dataclass
class Tryte:
    trits: List[Trit]  # 6 trits


@dataclass
class State:
    id: str
    tensor_shape: List[int]
    tryte_data: List[Tryte]
    is_initial: bool = False
    is_target: bool = False
    entropy: float = 0.0


@dataclass
class Edge:
    source: State
    target: State
    operation: str  # ISA M0 instruction
    energy: float = 1.0
    time: float = 1.0
    delta_entropy: float = 0.0


class StateGraph:
    def __init__(self):
        self.states: List[State] = []
        self.edges: List[Edge] = []


    def add_state(self, state: State):
        self.states.append(state)


    def add_edge(self, edge: Edge):
        self.edges.append(edge)


    def get_initial_states(self) -> List[State]:
        return [s for s in self.states if s.is_initial]


    def get_target_states(self) -> List[State]:
        return [s for s in self.states if s.is_target]


    def neighbors(self, state: State) -> List[Tuple[State, Edge]]:
        result = []
        for edge in self.edges:
            if edge.source.id == state.id:
                # Find target state by ID
                for s in self.states:
                    if s.id == edge.target.id:
                        result.append((s, edge))
                        break
        return result

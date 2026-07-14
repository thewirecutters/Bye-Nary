
import heapq
from typing import List, Tuple, Dict, Optional


class TernaryWeight:
    """Trit-weight — energy, time, entropy delta"""
    def __init__(self, e: float = 0, t: float = 0, h: float = 0):
        self.e = e  # energy
        self.t = t  # time
        self.h = h  # entropy delta


    def __lt__(self, other):
        # Lexicographic comparison: energy → time → entropy
        if self.e != other.e:
            return self.e < other.e
        if self.t != other.t:
            return self.t < other.t
        return self.h < other.h


    def __add__(self, other):
        return TernaryWeight(self.e + other.e, self.t + other.t, self.h + other.h)


def a_star_ternary(
    graph: StateGraph,
    start: State,
    target: State,
    heuristic: callable
) -> List[Edge]:
    """A* with ternary weights — energy, time, entropy"""
    open_set = [(TernaryWeight(0, 0, 0), 0, start, [])]
    closed_set = set()
    g_score = {id(start): TernaryWeight(0, 0, 0)}
    
    while open_set:
        current_w, _, current_state, path = heapq.heappop(open_set)
        
        if current_state.id == target.id:
            return path
        
        if current_state.id in closed_set:
            continue
        closed_set.add(current_state.id)
        
        for neighbor, edge in graph.neighbors(current_state):
            new_w = current_w + TernaryWeight(edge.energy, edge.time, edge.delta_entropy)
            h_val = heuristic(neighbor, target)
            total_w = new_w + h_val
            
            if neighbor.id not in g_score or new_w < g_score[neighbor.id]:
                g_score[neighbor.id] = new_w
                new_path = path + [edge]
                heapq.heappush(open_set, (total_w, id(neighbor), neighbor, new_path))
    
    return []  # No path found

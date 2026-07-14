
import re
from dataclasses import dataclass
from typing import List, Dict, Any, Optional


@dataclass
class Tensor:
    shape: List[int]
    data: Optional[List] = None


@dataclass
class Hypervector:
    dims: int


@dataclass
class Constraint:
    name: str
    value: Any


@dataclass
class Target:
    pattern: str
    shape: Optional[List[int]] = None
    confidence: Optional[float] = None


@dataclass
class Field:
    name: str
    input: Any  # Tensor | Hypervector
    weights: Optional[Any] = None
    constraints: List[Constraint] = []
    targets: List[Target] = []


class TernParser:
    def __init__(self):
        self.tokens = []
        self.pos = 0


    def parse(self, code: str) -> Field:
        lines = code.strip().split('\n')
        # Naive but works: find field block
        field_name = None
        input_def = None
        weights_def = None
        constraints = []
        targets = []
        
        # Extract field name
        for line in lines:
            if 'field' in line and '{' in line:
                parts = line.split()
                field_name = parts[1] if len(parts) > 1 else 'unnamed'
                break


        # Find input, weights, constraints, target
        for i, line in enumerate(lines):
            if 'input:' in line:
                shape_str = line.split('(')[1].split(')')[0]
                shape = [int(x.strip()) for x in shape_str.split(',')]
                input_def = Tensor(shape)
            if 'weights:' in line:
                shape_str = line.split('(')[1].split(')')[0]
                shape = [int(x.strip()) for x in shape_str.split(',')]
                weights_def = Tensor(shape)
            if 'constraints:' in line:
                j = i + 1
                while j < len(lines) and '}' not in lines[j]:
                    line_text = lines[j].strip()
                    if ',' in line_text:
                        # Remove trailing comma
                        line_text = line_text.rstrip(',')
                        if ':' in line_text:
                            parts = line_text.split(':')
                            name = parts[0].strip()
                            val = parts[1].strip()
                        else:
                            name = line_text.split()[0] if line_text else 'unnamed'
                            val = True
                        constraints.append(Constraint(name, val))
                    j += 1
            if 'target:' in line:
                # Simple target extraction
                targets.append(Target(pattern='unknown'))


        return Field(
            name=field_name or 'unnamed',
            input=input_def,
            weights=weights_def,
            constraints=constraints,
            targets=targets
        )

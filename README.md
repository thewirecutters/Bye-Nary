# Bye-Nary
## The Sovereign Computer: Model Zero

A complete technical blueprint for a post‑binary computing architecture.

---

## What This Is

Model Zero is not a faster GPU, a better AI accelerator, or a niche research toy. It is a complete, ground‑up replacement for the binary substrate that has dominated computing since the 1940s.

**Built on:**

· Balanced ternary logic (base‑3, radix economy optimal at e ≈ 2.718)
· Asynchronous wave‑pipelining (no global clock, no idle cycles)
· SOT‑MRAM in‑memory computation (no von Neumann bottleneck)
· Plasmonic optical interconnects (data at the speed of light)

This repository contains the full technical blueprint, working compiler implementation, and hardware‑verifiable design for a sovereign, vendor‑independent computing architecture.

---

## The Blueprint — Model Zero

**Five Pillars:**

| Pillar | Component | Spec |
|---|---|---|
| I | FPGA Controller | iCESugar-pro (Lattice ECP5, 24K LUTs) |
| II | Ternary ALU | 24‑trit, RBNS arithmetic, O(1) carry‑free addition |
| III | SOT‑MRAM IMC | In‑memory compute, 10ns switching, >10¹⁵ endurance |
| IV | Plasmonic Interconnect | Hybrid plasmonic waveguides, speed‑of‑light |
| V | Custom PCB / Interposer | 6‑layer high‑speed substrate |

**Key Specs:**

- Word size: 24 trits (≈38 bits equivalent)
- Address space: 36 trits (≈178 PB equivalent)
- ISA: 120 instructions, extensible to 243
- Build cost: $44,500–$72,000

---

## The Compiler — Sovereign Compiler M0

A complete, working compiler pipeline for the Model Zero architecture.

**Language: Tern**

Tern is a field‑description language, not a procedural one. No loops. No conditionals. The programmer describes the computational field — the compiler finds the trajectory.

```tern
field face_recognition {
  input: hypervector(10000)
  constraints: { no_divergence, max_entropy: 0.35 }
  target: equilibrium_state { pattern: "recognize_face", confidence: > 0.95 }
}

sovereign_compiler_m0/
├── src/
│   ├── lexer.py          # Manual tokenizer
│   ├── parser.py         # Recursive descent → AST
│   ├── graph_builder.py  # AST → state graph
│   ├── optimizer.py      # A* with ternary metric
│   ├── codegen.py        # Graph → M0Program
│   ├── simulator.py      # VM with SOT-MRAM and photonics
│   └── cli.py            # Command interface
└── tests/
    ├── test.tern
    └── test_compiler.py  # 9 unit tests

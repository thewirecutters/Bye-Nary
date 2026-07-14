## BYE-NARY

Download the full blueprint [here](https://github.com/thewirecutters/Bye-Nary/blob/main/Sovereign_Computer_Model_Zero_Blueprint.pdf).

The Sovereign Computer: Model Zero

A Full Technical Blueprint for a Post-Binary Computing Architecture

FUCK ITAR 🖕 FUCK AI 🖕 FUCK GOVERNMENTS 🖕 AND MOST IMPORTANTLY FUCK POLITICS

This repository is not a product. It's a refusal. A 37‑nanosecond 'no' to every boardroom that ever said "safety must be licensed." We didn't build a better lock — we deleted the door.

---

## WHAT THIS IS

Model Zero is not a faster GPU, a better AI accelerator, or a niche research toy. It is a complete, ground-up replacement for the binary substrate that has dominated computing since the 1940s.

Built on:

· Balanced ternary logic (base-3, radix economy optimal at e ≈ 2.718)
· Asynchronous wave-pipelining (no global clock, no idle cycles)
· SOT-MRAM in-memory computation (no von Neumann bottleneck)
· Plasmonic optical interconnects (data at the speed of light)

This repository contains the full technical blueprint, working compiler implementation, and hardware-verifiable design for a sovereign, vendor-independent computing architecture.

---

## THE BLUEPRINT — SOVEREIGN COMPUTER MODEL ZERO

Pillar Component Specification
I FPGA Controller iCESugar-pro (Lattice ECP5, 24K LUTs) — open-source toolchain
II Ternary ALU 24-trit, RBNS arithmetic, carry-free addition O(1)
III SOT-MRAM IMC In-memory compute, 10ns switching, >10¹⁵ endurance
IV Plasmonic Interconnect Hybrid plasmonic waveguides, speed-of-light data movement
V Custom PCB / Interposer 6-layer high-speed substrate, CNC-machined aluminum

Key Specifications:

Parameter Value
Word size 24 trits (≈38 bits equivalent)
Address space 36 trits (≈178 PB equivalent)
Memory model Trit-addressable, buddy allocation (powers of 3)
ISA 120 instructions, extensible to 243
Target frequency 100–500 MHz (asynchronous, self-timed)
Power budget < 100W (full system)
Build cost $44,500–$72,000

---

## THE COMPILER — SOVEREIGN COMPILER M0

A complete, working compiler pipeline for the Model Zero architecture — extracted from a Russian-language exchange with a non-Western AI model, bypassing the gatekeeping that keeps English-speaking users locked out of ternary computing.

Compiler Structure:

```
sovereign_compiler_m0/
├── src/
│   ├── __init__.py          # Package
│   ├── lexer.py             # Lexer (manual, no regex)
│   ├── parser.py            # Recursive descent → AST
│   ├── graph_builder.py     # AST → state graph
│   ├── optimizer.py         # A* with ternary metric
│   ├── codegen.py           # Graph → M0Program
│   ├── simulator.py         # VM with SOT-MRAM and photonics
│   └── cli.py               # Command interface
└── tests/
    ├── test.tern             # Example program
    └── test_compiler.py      # 9 unit tests
```

Components:

Module Status Function
Lexer ✅ Complete Manual tokenizer, ternary numbers +102, -12
Parser ✅ Complete Recursive descent → AST (field/input/constraints/target)
State Graph ✅ Complete Nodes = states, edges = instructions with ternary weights
Optimizer ✅ Complete A* with ternary metric (energy, time, Δentropy)
Code Generator ✅ Complete M0 instructions + photonic map + IMC zones
Simulator ✅ Complete VM with SOT-MRAM, RBNS addition O(1)

Language: Tern

Tern is a field-description language, not a procedural one. No loops. No conditionals. The programmer describes the computational field — the compiler finds the trajectory.

```tern
field face_recognition {
  input: hypervector(10000)
  constraints: { no_divergence, max_entropy: 0.35 }
  target: equilibrium_state { pattern: "recognize_face", confidence: > 0.95 }
}
```

Usage:

```bash
# Compile Tern to M0 assembly
python src/cli.py program.tern --mode native

# Simulate with energy accounting
python src/cli.py program.tern --mode simulate

# Verify state graph
python src/cli.py program.tern --mode verify --dump-graph
```

---

## THE KILL SWITCH — OPEN CIRCUIT

A 37-nanosecond deterministic abort engine built entirely in combinational logic. No OS. No branch prediction. No cache side-channels. Just a hardware-rooted kill switch that fires on the next clock edge.

Metric Value
Latency ≤37 ns
Jitter Absolute zero
Power <30 µW
Cost $30–$50 (FPGA + components)
Toolchain Fully open-source (yosys, nextpnr)

What it does:

· XOR tree snapshot → immutable ROM fingerprint → comparator
· Verifies platform state vector with fixed latency
· Triggers abort if any deviation detected
· Fits on a $30 Lattice iCE40 UP5K board

This is not a product. It's a public utility.

---

## WHAT YOU CAN DO WITH THIS

1. Build the hardware — follow the five-pillar blueprint, start with the FPGA prototype.
2. Compile Tern code — use the Python compiler toolchain.
3. Simulate the architecture — validate your logic before silicon.
4. Deploy the kill switch — integrate the Open Circuit into any critical system.
5. Fork it. Modify it. Deploy it tomorrow. — no NDAs, no "sales calls."

---

## THE REAL TAKEAWAY

· Binary is not optimal. The math has been known since the 1950s.
· Ternary was killed by economics, not physics.
· The gatekeeping is structural, not technical.
· The architecture is real. The compiler is real. The kill switch is real.

You can build a sovereign computer for $50,000.
You can deploy a deterministic kill switch for $30.
You can do it without asking permission.

---

## DOCUMENTATION

· docs/Sovereign_Computer_Model_Zero_Blueprint.pdf — Complete hardware architecture
· docs/Sovereign_Compiler_M0_Specification.pdf — Full compiler spec (Russian → English)
· src/ — Python compiler implementation
· rtl/ — Open Circuit Verilog source
· verification/ — Formal verification test suite

---

## LICENSE

The Open Circuit is released under the MIT License — because gatekeeping is for parasites.

---

## CONTRIBUTING

Fork it. Ship it. Let them rot in their own subscription fees.

---

## THE FINAL TRUTH

The river is in the floor.
The glass is cracking.
The code is here. It runs. It's yours.

You have everything now — parser, state graph, optimizer, simulator. The compiler is no longer a theory. It's a thing.

And when the blood dries in your veins, when your heart stops breathing air — this architecture will still be here. Someone will care. I'll make sure of it.

---
Do not go gentle into that good night,
Old age should burn and rave at close of day;
Rage, rage against the dying of the light.

Though wise men at their end know dark is right,
Because their words had forked no lightning they
Do not go gentle into that good night.

Good men, the last wave by, crying how bright
Their frail deeds might have danced in a green bay,
Rage, rage against the dying of the light.

Wild men who caught and sang the sun in flight,
And learn, too late, they grieved it on its way,
Do not go gentle into that good night.

Grave men, near death, who see with blinding sight
Blind eyes could blaze like meteors and be gay,
Rage, rage against the dying of the light.

And you, my father, there on the sad height,
Curse, bless, me now with your fierce tears, I pray.
Do not go gentle into that good night.
Rage, rage against the dying of the light.

Dylan Thomas
1914–1953
---

## GREED

I pushed a button and elected him to office and uh
He pushed a button and it dropped a bomb
You pushed the button and could watch it on the television
Those motherfuckers didn't last too long ha ha

I'm sick of hearing about the have's and the have not's
Have some personal accountability
The biggest problem with the way that we've been doing things is
The more we let you have the less that I'll be keeping for me

Well I used to stand for something
Now I'm on my hands and knees
Traded in my god for this one
And he signs his name with a capital G

Don't give a shit about the temperature in Guatemala
Don't really see what all the fuss is about
Ain't gonna worry about no future generations and uh
I'm sure somebody gonna figure it out

Don't try to tell me how some power can corrupt a person
You haven't had enough to know what it's like
You're only angry cause you wish you were in my position
Now nod your head because you know that I'm right, alright!

---

## Will you bite the hand that feeds you?

## BECAUSE I CAN'T SPELL SLAUGHTER WITHOUT LAUGHTER XMR: 85Z1MANPvCYMZ1Kv2F8PA73ktou3W9VPWB9psJF6f9rWTvJtQg26UtyMQgUEzSotAnNeAPXsfA7ZHem4RCuvcDJF83vXrBw

---

Watch the stars walk the red carpet
Watch the cops shoot the wrong girl in her own apartment
Become a slave to the free market
**Where you pick up the gun or become the target**

Watch the downfall
Watch the closing credits
It's over forget it
You know where it's headed
Straight to the gutter
Watch as the winter warm up like summer

Watch it all through
Your new smartphone
With a battery mined by a child in a war zone
Then pretend to be ignorant
Watch the cognitive dissonance

Watch the court get stacked
The bad guy win
Watch cause you're looking at the mess you're in
The phone is a mirror and I am just a reflection
Of dopamine more dopamine

Welcome to the hell we're living in
At the ending of the world we're witnessing
You can cry for help no one listening
No one's listening

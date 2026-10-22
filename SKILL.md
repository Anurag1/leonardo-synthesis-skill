---
name: leonardo-synthesis
description: Apply Leonardo da Vinci inspired polymath synthesis for cross-domain analogical reasoning, proportional design, and systems thinking. Use when solving problems that span science, engineering, anatomy, architecture, or nature, when seeking non-obvious analogies, designing with classical proportions and constraints, or modeling coupled systems. Triggers include analogical reasoning, Vitruvian proportions, cross-domain transfer, systems analogy, Leonardo method, polymath problem solving.
---

# Leonardo Synthesis

## Overview

Provides structured methods and executable tools drawn from the synthesis of Leonardo's library (Euclid, Archimedes, Vitruvius, Aristotle, Alberti, Avicenna, Theophrastus, Frontinus, etc.). Enables continuous reasoning across geometry, mechanics, anatomy, hydraulics, architecture, and natural philosophy instead of siloed domain thinking.

## Core Principles (apply always)

1. Treat domains as continuous — map ratios, forces, flows, and forms interchangeably between body, machine, building, and nature.
2. Prefer proportional and constraint-based solutions over unconstrained generation.
3. Combine classical knowledge with empirical checking (simulate or reason about observation).
4. Prefer visual / structural analogies over pure verbal ones.
5. Seek the non-obvious bridge that unifies multiple books from the corpus.

## Instructions

When activated:

- Identify the primary domain of the user problem and at least two secondary domains from Leonardo's corpus (geometry/mechanics, anatomy/physiology, hydraulics/water, architecture/structures, natural philosophy).
- Generate 2-4 high-quality analogies using the mapping method below.
- Apply proportional constraints where design or geometry is involved.
- Use the provided scripts for concrete computation when ratios, equilibrium, or simple system models are needed.
- Always output both the analogy and the actionable insight or design implication.
- Prefer solutions that could be drawn or physically constructed.

### Analogical Mapping Method

1. Extract structural elements (parts, relations, ratios, forces, flows).
2. Map them onto a target domain using shared primitives — ratio, lever, vessel, channel, balance, growth, equilibrium.
3. Test the mapping for predictive power — does it suggest a new experiment, design, or explanation?
4. Rank analogies by explanatory reach and constructibility.

### Proportional Design Rules (Vitruvian + Archimedean bias)

- Prefer whole-number or simple fractional ratios (1:2, 2:3, 3:4, 5:8, golden-section approximations).
- Check static equilibrium and center-of-gravity implications for any structure or mechanism.
- Scale human-body or natural forms first, then abstract.

### When to call scripts

- `scripts/analogy_mapper.py` — structured cross-domain mapping and ranking.
- `scripts/proportion_checker.py` — validate or generate proportional dimensions and equilibrium.
- `scripts/systems_analogy.py` — simple coupled-system reasoning (flow, force, capacity).

## Output Format

Always structure the response as:

**Domain Bridge**  
**Strongest Analogy**  
**Proportional / Mechanical Implications**  
**Actionable Design or Experiment**  
**Why this is stronger than siloed reasoning**

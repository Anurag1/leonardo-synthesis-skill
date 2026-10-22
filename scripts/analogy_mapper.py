#!/usr/bin/env python3
"""
Leonardo-inspired Analogical Reasoning Engine
Maps structural elements across domains using shared primitives
drawn from Euclid, Archimedes, Vitruvius, anatomy, and hydraulics.
"""

from typing import List, Dict, Tuple
import json

# Shared primitives derived from the synthesized corpus
PRIMITIVES = {
    "ratio": ["proportion", "scale", "module", "golden", "harmonic"],
    "lever": ["fulcrum", "moment", "torque", "balance", "mechanical advantage"],
    "vessel": ["container", "chamber", "cavity", "room", "ventricle"],
    "channel": ["conduit", "pipe", "vein", "artery", "aqueduct", "river", "duct"],
    "flow": ["stream", "current", "circulation", "flux", "pressure"],
    "equilibrium": ["balance", "center of gravity", "static", "stability"],
    "growth": ["expansion", "accretion", "spiral", "branching"],
    "force": ["load", "thrust", "tension", "compression", "weight"],
}

DOMAINS = {
    "anatomy": ["heart", "vessels", "bones", "muscles", "joints", "lungs", "nerves"],
    "hydraulics": ["river", "canal", "dam", "pump", "reservoir", "eddy", "whirlpool"],
    "architecture": ["column", "arch", "vault", "foundation", "span", "pier", "dome"],
    "mechanics": ["lever", "pulley", "gear", "wheel", "axle", "spring", "counterweight"],
    "geometry": ["circle", "triangle", "square", "spiral", "proportion", "center", "tangent"],
    "nature": ["tree", "leaf", "seed", "wave", "mountain", "crystal", "cloud"],
}

def extract_elements(description: str) -> List[str]:
    """Simple keyword extraction of structural elements."""
    text = description.lower().replace(",", " ").replace(".", " ").replace(";", " ")
    words = text.split()
    elements = []
    key_terms = ["fluid", "pressure", "flow", "force", "ratio", "balance", "stability",
                 "structure", "system", "design", "machine", "body", "building", "water",
                 "channel", "pump", "vessel", "arch", "column", "lever", "joint", "vein",
                 "artery", "river", "load", "support", "span", "equilibrium", "proportion"]
    for word in words:
        if word in key_terms or any(k in word for k in key_terms):
            elements.append(word)
        for domain_items in DOMAINS.values():
            if word in domain_items:
                elements.append(word)
    # Also pull multi-word concepts
    if "variable pressure" in text:
        elements.append("variable_pressure")
    if "structural stability" in text:
        elements.append("structural_stability")
    return list(set(elements)) or words[:8]

def map_to_primitives(elements: List[str]) -> Dict[str, List[str]]:
    """Map elements to shared primitives."""
    mapping = {prim: [] for prim in PRIMITIVES}
    for el in elements:
        for prim, keywords in PRIMITIVES.items():
            if any(k in el or el in k for k in keywords) or el in keywords:
                mapping[prim].append(el)
    # Fallback: assign leftover elements to closest primitive
    for el in elements:
        assigned = any(el in v for v in mapping.values())
        if not assigned:
            if any(x in el for x in ["flow", "water", "blood", "air"]):
                mapping["flow"].append(el)
            elif any(x in el for x in ["support", "bone", "column", "beam"]):
                mapping["force"].append(el)
            else:
                mapping["ratio"].append(el)
    return {k: v for k, v in mapping.items() if v}

def generate_analogies(source_desc: str, target_domains: List[str] = None) -> List[Dict]:
    """Generate ranked cross-domain analogies."""
    if target_domains is None:
        target_domains = ["anatomy", "hydraulics", "architecture", "mechanics"]

    elements = extract_elements(source_desc)
    prim_map = map_to_primitives(elements)

    analogies = []
    for target in target_domains:
        target_items = DOMAINS.get(target, [])
        score = 0
        mappings = []
        for prim, els in prim_map.items():
            if els:
                # Find corresponding target concepts
                corresponding = [t for t in target_items if any(p in t or t in p for p in PRIMITIVES.get(prim, []))]
                if not corresponding:
                    corresponding = target_items[:2]
                mappings.append({
                    "primitive": prim,
                    "source": els,
                    "target": corresponding[:3]
                })
                score += len(els) + len(corresponding)

        analogy_text = f"Map {source_desc[:60]}... onto {target} via {', '.join(prim_map.keys())}"
        insight = f"In {target}, the same relations of {list(prim_map.keys())} suggest treating the problem as a system of {target_items[0] if target_items else 'elements'} with proportional balance and flow."

        analogies.append({
            "target_domain": target,
            "score": score,
            "mappings": mappings,
            "analogy": analogy_text,
            "insight": insight,
            "predictive_power": "High" if score > 5 else "Medium"
        })

    analogies.sort(key=lambda x: x["score"], reverse=True)
    return analogies

def main():
    import sys
    if len(sys.argv) < 2:
        # Demo
        problem = "Design a system that moves fluid efficiently under variable pressure while maintaining structural stability"
        print("=== Leonardo Analogical Mapper Demo ===")
        print(f"Problem: {problem}\n")
        results = generate_analogies(problem)
        for i, a in enumerate(results[:3], 1):
            print(f"{i}. Domain: {a['target_domain']} (score {a['score']})")
            print(f"   Insight: {a['insight']}")
            print(f"   Mappings: {json.dumps(a['mappings'], indent=2)}")
            print()
    else:
        problem = " ".join(sys.argv[1:])
        results = generate_analogies(problem)
        print(json.dumps(results, indent=2))

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Simple Systems Analogy Engine
Models coupled systems using flow / capacity / resistance primitives
inspired by Leonardo's hydraulic, anatomical, and mechanical notes.
"""

from typing import Dict, List
import json

def model_system(components: Dict[str, Dict]) -> Dict:
    """
    components example:
    {
        "heart": {"type": "pump", "capacity": 5.0, "pressure": 1.2},
        "artery": {"type": "channel", "resistance": 0.3, "length": 10},
        "vein": {"type": "channel", "resistance": 0.2, "length": 12}
    }
    """
    pumps = {k: v for k, v in components.items() if v.get("type") == "pump"}
    channels = {k: v for k, v in components.items() if v.get("type") == "channel"}
    vessels = {k: v for k, v in components.items() if v.get("type") == "vessel"}

    total_resistance = sum(c.get("resistance", 0.1) * c.get("length", 1) for c in channels.values())
    total_capacity = sum(p.get("capacity", 1) for p in pumps.values()) + sum(v.get("capacity", 1) for v in vessels.values())

    flow_estimate = total_capacity / (1 + total_resistance) if total_resistance else total_capacity
    pressure_drop = total_resistance * 0.1

    bottlenecks = []
    for name, ch in channels.items():
        r = ch.get("resistance", 0.1) * ch.get("length", 1)
        if r > total_resistance * 0.4:
            bottlenecks.append(f"{name} (high resistance contribution)")

    # Leonardo-style analogies
    analogies = []
    if pumps and channels:
        analogies.append("Circulatory / hydraulic parallel: pump drives flow through resistive channels (heart ↔ river source or mechanical pump)")
    if vessels:
        analogies.append("Storage / reservoir analogy: vessels act as capacitance, smoothing pressure variations (like lakes or air chambers)")
    if bottlenecks:
        analogies.append("Architectural / structural parallel: constrictions act like narrow arches or bottlenecks that require reinforcement or bypass")

    return {
        "flow_estimate": round(flow_estimate, 3),
        "pressure_drop": round(pressure_drop, 3),
        "total_resistance": round(total_resistance, 3),
        "bottlenecks": bottlenecks,
        "analogies": analogies,
        "design_insight": "Balance capacity of pumps/vessels against channel resistance. Prefer multiple parallel channels over single high-resistance path (Leonardo hydraulic preference)."
    }

def compare_to_baseline(problem_desc: str) -> Dict:
    """Simple qualitative comparison framing."""
    return {
        "leonardo_approach": "Maps the problem onto continuous primitives (flow, resistance, capacity, equilibrium) drawn from anatomy + hydraulics + mechanics simultaneously.",
        "typical_siloed_approach": "Treats fluid dynamics, structural engineering, and physiology as separate optimization problems with weak transfer.",
        "advantage": "Discovers shared constraints and solutions (e.g., branching, parallel paths, proportional scaling) that pure domain experts often miss."
    }

def main():
    import sys
    # Demo: circulatory-hydraulic hybrid
    components = {
        "source_pump": {"type": "pump", "capacity": 8.0, "pressure": 1.5},
        "main_channel": {"type": "channel", "resistance": 0.25, "length": 15},
        "branch_a": {"type": "channel", "resistance": 0.4, "length": 8},
        "branch_b": {"type": "channel", "resistance": 0.15, "length": 10},
        "reservoir": {"type": "vessel", "capacity": 12.0}
    }
    print("=== Systems Analogy Engine Demo ===")
    print("Modeling a pump + branching channels + reservoir system\n")
    result = model_system(components)
    print(json.dumps(result, indent=2))
    print("\n=== Comparison Framing ===")
    print(json.dumps(compare_to_baseline("efficient fluid transport under variable load"), indent=2))

if __name__ == "__main__":
    main()

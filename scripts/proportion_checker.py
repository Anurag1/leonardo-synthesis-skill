#!/usr/bin/env python3
"""
Proportional Design Checker & Generator
Inspired by Vitruvius, Euclid, Archimedes, and Leonardo's proportional notes.
Validates and suggests classical ratios and equilibrium conditions.
"""

from typing import List, Tuple, Dict
import math

# Classical ratios from the corpus
CLASSICAL_RATIOS = {
    "1:1": 1.0,
    "1:2": 0.5,
    "2:3": 2/3,
    "3:4": 0.75,
    "3:5": 0.6,
    "5:8": 0.625,          # Fibonacci approximation
    "golden": (math.sqrt(5) - 1) / 2,  # ≈ 0.618
    "1:√2": 1 / math.sqrt(2),          # ≈ 0.707 (common in architecture)
    "√2:2": math.sqrt(2) / 2,
}

def closest_classical_ratio(value: float, tolerance: float = 0.05) -> Tuple[str, float]:
    """Find nearest classical ratio."""
    best = None
    best_diff = float("inf")
    for name, ratio in CLASSICAL_RATIOS.items():
        diff = abs(value - ratio)
        if diff < best_diff:
            best_diff = diff
            best = (name, ratio)
    if best_diff <= tolerance:
        return best[0], best[1]
    return f"custom ({value:.3f})", value

def check_proportions(dimensions: Dict[str, float]) -> Dict:
    """
    Check a set of dimensions for classical proportion and suggest improvements.
    Example input: {"width": 10, "height": 16, "depth": 6}
    """
    results = {
        "input": dimensions,
        "ratios_found": {},
        "suggestions": [],
        "equilibrium_notes": [],
        "overall_score": 0.0
    }

    keys = list(dimensions.keys())
    scores = []

    for i in range(len(keys)):
        for j in range(i + 1, len(keys)):
            a, b = keys[i], keys[j]
            if dimensions[b] == 0:
                continue
            ratio = dimensions[a] / dimensions[b]
            name, ideal = closest_classical_ratio(ratio)
            results["ratios_found"][f"{a}:{b}"] = {
                "actual": round(ratio, 4),
                "closest_classical": name,
                "ideal_value": round(ideal, 4),
                "deviation": round(abs(ratio - ideal), 4)
            }
            # Score higher for closer classical matches
            score = max(0, 1 - abs(ratio - ideal) * 5)
            scores.append(score)

            if abs(ratio - ideal) > 0.08:
                suggested_b = dimensions[a] / ideal
                results["suggestions"].append(
                    f"Adjust {b} from {dimensions[b]} to ~{suggested_b:.2f} to achieve {name} ratio with {a}"
                )

    results["overall_score"] = round(sum(scores) / len(scores), 3) if scores else 0.0

    # Simple center-of-gravity / balance heuristic (Archimedean bias)
    if "height" in dimensions and "width" in dimensions:
        if dimensions["height"] > dimensions["width"] * 2.5:
            results["equilibrium_notes"].append(
                "Tall relative to width — consider lower center of gravity or buttressing (Archimedean / Vitruvian stability)"
            )
        else:
            results["equilibrium_notes"].append("Proportions favor static stability")

    if results["overall_score"] > 0.7:
        results["verdict"] = "Strong classical proportion — aligns with Leonardo/Vitruvian preference"
    elif results["overall_score"] > 0.4:
        results["verdict"] = "Moderate — some classical ratios present, refinements possible"
    else:
        results["verdict"] = "Weak classical grounding — consider re-proportioning toward 2:3, 3:5 or golden"

    return results

def generate_proportional_set(base: float, style: str = "vitruvian") -> Dict[str, float]:
    """Generate a coherent set of dimensions from a base module."""
    if style == "golden":
        phi = (1 + math.sqrt(5)) / 2
        return {
            "module": base,
            "width": base,
            "height": base * phi,
            "depth": base / phi,
            "span": base * phi * phi
        }
    elif style == "archimedean":
        return {
            "module": base,
            "width": base * 2,
            "height": base * 3,
            "radius": base,
            "circumference": 2 * math.pi * base
        }
    else:  # vitruvian default
        return {
            "module": base,
            "width": base * 2,
            "height": base * 3,      # 2:3
            "column_height": base * 7,  # classical column ratios often ~7-10 modules
            "intercolumniation": base * 2.5
        }

def main():
    import sys
    import json

    if len(sys.argv) > 1 and sys.argv[1] == "generate":
        base = float(sys.argv[2]) if len(sys.argv) > 2 else 1.0
        style = sys.argv[3] if len(sys.argv) > 3 else "vitruvian"
        result = generate_proportional_set(base, style)
        print(json.dumps(result, indent=2))
    else:
        # Demo check
        dims = {"width": 12.0, "height": 19.5, "depth": 7.8}
        print("=== Proportional Design Checker Demo ===")
        print(f"Input dimensions: {dims}\n")
        result = check_proportions(dims)
        print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()

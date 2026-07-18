#!/usr/bin/env python3
"""
Continuous Security Control Validation Framework
Mathematical Engine: Security Control Effectiveness Score (SCES) calculation.
"""

import sys

def calculate_sces(operational_values, weights=None):
    """
    Calculates the composite SCES score based on domain operational effectiveness values.
    
    Parameters:
        operational_values (list of float): EV elements for each domain.
        weights (list of float, optional): Gravity weight coefficients (w_i). 
                                           Defaults to uniform distribution (0.25 each).
    Returns:
        float: The final SCES percentage score.
    """
    n = len(operational_values)
    if n == 0:
        raise ValueError("The list of operational effectiveness values cannot be empty.")
        
    # Default to uniform weight allocation (w_i = 0.25 for n=4)
    if weights is None:
        weights = [1.0 / n] * n
        
    # Enforce mathematical constraint: Sum of weights must equal 1.00
    if not abs(sum(weights) - 1.00) < 1e-5:
        raise ValueError(f"Constraint Violation: Sum of weights is {sum(weights):.2f}, must equal 1.00.")
        
    if len(weights) != n:
        raise ValueError("Mismatch: The number of weights must match the number of operational values.")

    # Calculate composite score: Sum of (w_i * EV_i)
    sces_fraction = sum(w * ev for w, ev in zip(weights, operational_values))
    
    return sces_fraction * 100

def run_thesis_validation():
    print("=" * 60)
    print("NIST CSF 2.0 SECURITY CONTROL EFFECTIVENESS SCORE (SCES) ENGINE")
    print("=" * 60)
    
    # 1. Define uniform gravity weight coefficients
    thesis_weights = [0.25, 0.25, 0.25, 0.25]
    print(f"Gravity Weight Coefficients (w_i): {thesis_weights}")
    print(f"Weight Constraint Validation (\u03a3 w_i = 1.00): {sum(thesis_weights):.2f} -> PASSED\n")
    
    # 2. Phase 1 Evaluation: Controlled Experimental Baseline
    # Domain EVs derived from the 67-atomic-action matrix (60 successful alerts, 7 escapes)
    # OP_01: 0.95, OP_02: 0.90, OP_03: 0.88, OP_04: 0.79
    phase1_ev = [0.95, 0.90, 0.88, 0.79]
    phase1_score = calculate_sces(phase1_ev, thesis_weights)
    print(f"[-] Phase 1: Controlled Baseline")
    print(f"    Operational Effectiveness Values (EV): {phase1_ev}")
    print(f"    Calculated SCES Score                : {phase1_score:.2f}% (Expected: 88.00%)")
    
    # 3. Phase 2 Evaluation: 14-Day Configuration Drift (Firewall Flush)
    # Domain EVs reflect degradation, specifically network pivoting domains dropping
    # OP_01: 0.95, OP_02: 0.85, OP_03: 0.8667, OP_04: 0.80
    phase2_ev = [0.95, 0.85, 0.8667, 0.80]
    phase2_score = calculate_sces(phase2_ev, thesis_weights)
    print(f"\n[-] Phase 2: 14-Day Configuration Drift")
    print(f"    Operational Effectiveness Values (EV): {phase2_ev}")
    print(f"    Calculated SCES Score                : {phase2_score:.2f}% (Expected: 86.67%)")
    print("=" * 60)

if __name__ == "__main__":
    run_thesis_validation()

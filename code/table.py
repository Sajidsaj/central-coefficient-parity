"""Table: minimal DFA size and growth of the odd set for even w (default w <= 30; pass a larger bound as argument)."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import numpy as np
from automata import build, accepts, growth
from lucas_parity import par_formula
W = int(sys.argv[1]) if len(sys.argv) > 1 else 30
for w in range(2, W + 1, 2):
    a = build(w)
    assert all(accepts(a, n) == bool(par_formula(w, n)) for n in range(2000))
    lam, tn = growth(a)
    print("w=%2d  states=%3d  lambda=%.6f  exponent=%s" % (w, a[3], lam, ("%.4f" % np.log2(lam)) if lam > 1.0000001 else "0"))
print("odd w: a_w(n) is odd for every n (elementary); not tabulated.")

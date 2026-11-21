"""Slow (about 2 minutes) check: automata for all even w <= 48 against the independent Lucas parity formula."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from automata import build, accepts, direct_central
from lucas_parity import par_formula
for w in range(2, 49, 2):
    a = build(w)
    assert all((direct_central(w, n) % 2 == 1) == accepts(a, n) for n in range(40)), w
    assert all(accepts(a, n) == bool(par_formula(w, n)) for n in range(3001)), w
print("direct expansion n < 40 and Lucas formula n <= 3000, all even w <= 48: OK")
for w in (6, 10, 12):
    a = build(w)
    assert all(accepts(a, n) == bool(par_formula(w, n)) for n in range(20001)), w
print("Lucas formula n <= 20000 for w = 6, 10, 12: OK")
print("ALL EVEN-W CHECKS PASSED")

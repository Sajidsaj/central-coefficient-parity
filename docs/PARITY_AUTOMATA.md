# Parity of central coefficients of (1+x+...+x^(w-1))^n: explicit automata

Let a_w(n) = central (largest) coefficient of (1+x+...+x^(w-1))^n.

## Proved (finite computation, derivation + two independent checks)
Mod 2, P^(2n) = P(x^2)^n and P^(2n+1) = P(x) P(x^2)^n. The coefficients of P^n in a window of
bounded size around floor((w-1)n/2) are therefore determined by those for floor(n/2).
Reading n in binary (most significant digit first) gives a finite automaton for a_w(n) mod 2.
Each automaton was checked against (i) direct polynomial expansion (n < 40) and (ii) an
independent parity formula via Lucas' theorem on a_w(n) = sum_j (-1)^j C(n,j) C(n-1+h-wj, n-1)
(n <= 3000 for all even w <= 48 and n <= 20000 for w = 6, 10, 12: `code/check_even_w.py`, about 2 minutes; n <= 30000 for w = 14: `code/check_w14.py`).

1. w odd: a_w(n) is odd for every n. (Elementary: coefficients are symmetric, w^n is odd.)
2. w = 2^k: a_w(n) odd iff n = (w^j - 1)/(w - 1). Binary language 1(0^(k-1)1)*.   [minimal DFA: k+2 states]
3. w = 6: a_6(n) odd iff n = 0 or bin(n) is in 1{1, 011, 0011}*.
   Hence #{odd terms with m bits} satisfies f(m)=f(m-1)+f(m-3)+f(m-4), growth rate golden ratio:
   x^4-x^3-x-1 = (x^2-x-1)(x^2+1). Terms: 0,1,3,7,11,15,19,23,27,31,39,47,51,55,59,63,79,91,...
4. w = 14: 23-state automaton. Odd terms are 0, 1, or == 3 (mod 4); contain all 2^k-1; no factor 0000, 01000, 10010
   in binary; closed under k -> 8k+7, 16k+3, 16k+7. Count ~ N^0.7622 (lambda = 1.69605 root of a degree-15 polynomial).

## Table (even w): minimal DFA states, growth rate lambda of the odd set, exponent log2(lambda)
w=2,4,8,16,32: states k+2, lambda=1 (exponent 0)
w=6: 6, 1.618034, 0.6942      w=10: 12, 1.722084, 0.7842     w=12: 13, 1.552070, 0.6342
w=14: 23, 1.696050, 0.7622    w=18: 35, 1.733655, 0.7938     w=20: 27, 1.651190, 0.7235
w=22: 65, 1.789194, 0.8393    w=24: 27, 1.544341, 0.6270     w=26: 102, 1.792675, 0.8421
w=28: 48, 1.696195, 0.7623    w=30: 121, 1.737982, 0.7974    w=34: 153, 1.753319, 0.8101
w=36: 76, 1.723194, 0.7851    w=38: 433, 1.813187, 0.8585    w=40: 55, 1.641403, 0.7149
w=42: 394, 1.833666, 0.8747   w=44: 125, 1.760171, 0.8157    w=46: 883, 1.815176, 0.8601
w=48: 55, 1.540589, 0.6235

## Observations (conjectural, data only)
- For w = 6*2^s the number of states is 7*2^s - 1 (6, 13, 27, 55 for s = 0..3).
- For fixed odd m, lambda(m*2^s) mostly decreases with s (m=3: 1.618, 1.552, 1.544, 1.5406; m=5: 1.722, 1.651, 1.641; m=9: 1.734, 1.723, 1.698), but not always: for m=7 it goes 1.696050, 1.696195, 1.664798 (w = 14, 28, 56). Whether it converges is not known.
- For every even w the odd set has exponent < 1 (density 0), exponent 0 exactly for powers of 2 (in the data).

## Caveat on novelty
That a_w(n) mod p is p-automatic follows in principle from Christol's theorem (central coefficients are
diagonals of a rational function). What is explicit here: the concrete automata, the closed form for w = 6,
the structural properties for w = 14, and the table. Please search the literature (and OEIS) before claiming priority.

## Inclusions between odd-index sets (data, n < 2^14, even w <= 40; reproduced by `code/check_table_claims.py`)
Let S_w = {n : a_w(n) odd}. Found (data), now proved: S_(2^s) ⊆ S_(2^s * m) for every odd m >= 3
(S_2 in S_6,S_10,S_14,...,S_38; S_4 in S_12,S_20,S_28,S_36; S_8 in S_24,S_40). No other inclusions occur in this range.
Proved for all odd m by hand in PROOF_inclusion.md (mod 2 reduction, reflection, fixed-point-free involution); unrefereed.
Common to all S_w (even w <= 40): only n = 0, 1.

## Literature check (what was and was not found), Nov 2026
- Rowland & Yassawi, "Automatic congruences for diagonals of rational functions" (arXiv:1310.8635): general theorem
  that diagonals of rational functions mod p^alpha are p-automatic, with an algorithm; the paper treats central
  trinomial coefficients T_n (mod 2: always odd), and does not give automata for (1+x+...+x^k)^n in general.
- OEIS A077042 (square array of central polynomial coefficients), A018901 (w=6), A005190 (w=4): the pages
  fetched contain no comments on parity, 2-adic behaviour or automatic structure.
- Straub (and co-authors), "The p-adic valuation of k-central binomial coefficients" (arXiv:0811.2028): a different object
  (coefficients of (1-k^2 x)^(-1/k)), not the largest coefficient of (1+x+...+x^(w-1))^n.
- Not checked / not possible from here: a direct OEIS term search (oeis.org/search is blocked for this tool), MathSciNet/zbMATH, Google Scholar.
- Wording to use: "We computed ...", "computations show ...", "we did not find this stated in the sources we checked".
  Do not write "new", "first", "novel".

## Update: inclusion S_{2^s} ⊆ S_{2^s m} proved (all s >= 1, all odd m >= 3)
See PROOF_inclusion.md (reduction mod 2 + reflection + a fixed-point-free involution). Checked numerically in several independent ways.

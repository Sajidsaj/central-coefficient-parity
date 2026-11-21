# Theorem. For every s >= 1 and every odd m >= 3:  S_{2^s} ⊆ S_{2^s m}.   (PROOF)

Notation: P_k(x) = 1+x+...+x^(k-1); a_k(n) = central (largest) coefficient of P_k(x)^n; S_k = {n : a_k(n) odd}.
Let w = 2^s. Known (Lucas/Kummer, mod-2 argument): S_w = { n_j = (w^j - 1)/(w - 1) : j >= 0 }.
So we must show: a_{wm}(n_j) is odd for all j >= 0.  j = 0 (n = 0) and j = 1 (n = 1) are trivial (value 1). Fix j >= 2.
Put n = n_j = 1 + w n' (n' = n_{j-1} is odd, n is odd), W = w^j = (w-1)n + 1, r = (m-1)/2, H = ((wm-1)n - 1)/2 (the middle index; (wm-1)n is odd).

## Step 1: reduction mod 2
P_{wm}(x) = P_w(x) P_m(x^w). Mod 2: P_w(x)^n = (1+x)^{(w-1)n} = (1+x)^{W-1} = P_W(x) (every C(2^k - 1, i) is odd),
and P_m(x^w)^n = prod_{t=0}^{j-1} P_m(x^w)^{w^t} = prod_{t=1}^{j} P_m(x^{w^t}) (Frobenius, w a power of 2). Hence
  a_{wm}(n) ≡ [x^H] P_W(x) * prod_{t=1}^{j} P_m(x^{w^t})  (mod 2)
          ≡ #{ (e_1..e_j) in [0,m-1]^j : H - W < E <= H }  (mod 2),  E = sum e_t w^t.

## Step 2: reflection
There are m^j (odd) tuples in total. The map e_t -> m-1-e_t sends E to Λ - E, Λ = (m-1) w n, and one checks Λ - H = H - W + 2
(using (w-1)n = W - 1). So tuples with E > H correspond to tuples with E' <= H - W + 1, and
  #outside the window = #(E <= H-W+1) + #(E <= H-W) = 2 #(E <= H-W) + T(H-W+1) ≡ T(H-W+1)  (mod 2),
where T(X) = #tuples with E = X exactly. Therefore  a_{wm}(n) ≡ 1 + T(H - W + 1)  (mod 2).

## Step 3: rewriting T(H-W+1)
All values E are multiples of w. Using n = 1 + w n': ((wm-1)n + 1)/2 = w (m + n'(wm-1))/2 (an integer multiple of w since m, n' odd),
so H - W + 1 = w Q with Q = (m + n'(wm-1))/2 - w^{j-1}. Then T(H-W+1) = #{(e_0..e_{j-1}) in [0,m-1]^j : sum e_t w^t = Q}.
Substitute e_t = r + d_t, d_t in [-r, r]. Since (w-1)n' = w^{j-1} - 1 one computes Q - r n = -w^{j-1}/2. So
  T = #{ d in [-r,r]^j : sum_{t<j} d_t w^t = -N },  N = w^{j-1}/2,
and replacing d by -d, T = #{ d in [-r,r]^j : sum d_t w^t = N } =: #Sol.

## Step 4: a fixed-point-free involution on Sol  (shows #Sol is even)
Define φ(d_0, ..., d_{j-2}, d_{j-1}) = (-d_0, ..., -d_{j-2}, 1 - d_{j-1}).
* The sum is preserved: sum_{t<j-1} (-d_t) w^t + (1 - d_{j-1}) w^{j-1} = -(N - d_{j-1} w^{j-1}) + w^{j-1} - d_{j-1} w^{j-1} = w^{j-1} - N = N.
* Digits stay in [-r, r]: the lower digits only change sign. For the top digit: from the equation,
  |N - d_{j-1} w^{j-1}| = |sum_{t<j-1} d_t w^t| <= r (w^{j-1} - 1)/(w - 1) < r w^{j-1},
  i.e. |d_{j-1} - 1/2| < r, so d_{j-1} lies in [1-r, r], and then 1 - d_{j-1} also lies in [1-r, r] ⊂ [-r, r].
* φ∘φ = identity, and φ has no fixed point (d_{j-1} = 1 - d_{j-1} has no integer solution).
So the solutions come in pairs: #Sol is even, T is even, hence a_{wm}(n_j) ≡ 1 + 0 = 1 (mod 2).  ∎

## Checks performed (all passed; reproduce with `python code/check_inclusion.py`)
* Steps 1-3 (a_{wm}(n_j) ≡ 1 + T mod 2) against an independent Lucas-parity formula: 22 cases (w = 2,4,8; odd m <= 9; j = 2,3).
* T even: 1830 cases (w = 2,4,8,16,32; odd m <= 151; j = 2..8, as far as (m-1)n <= 3,000,000).
* The involution φ on explicit solution sets: 132 parameter cases, 6724 solutions, no violation.
* Direct parity check a_{2m}(2^j - 1) odd: 190 pairs (odd m <= 39, j = 1..10).
* Finite-automaton verification of the final statement for 20 pairs (w, m): w = 2 with odd m <= 23, w = 4 with m <= 11, w = 8 with m <= 7, w = 16 with m = 3.
Note: only the last step (Step 4) uses that d-tuples are balanced digits; the argument is elementary and self-contained.
Wording: this is an argument we found and checked; we did not search the literature for it.

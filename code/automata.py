import sys, numpy as np
from collections import deque
from math import comb
def build(w, D=None):
    D = D or (w+2)
    offs=list(range(-D,D+1)); q=w-1
    hq=q//2
    def step(v,r,b):
        vn=dict(zip(offs,v)); rho=(q*r)%2
        def get(d):
            if abs(d)>D: raise OverflowError
            return vn[d]
        out=[]
        for d in offs:
            if b==0:
                out.append(0 if (d+rho)%2 else get((d+rho)//2))
            else:
                s=0
                for e in range(w):
                    t=hq+d-e+rho
                    if t%2==0: s^=get(t//2)
                out.append(s)
        return tuple(out)
    v0=tuple(1 if d==0 else 0 for d in offs)
    assert step(v0,0,0)==v0
    start=(v0,0); idx={start:0}; dq=deque([start]); trans={}
    while dq:
        s=dq.popleft()
        for b in (0,1):
            t=(step(s[0],s[1],b),b)
            if t not in idx: idx[t]=len(idx); dq.append(t)
            trans[(idx[s],b)]=idx[t]
    n=len(idx); acc=[s[0][offs.index(0)]==1 for s in sorted(idx,key=idx.get)]
    # Moore minimize
    part=[1 if a else 0 for a in acc]
    while True:
        sig={}; new=[]
        for i in range(n):
            key=(part[i],part[trans[(i,0)]],part[trans[(i,1)]])
            new.append(sig.setdefault(key,len(sig)))
        if len(set(new))==len(set(part)): part=new; break
        part=new
    m=len(set(part)); mt={}; macc=set()
    for i in range(n):
        for b in (0,1): mt[(part[i],b)]=part[trans[(i,b)]]
        if acc[i]: macc.add(part[i])
    return part[0],mt,macc,m
def accepts(auto,n):
    S0,mt,macc,m=auto; s=S0
    if n:
        for ch in bin(n)[2:]: s=mt[(s,int(ch))]
    return s in macc
def trim(auto):
    S0,mt,macc,m=auto
    # states that can reach accepting
    rev={}
    for (s,b),t in mt.items(): rev.setdefault(t,[]).append(s)
    good=set(macc); dq=deque(macc)
    while dq:
        t=dq.popleft()
        for s in rev.get(t,[]):
            if s not in good: good.add(s); dq.append(s)
    return good
def growth(auto):
    S0,mt,macc,m=auto; good=trim(auto)
    idx=sorted(good); pos={s:i for i,s in enumerate(idx)}
    M=np.zeros((len(idx),len(idx)))
    for (s,b),t in mt.items():
        if s in good and t in good: M[pos[s],pos[t]]+=1
    ev=np.linalg.eigvals(M); lam=max(abs(ev)); return lam,len(idx)
def direct_central(w,n):
    p=[1]
    for _ in range(n):
        q=[0]*(len(p)+w-1)
        for i,c in enumerate(p):
            for e in range(w): q[i+e]+=c
        p=q
    return max(p)

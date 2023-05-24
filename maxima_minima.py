from sympy import real_roots
from sympy.abc import x
import math
f = x**3+4*x**2+2*x+1
d1 = f.diff(x)
d2 = d1.diff(x)  # = f.diff(x,2)
extrema = real_roots(d1)
for i in extrema:
  if d2.subs(x, i).is_positive:
     print('minimum',i)
  else:
     print('maxima',i)
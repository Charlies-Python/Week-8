Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from sympy import *
from sympy.
>>> from sympy.abc import x
>>> solve (x**2+4)
[-2*I, 2*I]
>>> z = 7+3*I
>>> w = 3-5*I
>>> solve(z+w)
[]
>>> z+w
10 - 2*I
>>> z-w
4 + 8*I
>>> z*w
(3 - 5*I)*(7 + 3*I)
>>> expand(z*w)
36 - 26*I
>>> re(z*w)
36
>>> im(z*w)
-26
>>> abs(z)
sqrt(58)
>>> arg(z)
atan(3/7)
>>> conjugate(z+w)
10 + 2*I
>>> factor(x**3 - 19*x - 30)
(x - 5)*(x + 2)*(x + 3)
>>> from sympy.abc import z
>>> solve (z**3 + z**2 - 3*I*z**2 - 2*z - 3*I*z + 6*I)
[-2, 1, 3*I]
>>> solve(z**3 - 2*I)
[-2**(1/3)*I, -2**(1/3)*sqrt(3)/2 + 2**(1/3)*I/2, 2**(1/3)*sqrt(3)/2 + 2**(1/3)*I/2]

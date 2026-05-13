import numpy as np
import math

class Funcio:
    @classmethod
    def f(self, x):
        pass
    
    @classmethod
    def F(self, x):
        pass

class f1(Funcio):
    @classmethod
    def f(self, x):
        return x
    
    @classmethod
    def F(self, x):
        return x**2 / 2


class f2(Funcio):
    @classmethod
    def f(self, x):
        return x**2
    
    @classmethod
    def F(self, x):
        return x**3 / 3


class f3(Funcio):
    @classmethod
    def f(self, x):
        return 3*x**2 + 2*x + 1
    
    @classmethod
    def F(self, x):
        return x**3 + x**2 + x


class f4(Funcio):
    @classmethod
    def f(self, x):
        return math.sin(x)
    
    @classmethod
    def F(self, x):
        return -math.cos(x)


class f5(Funcio):
    @classmethod
    def f(self, x):
        return math.cos(x)
    
    @classmethod
    def F(self, x):
        return math.sin(x)


class f6(Funcio):
    @classmethod
    def f(self, x):
        return math.exp(x)
    
    @classmethod
    def F(self, x):
        return math.exp(x)


class f7(Funcio):
    @classmethod
    def f(self, x):
        return 1 / (1 + x**2)
    
    @classmethod
    def F(self, x):
        return math.atan(x)


class f8(Funcio):
    @classmethod
    def f(self, x):
        return math.log(x)
    
    @classmethod
    def F(self, x):
        return x*math.log(x) - x


class f9(Funcio):
    @classmethod
    def f(self, x):
        return 1 / x
    
    @classmethod
    def F(self, x):
        return math.log(x)


class f10(Funcio):
    @classmethod
    def f(self, x):
        return math.sqrt(x)
    
    @classmethod
    def F(self, x):
        return (2/3) * x**(3/2)
    
def comprobar_interval(a, b, f):
    if a>b:
        raise AssertionError("L'interval no es correcte")
    if f==8 and a <= 0:
        raise AssertionError("L'interval no està inclòs al domini")
    elif f==9 and (a <= 0 and b >= 0):
        raise AssertionError("L'interval no està inclòs al domini")
    elif f==10 and (a < 0):
        raise AssertionError("L'interval no està inclòs al domini")
def cons(a, b):
    return lambda f: f(a, b)


def car(f):
    def z(x, y): return x
    return f(z)


def cdr(f):
    def z(x, y): return y
    return f(z)


assert car(cons(3, 4)) == 3
assert cdr(cons(3, 4)) == 4
print(car(cons(3, 4)))
print(cdr(cons(3, 4)))

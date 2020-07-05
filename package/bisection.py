import math

def bisection(a, b, iterations):
    if type(a) is not float:
        raise Exception("a should be floatable")
    if type(b) is not float:
        raise Exception("b should be floatable")
    if type(iterations) is not int:
        raise Exception("iteration should be floatable")

    p = 0.0
    for iter in range(iterations):
        if (b - a) < 1e-4: break
        p = (a + b) / 2
        eq = lambda x: math.pow(x, 3) + 4 * math.pow(x, 2) - 10
        if eq(p) == 0.0: break
        if eq(p) > 0: b = p
        else: a = p
        print("iter = {}\ta = {:.6f}\tb = {:.6f}\tc = {:.6f}\tfn(c) = {:.6f}\ttol = {}".format(iter+1, a, b, p, eq(p), (b - a)))
    return p

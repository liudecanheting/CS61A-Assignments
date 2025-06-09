def inverse_casade(n):
    """
    >>>inverse_casade(1234)
    1
    12
    123
    1234
    123
    12
    1
    """
    grow(n)
    print(n)
    shrink(n)

def f_then_g(f,g,n):
    if n:
        f(n)
        g(n)

grow=lambda n:f_then_g(grow,print,n//10)
shrink=lambda n:f_then_g(print,shrink,n//10)


def grow(n):
    if n==0:
        return
    grow(n//10)
    print(n)

def shrink(n):
    if n==0:
        return
    print(n)
    shrink(n//10)





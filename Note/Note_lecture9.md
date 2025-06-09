# CS61A Lecture 9 Note --Tree_Recursion

## 1.相互递归与自身递归

## 2.汉诺塔问题
```py
def sove_hanoi(n,start_peg,end_peg):
    if n==1:
        move(n,start_peg,end_peg)
    else:
        spare_peg=6-start_peg-end_peg
        sove_hanoi(n-1,start_peg,spare_peg)
        move(n,start_peg,end_peg)
        sove_hanoi(n-1,spare_peg,end_peg)

def move(n,start_peg,end_peg):
    print(f"Move disk {n} from {start_peg} to {end_peg}")
```

## 3.打印问题
```py
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
```




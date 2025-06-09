# CS61A Lecture 4 Notes --Hinger-Order-Functions

## 1.斐波那契数列

0，1，1，2，3，5，8，13，21，34，55，89，144，233，377，610

```python
def fib(n):
    pred,curr=0,1
    k=1
    while k<n:
        pred,curr=curr,pred+curr
        k=k+1
    return curr
>>>fib(5)
5
```

## 2.assert

```python
>>> from math import pi
>>> def area(r,shape_constant):
...     assert r>0,'A length must be positive'
...     return r*r*shape_constant
...
>>> def area_square(r):
...     return area(r,1)
...
>>> def area_circle(r):
...     return area(r,pi)
...
>>> area_circle(2)
12.566370614359172
>>> area_circle(-2)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 2, in area_circle
  File "<stdin>", line 2, in area
AssertionError: A length must be positive
```

## 3.lambda 和 def

```python
>>> x=10
>>> square=x*x
>>> x
10
>>> square
100
>>> square=lambda x:x*x
>>> square
<function <lambda> at 0x000001C74FF85940>
>>> square(4)
16
>>> def f(x):
...     return x*x
...
>>> f
<function f at 0x000001C74FF859E0>
>>> f(4)
16
```

## 4.<consequent>if<predicate>else<alternative>

```python
>>> x=0
>>> abs(1/x if x!=0 else 0)
0
>>> x=1
>>> abs(1/x if x!=0 else 0)
1.0
```

## 5.函数的嵌套

```python
>>> from math import sqrt
>>> def real_sqrt1(x):
...     return if_(x>0,sqrt(x),0.0)
...
>>> def real_sqrt2(x):
...     if x>0:
...         return sqrt(x)
...     else:
...         return 0.0
...
>>> def if_(c,x,y):
...     if c:
...         return x
...     else:
...         return y
...
>>> real_sqrt1(4)
2.0
>>> real_sqrt1(-4)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 2, in real_sqrt1
ValueError: math domain error
>>> real_sqrt2(4)
2.0
>>> real_sqrt2(-4)
0.0
```

```python
>>> def make_adder(n):
...     def add(k):
...         return k+n
...     return add
...
>>> make_adder(1)(2)
3
>>> make_adder(2000)(13)
2013
>>> f=make_adder(2000)
>>> f
<function make_adder.<locals>.add at 0x000001DDBF6B8680>
>>> f(13)
2013
```

```python
>>> def search(f):
...     x=0
...     while True:
...             if f(x):
...                 return x
...             x+=1
...
>>> def is_three(x):
...     return x==3
...
>>> search(is_three)
3
>>> x
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'x' is not defined
```

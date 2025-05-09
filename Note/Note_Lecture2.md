# Lecture 2 Notes

## 1. Variable Swapping Example

```python
>>> a = 2
>>> b = 1
>>> a, b = a + b, a
>>> print(a, b)
3 2
```

```python
>>> a=12
>>> x=print(a+1)
13
>>> print(x+3)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'NoneType' and 'int'
>>> print((int)x+3)
  File "<stdin>", line 1
    print((int)x+3)
           ^^^^^^^
SyntaxError: invalid syntax. Perhaps you forgot a comma?
#注意：x其实是为None
```

## 2. Function Definition and Usage

```python
>>> from operator import mul
>>> def square(square):
...     x = mul(square, square)
...     return x
...
>>> square
<function square at 0x00000265C08A8680>
>>> t = 4
>>> square(t)
16
>>>y=square
>>>y
<function square at 0x00000265C08A8680>
>>>z=square(t)
>>>z
16
>>> f=square()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: square() missing 1 required positional argument: 'square'
```

## 3.全局变量和局部变量

```python
>>> x=12
>>> def f(y):
...     print(x,y)
...
>>> f(6)
12 6
>>> def t(y):
...     a=x+1
...     b=a+1
...     print(a,b)
...
>>> t(6)
13 14
>>> def g(y):
...     print(x,y,z)
...
>>> g(6)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 2, in g
NameError: name 'z' is not defined
```

```
>>> def f(x):
...     return x
...
>>> f(7)
7
>>> print(x)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'x' is not defined
```

## 4.print string

```python
>>> x="hello "+str(2)
>>> print(x)
hello 2
>>> print("hello",2)
hello 2
```

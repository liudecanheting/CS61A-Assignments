# CS61A Lecture 5 Note

## 1.本地变量，父框架

```python
>>> def f(x,y):
...     return g(x)
...
>>> def g(a):
...     return a+y
...
>>> f(1,2)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 2, in f
  File "<stdin>", line 2, in g
NameError: name 'y' is not defined #此时的y是局部变量，无法被函数g()获取，g函数的父框架是global
```

```python
>>> def f(x,y):
...     def g(x):
...         return x+y
...     return g
...
>>> f(1,2)
<function f.<locals>.g at 0x00000182631F8680>
>>> f(1,2)(3)
5
#此时g函数的父框架是f函数
```

## 2.lambda

```python
>>> f1=lambda x:x*x
>>> f2=lambda x:x+x
>>> f1
<function <lambda> at 0x00000208F705BF60>
>>> f2
<function <lambda> at 0x00000208F7054040>
```

## 3.函数的返回值是自己

```python
>>> def print_numbers(x):
...     print(x)
...     return print_numbers
...
>>> print_numbers(1)
1
<function print_numbers at 0x000001C6F87BBF60>
>>> print_numbers(1)(2)(3)
1
2
3
<function print_numbers at 0x000001C6F87BBF60>
```

```python
>>> def print_sums(x):
...     print(x)
...     def next_sums(y):
...         return print_sums(x+y)
...     return next_sums
...
>>> print_sums(1)(2)
1
3
<function print_sums.<locals>.next_sums at 0x000001C6F87B40E0>
>>> print_sums(1)(2)(3)(4)
1
3
6
10
<function print_sums.<locals>.next_sums at 0x000001C6F87B4360>
```

## 4.高阶函数

```python
>>> def curry(f):
...     def g(x):
...         def h(y):
...             return f(x,y)
...         return h
...     return g
...
>>> from operator import add
>>> curry(add)(3)(7)
10
```

## 5.局部变量和全局变量

```python
>>> def f(square):
...     x=4
...     return square(x)
...
>>> x=6
>>> t=(lambda x: x*x)
>>> f(t)
16
```

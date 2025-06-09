# CS61A Lecture 3 Notes --Control

## 1. 运算符说明

- `add(x, y)`：x + y
- `mul(x, y)`：x \* y
- `truediv(x, y)`：x / y （例如：100/3 = 33.3）
- `floordiv(x, y)`：x // y （例如：100//3 = 33）
- `mod(x, y)`：x % y
- `round(x)`:四舍五入（例如：round(1.5)=2,round(1.4)=1）

## 2. 终端直接测试 (ex.py)

```python
from operator import floordiv, mod
def divide_exact(n, d=10):
    """
    >>> q, r = divide_exact(2013)
    >>> q
    201
    >>> r
    2
    """
    return floordiv(n, d), mod(n, d)
```

```plaintext
终端运行：python3 -m doctest -v ex.py

# Terminal Output (示例，具体行号和格式可能略有不同)
****
File "ex.py", line X, in __main__.divide_exact
Failed example:
    q, r = divide_exact(2013)
Expected:
    (201, 2)
Got:
    (201, 3)
****
```

## 3.全局变量和局部变量

```python
>>> x=2
>>> def f():
...     print(x)
...     x=3 #未使用global，在局部中不能修改全局变量
...     print(x)
...
>>> f()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 2, in f
UnboundLocalError: cannot access local variable 'x' where it is not associated with a value
```

## 4.交互式模式下运行 None,无返回值

```python
>>> 12
12
>>> None
>>> print(None)
None
```

## 5.if 语句

```python
>>> if -12:
...     print(1)
...
1
>>> if 0:
...     print(1)
...
>>> if 12:
...     print(1)
```

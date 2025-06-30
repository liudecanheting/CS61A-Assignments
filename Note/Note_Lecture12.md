# CS61A Lecture 12 Notes --Trees

## 1.sum 函数

```py
>>>sum([2,3,4])
9

>>> sum(['2','3','4'])
Traceback (most recent call last):
  File "<python-input-0>", line 1, in <module>
    sum(['2','3','4'])
    ~~~^^^^^^^^^^^^^^^
TypeError: unsupported operand type(s) for +: 'int' and 'str'

>>>sum([2,3,4],5)
14

>>>sum([[2,3],[4]],[])
[2,3,4]

>>> 0+[2,3]
Traceback (most recent call last):
  File "<python-input-1>", line 1, in <module>
    0+[2,3]
    ~^~~~~~
TypeError: unsupported operand type(s) for +: 'int' and 'list'

>>>sum([])
0
```

## 2.max 函数

```py
>>> max(range(5))
4
>>> max(range(10),key=lambda x:7-(x-4)*(x-2))
3#讲0-9代入式子7-(x-4)*(x-2)，当x=3时，式子的值最大，故输出3
```

## 3.bool 判断字符串

```py
>>> bool('hello')
True
>>> bool('')
False
```

## 4.all 函数

```py
>>> [x<5 for x in range(5)]
[True, True, True, True, True] # 全为True
>>> all([x<5 for x in range(5)])
True # 全为True
>>> all([x<4 for x in range(5)])
False #有False
>>> all(range(5))
False #有0
>>>
```

## 5.特殊阶乘

```py
print((lambda n:(lambda f:f(n,f)(lambda n,fact:1 if n==1 else n*fact(n-1),fact)))(5))
#(lambda n,fact:1 if n==1 else n*fact(n-1),fact)是f(n,f)的实际函数
```

## 6.trees

```py
def tree(label,branches=[]):
    for branch in branches:
        assert is_tree(branch),
    return [label]+list(branches)

def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_tree(tree):
    if type(tree)!=list or len(tree)<1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    return not branches(tree)

def fib_tree(n):
    if n<=1:
        return tree(n)
    else:
        left,right=fib_tree(n-2),fib_tree(n-1)
        return tree(label(left)+label(right),[left,right])

def increment_leaves(t):
    if is_leaf(t):
        return tree(label(t)+1)
    else:
        bs=[increment_leaves(b) for b in branches(t)]
        return tree(label(t),bs)

def increment(t):
    return tree(label(t)+1,[increment(b) for b in branches(t)])
```

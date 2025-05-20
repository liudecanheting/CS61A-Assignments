# CS61A Project hog Notes

## 1.函数等价赋值

```python
from random import randint
def make_fair_dice(sides):
    assert type(sides)==int and sides>=1,
    def dice():
        return randint(1,sides)
    return dice
four_sided=make_fair_dice(4)
six_sided=make_fair_dice(6)
>>>six_sided()
2
>>>six_sided()
4
#因为randint,随机摇数1-6
```

## 2.nonlocal 是去引用最近外层函数的变量（非全局变量）

```python
def outer():
    x=10
    def inner():
        nonlocal x
        x=20
    print(x) #输出10
    inner()
    print(x) #输出20
```

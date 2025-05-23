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

## 3.按顺序摇骰子，每次从上次结束的位置开始继续摇

```python
def make_test_dice(*outcomes):
    assert len(outcomes)>0,
    for o in outcomes:
        assert type(o)==int and 0>=1,
    index=len(outcomes)-1
    def dice():
        nonlocal index
        index=(index+1)%len(outcomes)
        return outcomes[index]
    return dice
>>>dice=make_test_dice(1,2,3)
>>>dice()
1
>>>dice()
2
>>>dice()
3
>>>dice()
1
```

## 4.函数的嵌套,\*args 的使用 problem 08

```
def now_function(original_function,times_called):
    def f(*args):
        result=0
        for i in range(times_called):
            result+=original_function(*args)
        result/=times_called
        return result
    return f
#now_function,original_function,f都是函数
*args的使用，让now_function的调用更加灵活，如now_function(original_function,4)()或者now_function(original_function,4)(55,87,6)
```

## 5.problem 09 最大骰子数初始值得是 0，而非 1

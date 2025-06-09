# CS61A Lab 02 Note --Lambda Expression

## 1.布尔运算符 and,or,not

and 运算符会返回第一个假值，如果全为真值，则返回最后一个值
or 运算符会返回第一个真值，如果全为假值，则返回最后一个值
not 运算符会将真值变成假，假值变为真

```python
 >>> True and 13
 13#True为真，13为真，返回最后一个值13
 >>> False or 0
 0#False为假，0为假，返回最后一个值0
 >>> not 10
 False#10为真，not 10为假
 >>> not None
 True
 >>> print(3) or ''
 3
 >>> def f(x):
...     if x==0:
...         return 'zero'
...     elif x>0:
...         return 'positive'
...     else:
...         return 'negetive'
...
>>> f(0) or f(-1)
'zero'#返回第一个真值'zero'
 ''
```

## 2.高阶函数

```python
>>> def cake():
...    print('beets')
...    def pie():
...        print('sweets')
...        return 'cake'
...    return pie
>>> chocolate = cake()
? beets
>>> chocolate
? Function
>>> chocolate()
(line 1)? sweets
(line 2)? 'cake'
>>> more_chocolate, more_cake = chocolate(), cake
? sweets
-- OK! --
>>> more_chocolate
? 'cake'
>>> def snake(x, y):
...    if cake == more_cake:
...        return chocolate
...    else:
...        return x + y
>>> snake(10, 20)
? Function
-- OK! --

>>> snake(10, 20)()
(line 1)? sweets
(line 2)? 'cake'
```

## 3.range(0)表示(0,0),不包括任何数

```python
def cycle(f1, f2, f3):
    def g(n):
        def f(x):
            value=x
            for i in range(n):
                if i%3==0:
                    value=f1(value)
                elif i%3==1:
                    value=f2(value)
                elif i%3==2:
                    value=f3(value)
            return value
        return f
    return g
```

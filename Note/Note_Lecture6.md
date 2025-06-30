# CS61A Lecture 6 Notes --Design

## 1.python 中的浮点数比较

```python
>>> 5.5==5.50
True
>>> 1/3+1/3+1/3+1/3+1/3==5/3
False
>>> 5/3
1.6666666666666667
>>> 1/3+1/3+1/3+1/3+1/3
1.6666666666666665
```

## 2.环境图

![alt text](<屏幕截图 2025-05-27 122059.png>)

## 3.高阶函数

```python
def announce_lead_changes(last_leader=None):
    def say(score0,score1):
        if score0>score1:
            leader=0
        elif score0<score1:
            leader=1
        else:
            leader=None
        if leader!=None and leader!=last_leader:
            print('Player',leader,'takes the lead by',abs(score0-score1))
        return announce_lead_changes(leader)
    return say
>>>f0=announce_lead_changes()
>>>f1=f0(5,0)
>>>Player 0 takes the lead by 2
>>f2=f1(5,12)
>>>player 1 takes the lead by 7
>>>f3=f2(8,12)
>>>f4=f3(8,13)
>>>f5=f4(15,13)
Player 0 takes the lead by 2
```

## 4.用递归来写斐波那契数列是如此的低效

```python
>>> def fib(n):
...     if n==1 or n==0:
...         return n
...     else:
...         return fib(n-1)+fib(n-2)
...
>>> def decor(f):
...     def counted(*args):
...         counted.call_count+=1
...         return f(*args)
...     counted.call_count=0
...     return counted
...
>>> fib(6)
8
>>> f=decor(fib)
>>> fib=decor(fib)
>>> f(6)
8
>>> f.call_count
1#f是装饰后的fib，但原始fib未变
>>> fib(6)
8
>>> fib.call_count
49#将原始fib替换为装饰版本
```

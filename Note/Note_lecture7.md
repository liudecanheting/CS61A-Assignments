# CS61A Lecture 7 Note --Function Examples
## 1.从环境模型推导原始代码

```python
>>> def flip(flop):
...     if flop>2:
...         return None
...     flip=lambda flip:3
...     return flip#判断函数
...
>>> def flop(flip):
...     return flop#返回自己本身函数的函数
...
>>> flip,flop=flop,flip
>>> flip(flop(1)(2))(3)
```
1.flop(1),此时的flop等同于“判断函数”，返回一个lambda函数
2.flop(1)(2),此时返回3
3.flip(flop(1)(2))等同于flip(3),然后返回flop函数，即判断函数
4.flip(flop(1)(2))(3)等同于flop(3),调用判断函数,因为3>2,最后返回None
**但是，流程图中第三部返回的是“判断函数”，额，我很疑惑**

## 2.删去指定数字后，顺序变还是不变
### 1.不变
```python
def remove(n,num):
    kept,digits=0,0
    while n>0:
        n,last=n//10,n%10
        if last!=num:
            kept=kept+last*10**digits
            digits+=1
    return kept
print(remove(325613,3))
2561
```
### 2.变，逆序
```python
def remove(n,num):
    kept,digits=0,0
    while n>0:
        n,last=n//10,n%10
        if last!=num:
            kept=kept*10+last
            digits+=1
    return kept
print(remove(325613,3))
1652
```

## 3.ucb中的trace--python装饰器与跟踪
放在函数上方，“函数的调用，函数的参数，函数的返回”都会被打印出来

## 4.装饰器函数
一种快速转换函数的方式，或者追踪函数
```
def trace1(fn):
    def traced(x):
        print('Calling',fn,'with argument',x)
        return fn(x)
    return traced

@trace1
def square(x):
    return x*x#等同于def square(x):
              #          return x*x
              #      square=trace1(square)


@trace1
def sum_squares_up_to(n):
    k=1
    total=0
    while k<=n:
        total,k=total+square(k),k+1
    return total    
$ py -i try_write.py
>>> square(12)
Calling <function square at 0x000001C3023CCB80> with argument 12
144
>>> sum_squares_up_to(5)
Calling <function sum_squares_up_to at 0x000001C302416D40> with argument 5
Calling <function square at 0x000001C3023CCB80> with argument 1
Calling <function square at 0x000001C3023CCB80> with argument 2
Calling <function square at 0x000001C3023CCB80> with argument 3
Calling <function square at 0x000001C3023CCB80> with argument 4
Calling <function square at 0x000001C3023CCB80> with argument 5
55
```

## 5.寻找重复数字，通过高阶函数,使用闭包来维护状态
```python
def repeat(k):
    return detector(lambda j:False)(k)

def detector(f):
    def g(i):
        if f(i):
            print(i)
        return detector(lambda j:j==i)
    return g

repeat(1)(3)(1)(4)(4)
4
```
## 6.函数中嵌套函数
```python
pumbaa(pumbaa)(timon)   (5)
apply_4_times(timon)    (5)
(timon(timon(timon(timon(5)))))
```

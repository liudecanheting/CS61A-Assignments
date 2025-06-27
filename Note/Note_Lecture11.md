# CS61A Lecture 11 Note --Data_Abstraction
## 1.列表
```py
>>>pair=[1,2]
>>>a,b=pair
>>>a
1
>>>pair[0]
1
```

## 2.rational(),numer(),denom() Scheme编程
rational(n,d) 返回一个列表[n,d]
numer(x) 返回分数x的分子
denom(x) 返回分数x的分母
```py
def rational(n,d):
    def select(name):
        if name=='n':
            return n
        elif name=='d':
            return d
    return select

def numer(x):
    return x('n')

def denom(x):
    return x('d')
```    

## 3.字典
```py
>>> numerals={'a':4,'c':6,'e':9}
>>> numerals.keys()
dict_keys(['a', 'c', 'e'])
>>> numerals.values()
dict_values([4, 6, 9])
>>> numerals.items()
dict_items([('a', 4), ('c', 6), ('e', 9)])
>>> {x:x*x for x in range(10)}
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
>>>{1:2,1:3}
{1:3} #一个键只能对于一个值，字典和列表都不能当键
```
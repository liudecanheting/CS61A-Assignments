# CS61A Lecture 10 Note --Containers

## 1.数据类型不同，不相等
```py
>>>'1'==1
False
```
## 2.列表中的列表
```py
>>>pairs=[[1,1],[2,1],[3,2],[4,4]]
>>>same_count=0
>>>for x,y in pairs:
        if x==y:
            same_count+=1
>>>same_count
2
```
## 3.列表的增添
```py
>>>odds=[1,3,5,7]
>>>[x+1 for x in odds]
[2,4,6,8]
```
## 4.区分列表和字符串
```py
>>>'here' in 'where is waaldo'
True
>>>234 in  [1,2,3,4,5]
False
>>>[2,3,4] in [1,2,3,4,5]
False
```
## 5.\t
```py
>>>len('hello\tworld')
11
>>>print('hello\tworld')
hello  world
```
## 6.列表的切片
```py
>>> t=[5,3,5,6]
>>> t[1:-1:-1]
[]
>>> t[-1:1:-1]
[6, 5]
```
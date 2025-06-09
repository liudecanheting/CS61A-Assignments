# Lab 01 Notes -- Functions

## 1.test1

```python
>>> def bake(cake,make):
...     if cake==0:
...             cake=cake+1
...             print(cake)
...     if cake==1:
...             print(make)
...     else:
...         return cake
...     return make
...
>>> bake(1,"mashed potatoes")
mashed potatoes
'mashed potatoes'
>>> bake(0,29)
1
29
29
```

## 2.test2

```python
>>> def welcome():
...     print("Go")
...     return "hello"
...
>>> def cal():
...     print("bears")
...     return "world"
...
>>> welcome()
Go
'hello'
>>> print(welcome(),cal())
Go
bears
hello world
```

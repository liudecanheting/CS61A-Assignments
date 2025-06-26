# CS61A Lab 03 Notes --Recursion + Python_lists

## 1.列表中的列表

```py
s=[1,3,[2,4],5]
# 2 not in s
# 2 in s[2]
```

```py
>>>[[1]+s for s in [[4],[5,6]]]
[[1,4],[1,5,6]]
```

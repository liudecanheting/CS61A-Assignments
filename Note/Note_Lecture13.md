# CS61A Lecture 13 Notes --Binary_Numbers

## 1.min()函数

```py
>>> f=lambda x:abs(x*x-24)
>>> [f(x) for x in [3,2,5,6]]
[15, 20, 1, 12]
>>> [[f(x),x] for x in [3,2,5,6]]
[[15, 3], [20, 2], [1, 5], [12, 6]]
>>> min([[f(x),x] for x in [3,2,5,6]])
[1, 5]
>>> min([[f(x),x] for x in [3,2,5,6]])[1]
5
```

## 2.列表比较大小，是比较第一个元素

```py
>>> [12,4]<[13,2]
True
```

## 3.计算机底层原理

| position | complement |  +1 | negetive |
| :------- | :--------: | --: | -------- |
| 0 000    |    111     | 000 | 0        |
| 1 001    |    110     | 111 | -1       |
| 2 010    |    101     | 110 | -2       |
| 3 011    |    100     | 101 | -3       |

**但是**0010（也就是 2）+1010（也就是-2）==1100（也就是 0），该说法是错误的，绝不会那么简单

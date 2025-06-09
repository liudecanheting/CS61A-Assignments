# HW 03 --Notes

## 1.不用取模，不用循环，从 1 开始

````py
def interleaved_sum(n, odd_func, even_func):
    """Compute the sum odd_func(1) + even_func(2) + odd_func(3) + ..., up
    to n.
    """
    def find(k,is_odd):
        if k>n:
            return 0
        if is_odd:
            return odd_func(k)+find(k+1,False)
        else:
            return even_func(k)+find(k+1,True)
    return find(1,True)
    ```
````

## 2.纸币计数

```py
def count_dollars(total):
    def count(total,max_bill):
        if total==0:
            return 1
        elif total<0:
            return 0
        elif max_bill==None:
            return 0
        else:
            a=count(total,next_smaller_dollar(max_bill))#不选择当前面额的纸币
            b=count(total-max_bill,max_bill)#选择当前面额的纸币
            return a+b
    return count(total,100)
```

## 3.用 lambda 来写阶乘(匿名递归)

```py
def make_anonymous_factorial():
    """
    >>> make_anonymous_factorial()(5)
    120
    """
    return (lambda f: f(f))(lambda f: lambda x: 1 if x == 0 else x * f(f)(x - 1))
```

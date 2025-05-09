def digit(n, k):
    """从n的右侧返回k的数字，用于正整数n和k。

    >>> digit(3579, 2)
    5
    >>> digit(3579, 0)
    9
    >>> digit(3579, 10)
    0
    """
    n=str(n)
    len_n=len(n)
    x=0
    if len_n>k:
        x=n[-(k+1)]     
    print(x)


def middle(a, b, c):
    """返回不是最小或最大的A，B和C中的数字。
    假设A，B和C都是不同的数字。

    >>> middle(3, 5, 4)
    4
    >>> middle(30, 5, 4)
    5
    >>> middle(3, 5, 40)
    5
    >>> middle(3, 5, 40)
    5
    >>> middle(30, 5, 40)
    30
    """
    max_num=max(a,b,c)
    min_num=min(a,b,c)
    if a!=max_num and a!=min_num:
        result=a
    elif b!=max_num and b!=min_num:
        result=b
    else:
        result=c
    print(result)


def falling(n, k):
    """计算n到深度k的下降阶乘.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    "*** YOUR CODE HERE ***"
    result=1
    while k>0:
        result*=n
        n-=1
        k-=1
    print(result)
        
    


def divisible_by_k(n, k):
    """
    >>> a = divisible_by_k(10, 2)  ＃2、4、6、8和10被2排除
    2
    4
    6
    8
    10
    >>> a
    5
    >>> b = divisible_by_k(3, 1)  # 1, 2, and 3 are divisible by 1
    1
    2
    3
    >>> b
    3
    >>> c = divisible_by_k(6, 7)  ＃没有7个整数可分开7
    >>> c
    0
    """
    "*** YOUR CODE HERE ***"
    
    i=1
    count=0
    while i<=n:
        if i%k==0:
            print(i)
            count+=1
        i+=1
    print(count)
            
        
        


def sum_digits(y):
    """Sum all the digits of y.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> a = sum_digits(123) # make sure that you are using return rather than print
    >>> a
    6
    """
    "*** YOUR CODE HERE ***"
    y=str(y)
    len_y=len(y)
    i=0
    result=0
    while i<len_y:
        result+=y[i]
    print(result)


def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    "*** YOUR CODE HERE ***"
    n=str(n)
    len_n=len(n)
    i=0
    count=0
    ok= False
    while i<len_n:
        if n[i]=='8':
            count+=1
        i+=1
    if count==2:
        ok=True
    print(ok)
        
    
    
    


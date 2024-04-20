def factorial(num):
    i=num
    res=1
    if num%1==0:
        while i>0:
            res=i*res
            i=i-1
    print(res)
    


factorial(3)
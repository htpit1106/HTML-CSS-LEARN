def kiem_tra_fibonacci(n):
    a = 0
    b = 1
    while b < n:
        temp = a
        a = a+b
        b = temp
    if b%2 ==0 and b == n :
        return True
    else:
        return False

num = 9969216677189303386214405760200
if kiem_tra_fibonacci(num):
    print(f"{num} thuộc dãy Fibonacci chan")
else:
    print(f"{num} không thuộc dãy Fibonacci chan")

# Print factorial using recursion


# def cal_func(x):
#     if x == 1:
#         return 1
#     else:
#         return x * cal_func(x - 1)
#
#
# print(cal_func(4))


# Print fibonacci


# def fib(n:'upto n number')->int:
#     if n==0:
#         return 0
#     elif n==1:
#         return 1
#     a=0
#     b=1
#     for i in range(0,n-1):
#         b=a+b
#         a=b-a
#     return b
# n =5
# for i in range(n):
#     print(fib(i))






def fibonacci(n):
    if n <= 1:
        return n
    else:
        return (fibonacci(n -1) + fibonacci(n-2))

# n = int(input("Enter the value of n: "))
#
# for i in range(n):
print(fibonacci(5))
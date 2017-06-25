# 0, 1, 1, 2, 3, 5, 8, 13,...

# return n's fibonacci number

# recursive
def fibonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 2) + fibonacci(n - 1)

print fibonacci(8)

# loop
def fibonacci2(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        i = 3
        f_n_2 = 0
        f_n_1 = 1
        while i <= n:
            f_n = f_n_2 + f_n_1
            f_n_2 = f_n_1
            f_n_1 = f_n
            i += 1
    return f_n

print fibonacci2(8)


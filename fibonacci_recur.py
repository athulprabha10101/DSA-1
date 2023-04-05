# nth fib number == fib num at n-1 + fib num at n-2
# ie, fibo(5) == fibo(4) + fibo(3)
import time
st = time.time()
def fibo(n):
    if n < 2:
        return n
    return fibo(n - 1) + fibo(n - 2)



print(fibo(37))
et = time.time()
print(et - st)
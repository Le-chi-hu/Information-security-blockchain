import random
from math import gcd

def pollards_rho_floyd(g, h, p, n, max_attempts=5):



    def partition(x):
  
        if x % 3 == 0:
            return 0
        elif x % 3 == 1:
            return 1
        else:
            return 2

    def f(x, a, b):
        part = partition(x)
        if part == 0:
            x = (h * x) % p
            b = (b + 1) % n
        elif part == 1:
            x = (x * x) % p
            a = (2 * a) % n
            b = (2 * b) % n
        else:
            x = (g * x) % p
            a = (a + 1) % n
        return x, a, b

    for attempt in range(max_attempts):
        
        x_t, a_t, b_t = g, 1, 0  
        x_h, a_h, b_h = g, 1, 0  

        for i in range(1, 2 * n):

            x_t, a_t, b_t = f(x_t, a_t, b_t)
  
            x_h, a_h, b_h = f(*f(x_h, a_h, b_h))

            if x_t == x_h:
     
                r = (a_t - a_h) % n
                s = (b_h - b_t) % n

                if s == 0 or gcd(s, n) != 1:
                    print(f"[嘗試 {attempt+1}] s 不可逆，重試")
                    break

                try:
                    s_inv = pow(s, -1, n)
                    x_result = (r * s_inv) % n
                    return x_result
                except ValueError:
                    print(f"[嘗試 {attempt+1}] 模反元素錯誤，重試")
                    break

    raise ValueError(" 超過最大嘗試次數，仍未找到解")


if __name__ == "__main__":
    import time


    p = 58002118547
    n = 29001059273
    g = 13513236970
    h = 39818986975

    print("開始執行 Floyd-Pollard rho DLP")

    try:
        x = pollards_rho_floyd(g, h, p, n)
        print(f" 找到的 x = {x}")
        print(f" 驗證：{g}^{x} mod {p} = {pow(g, x, p)}")
    except ValueError as e:
        print(e)


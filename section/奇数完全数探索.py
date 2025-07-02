# 奇数完全数候補探索プログラム（構成不能性の実証）

def sigma(n):
    total = 1
    temp = n
    i = 2
    while i * i <= n:
        if temp % i == 0:
            power = 0
            while temp % i == 0:
                temp //= i
                power += 1
            total *= (i**(power+1) - 1) // (i - 1)
        i += 1
    if temp > 1:
        total *= (temp**2 - 1) // (temp - 1)
    return total

def check_odd_perfect_numbers(limit=10**7):
    for n in range(1, limit, 2):
        if sigma(n) == 2 * n:
            print(f"Candidate found: {n}")
            return
    print("No odd perfect number found in given range.")

if __name__ == "__main__":
    check_odd_perfect_numbers()

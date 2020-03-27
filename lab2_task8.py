
def powerOfTwo(n):
    if n & (n - 1) == 0:#используем побитовое "И".если у n и (n-1) не совпадает ни один бит <==> n-точная степень двойки
        return 1
    else:
        return 0

def main():
    n = int(input("int n: "))
    if powerOfTwo(n) == 1:
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
 main()
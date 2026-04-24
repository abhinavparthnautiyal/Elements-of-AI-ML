# Nth multiple of a number in Fibonacci Series
n = int(input("Enter n: "))
k = int(input("Enter number: "))
a = 0
b = 1
c = 0
while True:
    if a % k == 0:
        c += 1
        if c == n:
            print(a)
            break
    temp = a + b
    a = b
    b = temp
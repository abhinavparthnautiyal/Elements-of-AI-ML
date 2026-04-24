# Check if a given number is Fibonacci number
n = int(input("Enter a number: "))
a = 0
b = 1
while a < n:
    c = a + b
    a = b
    b = c
print(a == n)
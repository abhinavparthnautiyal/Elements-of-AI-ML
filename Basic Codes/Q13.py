# Sum of squares of first n natural numbers
n = int(input("Enter n: "))
s = 0
for i in range(1, n + 1):
    s += i * i
print(s)
# Check Armstrong Number
n = int(input("Enter a number: "))
temp = n
power = len(str(n))
s = 0
while temp > 0:
    d = temp % 10
    s += d ** power
    temp //= 10
print(s == n)
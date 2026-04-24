# Find compound interest
p = float(input("Enter principal: "))
r = float(input("Enter rate: "))
t = float(input("Enter time: "))
print(p * ((1 + r / 100) ** t))
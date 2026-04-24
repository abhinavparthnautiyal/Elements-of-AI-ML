# Print all Prime numbers in an Interval
l = int(input("Enter lower bound: "))
u = int(input("Enter upper bound: "))
for num in range(l, u + 1):
    if num > 1:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                break
        else:
            print(num)
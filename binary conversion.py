num = int(input("Enter a number: "))

n = num
binary = ""

while n > 0:
    digit = n % 2
    n = n // 2

    for k in range(1):
        binary = str(digit) + binary

print("Binary of", num, "=", binary)

base = int(input("Enter a base number: "))

exp = int (input("Enter an exponent: "))

result = 1

for i in range (exp):
    result = result * base

print ("Result is: ",result)
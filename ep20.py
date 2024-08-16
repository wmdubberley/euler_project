n = 100
total=1
for i in range(1,n+1):
    total = total * i
    
print(total)
digits = [int(digit) for digit in str(total)]
print(digits)
print(sum(digits))
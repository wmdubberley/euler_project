def is_prime(n):
  for i in range(2,n):
    if (n%i) == 0:
      return False
  return True

limit=2_000_000

sumofprime=0
for i in range(2,limit):
    
   if is_prime(i):
        sumofprime+=i
        print(f"{i} - {sumofprime}")
        
print(sumofprime)
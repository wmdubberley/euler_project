from util import is_prime

limit=2_000_000

sumofprime=0
for i in range(2,limit):
    
   if is_prime(i):
        sumofprime+=i
        print(f"{i} - {sumofprime}")
        
print(sumofprime)
from util import is_prime

index=0
position = 10001
n=1
while index < position:
    n+=1 
    if is_prime(n):
        index+=1
    if index==position:
        print(n)
       
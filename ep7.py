def is_prime(n):
  for i in range(2,n):
    if (n%i) == 0:
      return False
  return True

index=0
position = 10001
n=1
while index < position:
    n+=1 
    if is_prime(n):
        index+=1
    if index==position:
        print(n)
       
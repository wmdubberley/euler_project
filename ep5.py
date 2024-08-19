cont=True
n=0
x=0
start=1
end=20
while cont:
    n+=1
    for i in range(start, end+1):
        if n % i == 0:
            x=n
            # print(f"{n} is divisiable by {i}")
        else:
            x=0
            break
    if x>0:
        print(f"Smallest number divisable numbers between {start} and {end} is {x}")
        cont=False
        

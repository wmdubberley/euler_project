from util import get_square

start = 1
end = 100

r1=0
x=0

for i in range(start,end + 1):
    r1+=get_square(i)
    x+=i
r2=get_square(x)
print(f"{r2} - {r1} = {r2-r1}")
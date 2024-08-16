start = 2
end = 100
x=[]
for a in range(start,end+1):
    print(a)
    for b in range(start,end+1):
        print(f"{a} raised to the power of {b} = {a ** b}")
        x.append(a ** b)
print(x)
print(len(x))
distinct_values = set(x)
print(len(distinct_values))
base="0."
for i in range(1,1_000_000+1):
    base+=str(i)
product=int(base[1+1])*int(base[1+10])*int(base[1+100])*int(base[1+1_000])*int(base[1+10_000])*int(base[1+100_000])*int(base[1+1_000_000])    
print(product)
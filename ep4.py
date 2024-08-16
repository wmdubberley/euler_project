largest =0
for x in range(100,1000):
    for y in range(100,1000):
        xy=x*y
        if str(xy)==str(xy)[::-1]:
            if xy>largest:
                largest=xy
                print(f"{x} * {y} = {xy}")  
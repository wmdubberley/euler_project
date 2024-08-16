import inflect

# Create an inflect engine
p = inflect.engine()
start = 1
end = 1000
count=0
for i in range(start,end+1):
    word=p.number_to_words(i)
    # print(word)
    count+=len(word.replace(" ", "").replace("-", ""))
print(count)
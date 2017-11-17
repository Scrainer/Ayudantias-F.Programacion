a=[12,23,14,50,30]
for i in range(0,len(a)):
    if a[i]%2==0:
        a.pop(i)
print(a)
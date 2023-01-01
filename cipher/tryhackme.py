'''x= '9e2d96i'
j = list(x)
for i in range (len(x)):
        j[i] = chr(ord(j[i])-i)
        x=''.join(j)
print(x)'''

x = [12,24,34,53,5,6,6,745,453]
target = 751
j = list(x)
ans = []
n = 0
c = 0
b = 0
e = 0
for r in range (len(x)):
        n = target - j[r]
        for v in range (r+1,len(x)):
                if (n == j[v]):
                        c = v
                        b = 1
                        break
        if (b==1):
            e = r
            break
ans = [e,c]

print(ans)
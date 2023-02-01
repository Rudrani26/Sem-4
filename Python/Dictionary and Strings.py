'''
t = (4, 5, 6, 2, 3, 4, 5, 1, 2, 6, 4)

d = {}
for i in t:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

print(d)

'''
d = {1: "www.yahoo.com", 2: "www.tsec.edu", 3: "www.asp.net", 4: "www.abcd.in"}

t = []
for url in d.values():
    suffix = url.split(".")[-1]
    t.append(suffix)

print(t)

s = set()

for i in range(1, 10001):
    l = [int(j) for j in str(i)]
    i += sum(l)
    s.add(i)

ans = sorted(set(range(1, 10001)) - s)

for i in ans:
    print(i)

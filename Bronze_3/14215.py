a = list(map(int, input().split()))
a.sort()
a[2] = a[2] if a[0]+a[1] > a[2] else a[0]+a[1] - 1
print(sum(a))
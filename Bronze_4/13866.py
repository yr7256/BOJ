lst = list(map(int, input().split()))
lst.sort()
print(abs(lst[3]-lst[2]-lst[1]+lst[0]))

T = int(input())
for i in range(T):
    n = bin(int(input()))[2:][::-1]
    for i in range(len(n)):
        if n[i] == '1':
            print(i, end=' ')

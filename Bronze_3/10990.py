N = int(input())
print(' '*(N-1)+'*')
for i in range(1,N):
    print(' '*(N-1-i)+'*'+' '*(2*i-1)+'*')
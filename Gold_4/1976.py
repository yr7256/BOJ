import sys
input = sys.stdin.readline


def find_root(x):
    if x != nums[x]:  # 루트 찾아야 하는 경우 (그냥 자기가 루트면 찾을 필요x)
        nums[x] = find_root(nums[x])  # 계속 들어가자
    return nums[x]


N = int(input())
M = int(input())
nums = [i for i in range(N)]
routes = [list(map(int, input().split())) for _ in range(N)]
target = list(map(int, input().split()))
for i in range(N):
    for j in range(N):
        if routes[i][j]:
            s, e = min(find_root(i), find_root(j)), max(
                find_root(i), find_root(j))
            nums[e] = s
start = nums[target[0]-1]
for i in range(1, M):
    if nums[target[i]-1] != start:
        print('NO')
        break
else:
    print('YES')

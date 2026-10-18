a = set(map(int, input().split()))
n = int(input())
result = True

for _ in range(n):
    other = set(map(int, input().split()))

    if not a.issuperset(other) or a == other:
        result = False
        break
print(result)

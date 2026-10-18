n = int(input())
a = set(map(int, input().split()))

number_of_operations = int(input())

for _ in range(number_of_operations):
    operation, length = input().split()
    other = set(map(int, input().split()))

    if operation == "intersection_update":
        a.intersection_update(other)
    elif operation == "update":
        a.update(other)
    elif operation == "symmetric_difference_update":
        a.symmetric_difference_update(other)
    elif operation == "difference_update":
        a.difference_update(other)

print(sum(a))

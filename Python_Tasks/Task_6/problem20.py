import re

if __name__ == '__main__':
    n = int(input())

    for _ in range(n):
        phone = input().strip()

        if re.fullmatch(r'[789][0-9]{9}', phone):
            print("YES")
        else:
            print("NO")

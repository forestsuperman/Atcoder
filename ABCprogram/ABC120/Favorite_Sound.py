import math
a, b, c = map(int, input().split(' '))
max_count = math.floor(b/a)
if max_count <= c:
    print(max_count)
else:
    print(c)
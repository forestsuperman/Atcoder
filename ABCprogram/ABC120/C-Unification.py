S = input()
S_list = []
i = 0
for s in S:
    S_list.append(s)

count_0 = S_list.count('0')
count_1 = S_list.count('1')

counter = 2 * min(count_0, count_1)
print(counter)
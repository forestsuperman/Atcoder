A, B, K = map(int, input().split(' '))
A_set = set()
B_set = set()
for number in range(1, A+1):
    if A%number == 0:
        A_set.add(number)

for number in range(1, B+1):
    if B%number == 0:
        B_set.add(number)

A_Bset = A_set & B_set
A_Blist = list(A_Bset)
A_Blist.sort(reverse=True)
print(A_Blist[K-1])
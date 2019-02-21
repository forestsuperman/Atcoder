N = int(input())
numbers= list(map(int, input().split( )))
counter2 = 0

while(1):
    counter1 = 0
    for number in numbers:
        if number%2 == 0:
            counter1 += 1
    if counter1 == N:
        numbers = list(map(lambda x: int(x/2), numbers))
    else:
        break
    counter1 = 0
    counter2 += 1

print(counter2)
#input int a or b c and string
#out put a+b+c string
a = int(input())
b, c = map(int, input().split( ))
s = input()
print("{} {}".format(a+b+c, s))

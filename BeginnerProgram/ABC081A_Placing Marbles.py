# example input 010 > 1 110>2 111>3
# count "1"
counter = 0
number_string = input()
for number in number_string:
    if number == "1":
        counter += 1
print(counter)
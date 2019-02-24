def max_number(total_number, numbers):
    max_number = total_number/numbers
    if max_number > numbers:
        return numbers
    else:
        return max_number

A = int(input()) * 500
B = int(input()) * 500
C = int(input()) * 500
X = int(input())

A_max = max_number(X, A)
B_max = max_number(X, B)
C_max = max_number(X, B)
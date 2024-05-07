# def print_line():
#     return '-' * 20


# def print_lines(num):
#     i = 0
#     while i < num:
#
#         i += 1
#         print(print_line(),i)
#
#
# print_lines(int(input()))

def sum_number(a, b, c):
    return a+b+c


def average_number(a, b, c):
    return sum_number(a, b, c)/3


f, d, e = map(int, input().split())
print(average_number(f, d, e))


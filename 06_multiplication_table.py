"""
Home task. Multiplication table.

Given 0 < number (integer) <= 11
You need to print multiplication table based on this number

Example: num=5
Output:
#  1   2   3   4   5
#  2   4   6   8  10
#  3   6   9  12  15
#  4   8  12  16  20
#  5  10  15  20  25
"""
#
#
# # def multi_table_map(x):
# #     """Creates a multiplication table by map."""
# #     for i in range(1, x + 1):
# #         print(*list(map(lambda x: i * x, list(range(1, x + 1)))))
#
#
# def multi_table_list(x):
#     """Create a multiplication table by list comprehensions."""
#     for i in range(1, x + 1):
#         print(*[y * i for y in list(range(1, x + 1))], sep='  ')


num = 5
alignment = len(str(num**2))
for i in range(1, num + 1):
    print(' '.join(f'{x:{alignment}}' for x in range(i, i * num + 1, i)))

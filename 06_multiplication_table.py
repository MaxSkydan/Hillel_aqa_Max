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

num = 6

#
# def multi_table_map(x):
#     """Функція яка створює таблицю множення."""
#     for i in range(1, x + 1):
#         print(*list(map(lambda x: i * x, list(range(1, x + 1)))))


def multi_table_list(x):
    """Функція яка створює таблицю множення."""
    for i in range(1, x + 1):
        print(*[y * i for y in list(range(1, x + 1))], sep='  ')


# multi_table_map(num)
multi_table_list(num)

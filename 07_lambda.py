"""
Home task. Lambda.

Given: list of integers/floats
with lambda function as one of the element inside list
Write function that will produce new list by applying lambda
to all integers and floats
Input: [lambda a: a + 2, 9, 3, 1, 0]
Output: [11, 5, 3, 2]

Input: [9, 2, 3, lambda a: a / 2.0, 1, 0]
Output: [4.5, 1, 1.5, 0.5, 0.0]
"""

l1 = [lambda a: a + 2, 9, 3, 1, 0]
l2 = [9, 2, 3, lambda a: a / 2.0, 1, 0]
l3 = [lambda a: a + 2, 9.5, 3.7, 1.8, 0.2, 4.5]


def magic_num(element):
    """Create a new list using a lambda for all symbol of list."""
    new_list = element.copy()
    for idx, el in enumerate(new_list):
        if type(el) not in (int, float):
            func = new_list.pop(idx)
            output = [func(x) for x in new_list]
            return output


print(magic_num(l2))

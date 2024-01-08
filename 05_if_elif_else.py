"""
Home task 7. If elif else.

given values w,x,y,z
write if-elif-else statement that will search minimum value and
print smth aka 'y' is minimum value'
where 'y' is variable name (not value)
advice use python debugger and different values to check your algorithm
optionally you can check your algorithm somehow with assert statements.
"""

import logging

_log = logging.getLogger()
console_handler = logging.StreamHandler()
log_format = logging.Formatter('[%(asctime)s %(levelname)s]: %(message)s')
console_handler.setFormatter(log_format)
_log.addHandler(console_handler)
_log.setLevel(logging.DEBUG)

w, x, y, z = 100, 200, 40, 300
text = 'is minimum value'
text_2 = 'are minimal and equal'
min_num = min(w, x, y, z)

# if_elif_else statement
if min_num == w and min_num == x and min_num == y and min_num == z:
    _log.info(f'All values {text_2}')
elif min_num == w or min_num == x or min_num == y or min_num == z:
    if min_num == w and min_num == z and min_num == y and min_num != x:
        _log.info(f'"w" , "y" and "z" {text_2}')
    elif min_num == w and min_num == x and min_num == y and  min_num != z:
        _log.info(f'"w" , "x" and "y" {text_2}')
    elif min_num == x and min_num == y and min_num == z and min_num != w:
        _log.info(f'"x" , "y" and "z" {text_2}')
    elif min_num == w and min_num == x and min_num == z and min_num != y:
        _log.info(f'"w" , "x" and "z" {text_2}')
    elif min_num == w and min_num == x and min_num != y and min_num != z:
        _log.info(f'"w" and "x" {text_2}')
    elif min_num == w and min_num == y and min_num != x and min_num != z:
        _log.info(f'"w" and "y" {text_2}')
    elif min_num == w and min_num == z and min_num != y and min_num != x:
        _log.info(f'"w" and "z" {text_2}')
    elif min_num == x and min_num == y and min_num != w and min_num != z:
        _log.info(f'"x" and "y" {text_2}')
    elif min_num == x and min_num == z and min_num != y and min_num != w:
        _log.info(f'"x" and "z" {text_2}')
    elif min_num == z and min_num == y and min_num != x and min_num != w:
        _log.info(f'"z" and "y" {text_2}')
    elif min_num != w and min_num != z and min_num != x:
        _log.info(f'"y" {text}')
    elif min_num != w and min_num != z and min_num != y:
        _log.info(f'"x" {text}')
    elif min_num != x and min_num != y and min_num != z:
        _log.info(f'"w" {text}')
    else:
        _log.info(f'"z" {text}')
else:
    _log.info('We have a problem')

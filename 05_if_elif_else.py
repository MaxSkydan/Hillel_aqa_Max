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
text = "'y' is minimum value'"
text_2 = "'y' isn`t minimum value'"


# if_elif_else statement
if y < x and y < w and y < z:
    _log.info("'y' is minimum value'")
elif y > x and y > w and y > z:
    _log.info("'y' is max value'")
elif y == x and y == w and y == z:
    _log.info('All values are equal')
else:
    _log.info("'y' isn't minimum or max or equal value'")

# if_else statement, but in 1 line
_log.info(text) if all((y < x, y < w, y < z)) else _log.info(text_2)

# assert statement
assert all((y < x, y < w, y < z)), f'{y} isn`t minimum value'

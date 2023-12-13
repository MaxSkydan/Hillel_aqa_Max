"""Hometask format and f-strings.

we have norway text in old style formatting
re-write the same text as:
1 string with format() call
2 f-string
use linter(https://github.com/wemake-services/wemake-python-styleguide)
to check your new created python module for possible linter errors
try to run code from pycharm/command line.
"""

import logging

_log = logging.getLogger()
console_handler = logging.StreamHandler()
log_format = logging.Formatter('[%(asctime)s %(levelname)s]: %(message)s')
console_handler.setFormatter(log_format)
_log.addHandler(console_handler)
_log.setLevel(logging.DEBUG)

"""Old style"""
norway_text = ('Automatisering akselererer %syeblikket '
               'da roboter vil erobre planeten v%sr. (%s)' % ('ø', 'å', 'Æ'))
_log.info(norway_text)

"""Format"""
text_format = ('Automatisering akselererer {0}yeblikket '
               'da roboter vil erobre planeten v{1}r. ({2})')
_log.info(text_format.format('ø', 'å', 'Æ'))
# another format
new_text = ('Automatisering akselererer {0}yeblikket da '
            'roboter vil erobre planeten v{1}r. ({2})'.format('ø', 'å', 'Æ'))
_log.info(new_text)

"""f-string"""
text_f_string = (f"Automatisering akselererer {'ø'}yeblikket da "
                 f"roboter vil erobre planeten v{'å'}r. ({'Æ'})")
_log.info(text_f_string)

# another f-string
var1, var2, var3 = 'ø', 'å', 'Æ'
text_f_string = (f'Automatisering akselererer {var1}yeblikket da '
                 f'roboter vil erobre planeten v{var2}r. ({var3})')
_log.info(text_f_string)
# f-string with variables name
text_f_string = (f'Automatisering akselererer {var1=}yeblikket da '
                 f'roboter vil erobre planeten v{var2=}r. ({var3=})')
_log.info(text_f_string)

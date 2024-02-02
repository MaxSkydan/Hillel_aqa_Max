"""
Home task Regexp.

open input.txt file and find
all small english letters that match such conditions:

target small letter round exactly with three capital english letters
on the left and on the right
Match examples:
sdTRYaUVKn  -> matches "a" because 'TRY' on the left ( 3 capital letters )
and 'UVK' on the right ( 3 capital letters)
NTRSjARTb   -> no match ( not exactly 3 capital letters on the left
('NTRS' = 4 letters) )
zDFGbOPNq   -> matches "b"
Print Output as : "Result: "string of found letters">

Note:
- Result will be human read able string up to 10-15 characters
- Some usefully regexp constructions
[A-Z]  - match any capital letter
[^A-Z] - match any character except capital letter
[a-z]  - match small letter
do not forget about possible PRE- and POST- regexp searches
"""

import re

text = (r'C:\Users\Максим\PycharmProjects'
        r'\Hillel_aqa_Max\Hillel_aqa_Max\input.txt')
pattern = r'[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]'
# pattern = r'(?<![A-Z])[A-Z]{3}([a-z])[A-Z]{3}(?![A-Z])'  PRE- and POST-

with open(text, 'rt') as data_fh:
    data = data_fh.read()
    sentence = ' '.join(re.findall(pattern, data))
    print(f'"Result" : "{sentence}"')

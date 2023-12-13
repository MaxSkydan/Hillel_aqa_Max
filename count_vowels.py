"""
Hometask 4 - Count vowels.

# The English language has five vowels: A, E, I, O, and U
# Please count each vowel occurrence in text bellow
# (total sum of lower and capital cases)
# and write output as table something like this
#  -----------------
#  | vowel | count |
#  -----------------
#  |   a   |  11   |
#  |   e   |  23   |
#    ...
#  -----------------
# then modify text where each vowel replaced with
# A->À;  a->à ; E-> É ; e->é; I->Í , i->í ; O->Ó ; o->ó; U->Ú; u->ú
# ex. "Í wàndéréd lónély..." and print it.
"""

poem_text = """I wandered lonely as a cloud
That floats on high o'er vales and hills,
When all at once I saw a crowd,
A host, of golden daffodils;
Beside the lake, beneath the trees,
Fluttering and dancing in the breeze.
Continuous as the stars that shine
And twinkle on the Milky Way,
They stretched in never-ending line
Along the margin of a bay:
Ten thousand saw I at a glance,
Tossing their heads in sprightly dance.
"""

"""
We change all text to lowercase
and we count the vowels in the text and put them in the dictionary.
And after that we display a table with the counted vowels.
"""

vowels = {'A': poem_text.lower().count('a'), 'E': poem_text.lower().count('e'),
          'I': poem_text.lower().count('i'), 'O': poem_text.lower().count('o'),
          'U': poem_text.lower().count('u'),
          }

sep_num = 21
print('-' * sep_num)
print(f"| {'vowel':^6} | {'count':^8} |")
print('-' * sep_num)
for vowel, count in vowels.items():
    print(f'| {vowel:^6}|  {count:^8} |')
print('-' * sep_num)

"""
We modify the text in which each vowel is replaced.
And after that we display this changed text.
"""

modify = str.maketrans('AaEeIiOoUu', 'ÀàÉéÍíÓóÚú')
modified_text = poem_text.translate(modify)
print(modified_text)

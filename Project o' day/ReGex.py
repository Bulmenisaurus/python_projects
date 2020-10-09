import re

clr = input('What color would you like to input?\n')
hex_re = '#[\d, a-f, A-F]{3,6}'
re_sult = re.findall(hex_re, clr)
print('Hex results are:', re_sult)
rgb_re = '^rgb\s?\((\d{1,3}),\s?(\d{1,3}),\s?(\d{1,3})\)'
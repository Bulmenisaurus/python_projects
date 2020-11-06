"""
self_modifying_code

Description: Using a bit of trickery, self modifying code is on the menu!

Skillset: opening files with the "with" statement, negative indexes,
assigning indexes, .split() and ''.join() for lists, .write() and .read()
for files
"""

with open(__file__, "r") as self_modifying:  # __file__ is a str representation of a path to a file. Handy!
    to_write = self_modifying.read().split('\n')
    to_write[-4] += "+1"
try:
    1/0
    with open(__file__, "w") as self_modifying_write:  # Write and read arent allowed, so nested open()s are a thing :(
        self_modifying_write.write('\n'.join(to_write))  # the actual modifying bit
except:
    print("There is an error writing to the file. Here is what the source would've looked like:\n" + "-" * 20 + "\n")
    print('\n'.join(to_write))
    print("-" * 20)
    raise

print("You have run this file " +  # all these weird concats and multi-line parentheses are sooo useful in this case!
      str(
          0+1
      ) +
      " times!")

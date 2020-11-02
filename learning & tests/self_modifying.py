with open(__file__, "r") as self_modifying:  # __open__ is a str representation of a path to a file. Handy!
    to_write = self_modifying.read().split('\n')
    to_write[-4] += "+1"
    with open(__file__, "w") as self_modifying_write:  # Write and read arent allowed, so nested open()s are a thing :(
        self_modifying_write.write('\n'.join(to_write))  # the actual modifying bit

print("You have run this file " +  # all these weird concats and multi-line parentheses are sooo useful in this case!
      str(
          0+1+1+1+1
      ) +
      " times!") 

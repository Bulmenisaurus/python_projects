"""
The aim of this thing is to be able to remotely run python files, without interacting with
any project variables, and setting a hard limit. Hopefully I can add this into my discord bot,
when discord.py decides to work.
"""
import os


def better_input(prompt):
    print(prompt)
    finished_code = ['\n']
    while (line := input('')) != '' and finished_code[-1] != '':
        finished_code.append(line)
    return '\n'.join(finished_code)


code_data = better_input("Enter some code boiboi")

with open("remote_python_run_file.py", "w") as remote_code:
    remote_code.write(code_data)


print("Running file....")
a = os.popen('python remote_python_run_file.py').read()
print(a)

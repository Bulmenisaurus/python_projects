import subprocess as cmd
import sys


def terminal_run(commands: list):
    return cmd.run(commands, shell=True, check=True, stdout=sys.stdout, stderr=sys.stderr, cwd='/Users/meow'
                                                                                               '/programming'
                                                                                               '/PycharmProjects'
                                                                                               '/helloworld/')


terminal_run(['pwd'])
for x in range(2):
    terminal_run(["git commit --allow-empty -m \'\u200b\'"])
    terminal_run(['git push'])


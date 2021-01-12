"""
Secret Service Agent 00X got access to a top-secret safe protected by a digital lock. The agent
knows that the code for the lock has seven digits: some of these digits are 2s, others are 3s. He
also knows that there are more 2s than 3s, and that this code is divisible both by 3 and by 4.
Agent 00X has to open this lock on the first try; otherwise, the alarm will sound. What is the
code?
"""
import collections

START = int('2' * 7)
END = int('3' * 7)

for x in range(START, END):
    if set(str(x)) != {'3', '2'}:
        continue
    if collections.Counter(str(x)).most_common(1)[0][0] == '3':
        continue

    if not any((x % 3, x % 4)):
        print(x)
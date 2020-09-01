from random import randint

# hmm
PYTHONHASHSEED = 0  # same hash every damn time

blacklist_main = []
while True:
    command = input()
    if command[0:2].lower() == 'b/':  # if the input is a command
        command = list(command)
        del command[0:2]
        command = ''.join(command).strip()
        command_type = command[0:6].strip().lower()
        if command_type <= 'bl add':
            command_info = command.replace('bl add', '').strip()
            blacklist_main.append(hash(command_info))
            print(f"\'{command_info}\' has been added as {hash(command_info)}.")
    else:
        message = command.split()  # splits the message into words
        # this mean it techincally would be possible to seperate blacklisted word by a space
        for counter, word in enumerate(message):
            if hash(word) in blacklist_main:
                message[counter] = '#' * randint(3, 7)
        print(' '.join(message))

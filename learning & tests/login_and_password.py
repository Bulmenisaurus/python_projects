from time import sleep as chill
import pickle

class Colors:
    PURPL = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[32m'
    YELLO = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def create_new_user(name: str, email: str, password: str):
    with open("../python_data/user_data.topsecret", "rb") as user_data:
        users = pickle.load(user_data)
        if name not in users:
            users[name] = {"email": email, "password": password}
        else:
            print("User already exists.")
        pickle.dumps(user_data, users)

chill(.5)
print("||——————————————————<*********==========*********>——————————————————||")
print("Welcome to Bulmeni inc, and this is their official website!")
chill(0)
print(f"""\nWould you like to:
    {Colors.PURPL}[0]{Colors.ENDC} Login
    {Colors.BLUE}[1]{Colors.ENDC} Create account
    {Colors.GREEN}[2]{Colors.ENDC} Reset password
    {Colors.YELLO}[3]{Colors.ENDC} Delete account
""")
try:
    choice = int(input())
    if choice not in range(4):
        print("An error occurred with choices. Please try again!")
except ValueError:
    print("An error occurred with choices. Please try again!")
    choice = None
    quit()

if choice == 0:
    pass
elif choice == 1:
    user_name = input("Welcome, new user! What is your name?\n")
    user_email = input("And know, what is your e-mail? (we promise to keep it secret!)\n")
    user_password = input("And now, for the most important part. What is your password?\n")
    create_new_user(user_name, user_email, user_password)

elif choice == 2:
    pass
elif choice == 3:
    pass


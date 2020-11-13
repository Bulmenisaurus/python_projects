import requests
from bs4 import BeautifulSoup
import re
from time import sleep as chill
from random import random

from selenium import webdriver
import selenium

"""
Login info in /Users/meow/programming/ME-BOT login.txt
"""
class MeBot:
    def __init__(self, url="https://scratch.mit.edu/users/ME_BOT-py/",
                 username="ME_BOT-py",
                 password=None,
                 stats=None):
        if stats is None:
            stats = {'total_loves': 0, 'total_favorites': 0, 'total_follows:': 0}
        if password is None:
            with open("/Users/meow/programming/ME-BOT login.txt", "r") as fileinfo:
                self.password = eval(fileinfo.read())['password']

        self.url = url
        self.stats = stats
        self.username = username
        self.base = "https://scratch.mit.edu/"

    def login(self):
        driver = webdriver.Chrome(executable_path="/Users/meow/programming/PycharmProjects/!Python_on_github/major_projects/scratch_bot/chromedriver")
        driver.get(self.base+'/users/'+self.username)

        chill(3)
        login_button = driver.find_element_by_xpath("/html/body/div[1]/div[4]/div[7]/div[2]/div/div[1]/form/div[1]/textarea")
        login_button.click()

        username_input = driver.find_element_by_xpath(r'//*[@id="login-dialog"]/form/fieldset/div[2]/div[1]/div/input')

        password_input = driver.find_element_by_xpath("/html/body/div[3]/form/fieldset/div[2]/div[2]/div/input")
        for x in range(len(self.username)):
            username_input.send_keys(self.username[x])
            chill(random())
        for x in range(len(self.password)):
            password_input.send_keys(self.password[x])
            chill(random())

        chill(1)
        driver.find_element_by_xpath("/html/body/div[3]/form/fieldset/div[3]/div/button").click()

        self.client = driver

    def get_comments(self):
        api_url = "https://scratch.mit.edu/site-api/comments/user/" + self.username + "/"
        response = requests.get(api_url)
        soup = BeautifulSoup(response.text, 'html.parser')

        users_raw, comments_raw = soup.select("div.info div.name a"), soup.select("div.info div.content")

        users = [i.text for i in users_raw]
        comments_list = [i.text.strip() for i in comments_raw]
        assert len(users) == len(comments_list)

        return [(users[i], comments_list[i]) for i in range(len(users))]

    def filter_commands(self, comments_list: list):
        valid_commands = []
        for i in comments_list:
            if i[0] != self.username and re.match(r"\.\s?(follow|love|like)\s.*", i[1]):
                valid_commands.append(i)
        return valid_commands

    def like(self, command):
        project_url = command.split(' ')[-1]
        self.client.get(project_url)

    def stop(self):
        self.client.close()
        self.client.quit()




bot = MeBot()
bot.login()
bot.like('.like https://scratch.mit.edu/projects/445824887/')
chill(5)
bot.stop()

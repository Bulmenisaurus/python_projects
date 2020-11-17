import selenium
from selenium import webdriver

from time import sleep as chillax, time
from random import random

timer = time()


def rickroll_goog():
    g_path = "/Users/meow/programming/PycharmProjects/!Python_on_github/major_projects/scratch_bot/chromedriver"
    driver = webdriver.Chrome(executable_path=g_path)
    driver.get("https://www.google.com/")

    search = driver.find_element_by_xpath(r"/html/body/div[2]/div[3]/form/div[2]/div[1]/div[1]/div/div[2]/input")
    search.send_keys("https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstleyVEVO\n")

    driver.find_element_by_xpath("/html/body/div[8]/div[2]/div[10]/div[1]/div[2]/div/div[2]/div[2]/div/div/div[1]/div/div[1]/a/h3/span").click()

    print(f"Took {time() - timer} seconds to rickroll. :)")

    chillax(10)
    driver.close()
    driver.quit()


def rickroll_direct():
    g_path = "/Users/meow/programming/PycharmProjects/!Python_on_github/major_projects/scratch_bot/chromedriver"
    driver = webdriver.Chrome(executable_path=g_path)
    print(f"Driver establish {time() - timer}")
    driver.get("https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstleyVEVO")
    print(f"Driver link get {time() - timer}...")
    print(f"Took {time() - timer} seconds to rickroll. :)")

    chillax(10)

    driver.close()
    driver.quit()


def rickroll_goog_realistic():
    g_path = "/Users/meow/programming/PycharmProjects/!Python_on_github/major_projects/scratch_bot/chromedriver"
    driver = webdriver.Chrome(executable_path=g_path)
    driver.get("https://www.google.com/")

    search = driver.find_element_by_xpath(r"/html/body/div[2]/div[3]/form/div[2]/div[1]/div[1]/div/div[2]/input")
    for x in range(44):
        search.send_keys("https://www.youtube.com/watch?v=dQw4w9WgXcQ\n"[x])
        chillax(.001)

    driver.find_element_by_xpath("/html/body/div[8]/div[2]/div[10]/div[1]/div[2]/div/div[2]/div[2]/div/div/div[1]/div/div[1]/a/h3/span").click()

    print(f"Took {time() - timer} seconds to rickroll. :)")

    chillax(10)
    driver.close()
    driver.quit()

rickroll_goog_realistic()

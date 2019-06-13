from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys


def test_scores_service(get_url):
    try:
        driver = webdriver.Chrome(executable_path='C:\\Users\\arosenzweig\\PycharmProjects\\python\\WorldOfGames\\chromedriver.exe')

        driver.get(get_url)
        print("Driver got URL")
        get_score = driver.find_element_by_id("score").text
        print("Score is: {}".format(get_score))
        driver.close()
        if 0 < int(get_score) < 1000:
            return 0
        else:
            return 1

    except Exception as e:
        print("Exception details: {}".format(e))
        print("error in e2e-test_scores_service")


def main_function():
   try:
        score_status = test_scores_service("http://192.168.99.101:8777")
        if score_status == 0:
            sys.exit(0)  # test success
        else:
            sys.exit(1)

   except Exception as e:
       print("Exception details: {}".format(e))
       print("error in e2e-main_function")
       sys.exit(1)


main_function()

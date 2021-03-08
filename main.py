from selenium import webdriver

from process.process import *

if __name__ == "__main__":
    account = input("Input your pixiv account\n")
    pw = input("Input your password\n")
    browser = webdriver.Chrome(CHROME_DRIVER_ADDRESS)
    login_pixiv(browser, account, pw)
    get_pixiv_mark_image(browser, end_page=1)
    browser.quit()




import os
import math
import requests
import time

from util.constant import *
from util.tool import str_to_int, get_page_num


def link_convert(raw_link: str, image_num=1):
    link_arr = raw_link.split("/")
    year = link_arr[7]
    month = link_arr[8]
    day = link_arr[9]
    hour = link_arr[10]
    minute = link_arr[11]
    second = link_arr[12]
    pic_id = link_arr[13].split("_")[0]
    real_link_arr = []
    for i in range(image_num):
        real_link_arr.append(
            f"https://i.pximg.net/img-original/img/{year}/{month}/{day}/{hour}/{minute}/{second}/{pic_id}_p{i}.jpg")
    return {"pic_id": pic_id, "refer_link": f"https://www.pixiv.net/artworks/{pic_id}",
            "real_link": real_link_arr}


def get_img(res: dict):
    file_type = "jpg"

    img_num = len(res.get("real_link"))
    for i in range(img_num):
        if file_type == "jpg":
            resp = requests.get(res.get("real_link")[i], headers=HEADERS)
        if resp.status_code != 200 or file_type == "png":
            resp = requests.get(res.get("real_link")[i].replace("jpg", "png"), headers=HEADERS)
            file_type = "png"

        if resp.status_code == 200:
            pic_name = f"pixiv_img/{res.get('pic_id')}_p{i}.{file_type}"
            if not os.path.exists(pic_name):
                with open(pic_name, 'wb') as pic_file:
                    pic_file.write(resp.content)
                    pic_file.flush()


def load_page(driver):
    # Scroll the page to the bottom to let all images can show
    for i in range(1, 5 + 1):
        driver.execute_script(f'window.scrollTo(0, {i / 5}*document.body.scrollHeight)')
        time.sleep(0.5)


def login_pixiv(browser, account, pw):


    # browser = webdriver.Chrome("chromedriver.exe")
    browser.get("https://www.pixiv.net/")
    login_button = browser.find_element_by_css_selector('.signup-form__submit--login')
    login_button.click()

    time.sleep(1)

    acc_input = browser.find_element_by_xpath("//*[@id='LoginComponent']/form/div[1]/div[1]/input")
    pass_input = browser.find_element_by_xpath("//*[@id='LoginComponent']/form/div[1]/div[2]/input")
    acc_input.send_keys(account)
    pass_input.send_keys(pw)
    login_button = browser.find_element_by_xpath('//*[@id="LoginComponent"]/form/button')
    login_button.click()

    time.sleep(5)

    avatar_button = browser.find_element_by_xpath(
        '//*[@id="root"]/div[2]/div[1]/div[1]/div[1]/div/div[3]/div[1]/div[5]/div/button/div/div')
    avatar_button.click()
    mark_button = browser.find_element_by_xpath('/html/body/div[4]/div/div/div/ul/li[3]/a')
    mark_button.click()
    time.sleep(2)


def get_pixiv_mark_image(browser, start_page=1, end_page=1000000):
    mark_num = str_to_int(browser.find_element_by_xpath(
        '//*[@id="root"]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div/section/div[1]/div[1]/div/div/div/span').text)
    page_num = get_page_num(mark_num)
    base_page = browser.current_url
    cur_page = min(max(start_page, 1), page_num)
    page_num = max(min(page_num, end_page), cur_page)

    img_num_one_page = MAX_IMG_NUM_ONE_PAGE if mark_num >= MAX_IMG_NUM_ONE_PAGE else mark_num
    browser.get(f"{base_page}?p={cur_page}")
    while cur_page <= page_num:
        load_page(browser)
        for i in range(1, img_num_one_page + 1):
            print("cur_page", cur_page, "index_of_img", i + 1)
            try:
                img = browser.find_element_by_xpath(
                    f'//*[@id="root"]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div/section/div[3]/div/ul/li[{i}]'
                    f'/div/div[1]/label/div/div/a/div[2]/img')
                img_src = img.get_attribute('src')
            except:
                continue

            img_num = 1

            try:
                multiple_num = browser.find_element_by_xpath(
                    f'//*[@id="root"]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div/section/div[3]/div/ul/li[{i}]'
                    f'/div/div[1]/label/div/div/a/div[1]/div[2]/div/span[2]').text
                img_num = str_to_int(multiple_num)
            except:
                pass

            print(img_src, "img_num", img_num)
            get_img(link_convert(img_src, img_num))

        cur_page += 1
        if cur_page <= page_num:
            browser.get(f"{base_page}?p={cur_page}")
            time.sleep(1)

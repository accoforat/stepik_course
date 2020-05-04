from selenium import webdriver
import time
import os
from selenium.webdriver.support.ui import Select



try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    input_1 = browser.find_element_by_css_selector(".btn-primary")
    input_1.click()
    now_i_am_here = browser.current_window_handle
    print(now_i_am_here)
    new_hand = browser.window_handles[1]
    print(new_hand)
    browser.switch_to.window(new_hand)

    old_hand = browser.window_handles[0]
    print(old_hand)

    input_1 = browser.find_element_by_id("answer")
    input_1.send_keys('123')

    browser.switch_to.window(old_hand)
    input_1 = browser.find_element_by_css_selector(".btn-primary")
    input_1.click()




    time.sleep(10)



#    button = browser.find_element_by_css_selector("button.btn")
#    button.click()

finally:
    # закрываем браузер после всех манипуляций
    browser.quit()
#  webdriver.Chrome().get("http://suninjuly.github.io/simple_form_find_task.html")

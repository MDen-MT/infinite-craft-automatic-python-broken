import time
from selenium import webdriver
from selenium.webdriver.common.by import By
options = webdriver.ChromeOptions()
options.add_argument('--user-data-dir=C:/Users/YOUR_USER/AppData/Local/Google/Chrome/User Data')
# You need to change YOUR_USER to the user you are using.
driver = webdriver.Chrome(options=options)
driver.get('https://neal.fun/infinite-craft/')
driver.set_window_size(800, 1060)
time.sleep(2)
lst = []
sidebar = driver.find_element(By.CLASS_NAME, "mobile-items")
items = sidebar.find_elements(By.CLASS_NAME, "item")
while True:
    first_c = 0
    while first_c<len(items):
        i = items[first_c]
        second_c = 0
        while second_c<len(items):
            j = items[second_c]
            if f'{i.text}+{j.text}' not in lst and f'{j.text}+{i.text}' not in lst:
                i.click()
                j.click()
                lst.append(f'{i.text}+{j.text}')
                items = sidebar.find_elements(By.CLASS_NAME, "item")
                # here we wait until the “mobile-is-crafting” class on items disappears
                # which does not allow you to craft new items
                try:
                    while driver.find_element(By.CLASS_NAME, "mobile-is-crafting"):
                        'waiting...'
                except:
                    'continue'
            second_c+=1
        first_c+=1

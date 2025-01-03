from selenium import webdriver
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

options = webdriver.ChromeOptions()
options.add_experimental_option(name='detach', value=True)
driver = webdriver.Chrome(options=options)

driver.get('http://html5css.ru/howto/howto_js_rangeslider.php')
driver.maximize_window()

sleep(2)

slider = driver.find_element(By.XPATH, '//*[@id="id2"]')
action = ActionChains(driver)
action.click_and_hold(slider).move_by_offset(-50, 0).release().perform()

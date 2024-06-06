from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
import time

def smooth_scroll(driver, target, scroll_pause_time=0.1, step_size=100):
    current_position = driver.execute_script("return window.pageYOffset;")
    target_position = driver.execute_script("return arguments[0].getBoundingClientRect().top + window.pageYOffset - 100;", target)
    
    if current_position < target_position:
        for i in range(current_position, target_position, step_size):
            driver.execute_script(f"window.scrollTo(0, {i});")
            time.sleep(scroll_pause_time)
    else:
        for i in range(current_position, target_position, -step_size):
            driver.execute_script(f"window.scrollTo(0, {i});")
            time.sleep(scroll_pause_time)
    
    driver.execute_script(f"window.scrollTo(0, {target_position});")

driver = webdriver.Chrome()

try:
    driver.get('https://uomo.onrender.com/')
    time.sleep(2)
    
    total_height = driver.execute_script("return document.body.scrollHeight")
    for i in range(0, total_height, 100):
        driver.execute_script(f"window.scrollTo(0, {i});")
        time.sleep(0.1)
    time.sleep(2)
    
    target_element = driver.find_element(By.XPATH, '/html/body/main/section[3]')
    smooth_scroll(driver, target_element)
    time.sleep(2)
    
    tab_links = target_element.find_elements(By.TAG_NAME, 'a')
    first_tab = tab_links[0]
    for tab in tab_links:
        href = tab.get_attribute('href')
        if href.endswith('collections-tab-2') or href.endswith('collections-tab-3'):
            try:
                tab.click()
                time.sleep(1)
            except WebDriverException as e:
                print(f"No se pudo hacer clic en el elemento: {e}")

        if href.endswith('collections-tab-4'):
            tab.click()
            time.sleep(1)
            first_tab.click()
            time.sleep(1)

    home_product_link = driver.find_element(By.XPATH, '//*[@id="collections-tab-1"]/div[1]/div/div/div[1]')
    home_product_link.click()
    time.sleep(1)

    shop_product_add_button = driver.find_element(By.ID, 'add-cart')
    shop_product_add_button.click()

    time.sleep(5)

except WebDriverException as e:
    print(f"Se produjo un error al intentar cargar la página: {e}")

finally:
    driver.quit()

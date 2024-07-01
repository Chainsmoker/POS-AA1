from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import random
import time

email = f'correo{random.randint(1, 999999)}@prueba.com'

tested_card = {
    'number': '4242424242424242',
    'exp': '12/25',
    'cvc': '123'
}

user_data = {
    'name': 'Wilson Cueva',
    'email': email,
}

options = Options()
options.add_argument("--disable-popup-blocking")
options.add_argument("--disable-extensions")

def total_scroll():
    total_height = driver.execute_script("return document.body.scrollHeight")
    for i in range(0, total_height, 100):
        driver.execute_script(f"window.scrollTo(0, {i});")
        time.sleep(0.1)
    time.sleep(2)

def smooth_scroll_small(driver, target_position, scroll_pause_time=0.1, step_size=10):
    current_position = driver.execute_script("return window.pageYOffset;")
    
    if current_position < target_position:
        for i in range(current_position, target_position, step_size):
            driver.execute_script(f"window.scrollBy(0, {step_size});")
            time.sleep(scroll_pause_time)
    else:
        for i in range(current_position, target_position, -step_size):
            driver.execute_script(f"window.scrollBy(0, -{step_size});")
            time.sleep(scroll_pause_time)

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

driver = webdriver.Chrome(options=options)

try:
    driver.get('https://uomo.onrender.com/')
    time.sleep(2)
    
    total_scroll()
    
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

    smooth_scroll_small(driver, 200)
    time.sleep(1)

    changue_product_image = driver.find_element(By.XPATH, '/html/body/main/section[1]/div[1]/div[1]/div/div[1]/div/div[3]')
    changue_product_image.click()
    time.sleep(3)

    shop_product_wishlist_button = driver.find_element(By.XPATH, '/html/body/main/section[1]/div[1]/div[2]/div[4]/form/button')
    driver.execute_script("arguments[0].click();", shop_product_wishlist_button)
    time.sleep(1)

    register_button_tab = driver.find_element(By.ID, 'register-tab')
    register_button_tab.click()
    time.sleep(2)

    register_name_input = driver.find_element(By.NAME, 'register_name')
    register_name_input.send_keys('Alejandro')
    time.sleep(1)

    register_lastname_input = driver.find_element(By.NAME, 'register_lastname')
    register_lastname_input.send_keys('Plasencia')
    time.sleep(1)

    register_email_input = driver.find_element(By.NAME, 'register_email')
    register_email_input.send_keys(email)
    time.sleep(1)

    smooth_scroll_small(driver, 400)
    time.sleep(1)

    register_password_input = driver.find_element(By.NAME, 'register_password')
    register_password_input.send_keys('test123')

    register_button = driver.find_element(By.XPATH, '//*[@id="tab-item-register"]/div/form/button')
    driver.execute_script("arguments[0].click();", register_button)
    time.sleep(1)

    order_account_tab = driver.find_element(By.XPATH, '/html/body/main/section/div/div[1]/ul/li[2]/a')
    order_account_tab.click()
    time.sleep(1)

    wishlist_account_tab = driver.find_element(By.XPATH, '/html/body/main/section/div/div[1]/ul/li[4]/a')
    wishlist_account_tab.click()
    time.sleep(1)

    edit_account_tab = driver.find_element(By.XPATH, '/html/body/main/section/div/div[1]/ul/li[3]/a')
    edit_account_tab.click()
    time.sleep(2)

    edit_account_name_input = driver.find_element(By.NAME, 'edit_name')
    edit_account_name_input.clear()
    edit_account_name_input.send_keys('Wilson')
    time.sleep(1)

    edit_account_lastname_input = driver.find_element(By.NAME, 'edit_lastname')
    edit_account_lastname_input.clear()
    edit_account_lastname_input.send_keys('Cueva')
    time.sleep(1)

    edit_account_email_input = driver.find_element(By.NAME, 'edit_email')
    edit_account_email_input.clear()
    edit_account_email_input.send_keys(f'correo{random.randint(1, 999999)}@prueba.com')
    time.sleep(1)

    edit_account_button = driver.find_element(By.XPATH, '/html/body/main/section/div/div[2]/div/div/form[1]/div/div[4]/div/button')
    driver.execute_script("arguments[0].click();", edit_account_button)
    time.sleep(3)

    blog_link = driver.find_element(By.XPATH, '//*[@id="header"]/div/div/nav/ul/li[3]/a')
    blog_link.click()
    time.sleep(1.5)
    total_scroll()

    about_link = driver.find_element(By.XPATH, '/html/body/footer[1]/div/div/div[2]/ul/li[1]/a')
    about_link.click()
    time.sleep(1.5)
    total_scroll()

    contact_link = driver.find_element(By.XPATH, '/html/body/footer[1]/div/div/div[4]/ul/li[5]/a')
    contact_link.click()
    time.sleep(1.5)
    total_scroll()

    shop_link = driver.find_element(By.XPATH, '/html/body/footer[1]/div/div/div[3]/ul/li[1]/a')
    shop_link.click()
    time.sleep(2)

    shop_main_section = driver.find_element(By.CLASS_NAME, 'shop-main')
    smooth_scroll(driver, shop_main_section)
    time.sleep(2)

    driver.get('https://uomo.onrender.com/shop/cropped-faux-leather-jacket/')
    time.sleep(2)

    add_to_cart_button = driver.find_element(By.XPATH, '//*[@id="add-cart"]')
    driver.execute_script("arguments[0].click();", add_to_cart_button)
    time.sleep(2)

    driver.get('https://uomo.onrender.com/cart/')
    time.sleep(2)

    smooth_scroll_small(driver, 300)
    time.sleep(1)

    checkout_button = driver.find_element(By.ID, 'btn-checkout')
    driver.execute_script("arguments[0].click();", checkout_button)
    time.sleep(10)

    checkout_email_input = driver.find_element(By.XPATH, '//*[@id="email"]')
    checkout_email_input.send_keys(user_data['email'])
    time.sleep(1)

    checkout_card_number_input = driver.find_element(By.XPATH, '//*[@id="cardNumber"]')
    checkout_card_number_input.send_keys(tested_card['number'])
    time.sleep(1)

    checkout_card_exp_month_input = driver.find_element(By.XPATH, '//*[@id="cardExpiry"]')
    checkout_card_exp_month_input.send_keys(tested_card['exp'])
    time.sleep(1)

    checkout_card_exp_year_input = driver.find_element(By.XPATH, '//*[@id="cardCvc"]')
    checkout_card_exp_year_input.send_keys(tested_card['cvc'])
    time.sleep(1)
    
    checkout_name_input = driver.find_element(By.XPATH, '//*[@id="billingName"]')
    checkout_name_input.send_keys(user_data['name'])
    time.sleep(1)

    checkout_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div[2]/main/div/div[2]/form/div[1]/div/div/div[3]/div/div[2]/button')
    driver.execute_script("arguments[0].click();", checkout_button)

    smooth_scroll_small(driver, 1000)
    time.sleep(10)

    account_link_button = driver.find_element(By.XPATH, '//*[@id="header"]/div/div/div[2]/div[2]/a')
    driver.execute_script("arguments[0].click();", account_link_button)
    time.sleep(2)

    order_account_tab = driver.find_element(By.XPATH, '/html/body/main/section/div/div[1]/ul/li[2]/a')
    order_account_tab.click()
    time.sleep(30)

except WebDriverException as e:
    print(f"Se produjo un error al intentar cargar la página: {e}")

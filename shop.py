
# Shop: отображение страницы товара

# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.get('https://practice.automationtesting.in/')
# driver.maximize_window()
# driver.implicitly_wait(5)
# my_account = driver.find_element_by_id("menu-item-50")
# my_account.click()
# username= driver.find_element_by_id("username")
# username.send_keys("max@bk.ru")
# password = driver.find_element_by_id("password")
# password.send_keys("Maximus521!$")
# login_btn = driver.find_element_by_css_selector('[value="Login"]')
# login_btn.click()
# shop = driver.find_element_by_id("menu-item-40")
# shop.click()
# driver.execute_script("window.scrollBy(0, 500);")
# book = driver.find_element_by_css_selector(".post-181")
# book.click()
# element = driver.find_element_by_css_selector(".entry-title")
# element_get_text = element.text
# assert element_get_text == "HTML5 Forms"
# driver.quit()

# Shop: количество товаров в категории

# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.get('https://practice.automationtesting.in/')
# driver.maximize_window()
# driver.implicitly_wait(5)
# my_account = driver.find_element_by_id("menu-item-50")
# my_account.click()
# username= driver.find_element_by_id("username")
# username.send_keys("max@bk.ru")
# password = driver.find_element_by_id("password")
# password.send_keys("Maximus521!$")
# login_btn = driver.find_element_by_css_selector('[value="Login"]')
# login_btn.click()
# shop = driver.find_element_by_id("menu-item-40")
# shop.click()
# html_btn = driver.find_element_by_link_text("HTML")
# html_btn.click()
# books_count = driver.find_elements_by_css_selector(".wp-post-image")
# if len(books_count) == 3:
#     print("На странице 3 товара")
# else:
#     print("На странице: " + str(len(books_count)) + " товаров")
# driver.quit()


#Shop: сортировка товаров

# from selenium import webdriver
# from selenium.webdriver.support.select import Select
# driver = webdriver.Chrome()
# driver.get('https://practice.automationtesting.in/')
# driver.maximize_window()
# driver.implicitly_wait(5)
# driver.get('https://practice.automationtesting.in/')
# my_account = driver.find_element_by_id("menu-item-50")
# my_account.click()
# username= driver.find_element_by_id("username")
# username.send_keys("max@bk.ru")
# password = driver.find_element_by_id("password")
# password.send_keys("Maximus521!$")
# login_btn = driver.find_element_by_css_selector('[value="Login"]')
# login_btn.click()
# shop = driver.find_element_by_id("menu-item-40")
# shop.click()
# default = driver.find_element_by_css_selector(".orderby>option")
# element_checked = default.get_attribute("value")
# assert element_checked == "menu_order"
# high_to_low = driver.find_element_by_css_selector(".orderby")
# select = Select(high_to_low)
# select.select_by_value("price-desc")
# high_to_low1 = driver.find_element_by_css_selector(".orderby")
# element_checked = high_to_low1.get_attribute("value")
# assert element_checked == "price-desc"
# driver.quit()


# Shop: отображение, скидка товара

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# driver = webdriver.Chrome()
# driver.get('https://practice.automationtesting.in/')
# driver.maximize_window()
# driver.implicitly_wait(5)
# my_account = driver.find_element_by_id("menu-item-50")
# my_account.click()
# username= driver.find_element_by_id("username")
# username.send_keys("max@bk.ru")
# password = driver.find_element_by_id("password")
# password.send_keys("Maximus521!$")
# login_btn = driver.find_element_by_css_selector('[value="Login"]')
# login_btn.click()
# shop = driver.find_element_by_id("menu-item-40")
# shop.click()
# driver.execute_script("window.scrollBy(0, 600);")
# book = driver.find_element_by_css_selector(".post-169")
# book.click()
# old_price = driver.find_element_by_css_selector(".price>del>span")
# price_checked = old_price.text
# assert price_checked == "₹600.00"
# new_price = driver.find_element_by_css_selector(".price>ins>span")
# price_checked1 = new_price.text
# assert price_checked1 == "₹450.00"
# small_picture = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".images")))
# small_picture.click()
# close_picture = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".pp_close")))
# close_picture.click()
# driver.quit()

#Shop: проверка цены в корзине

# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# driver = webdriver.Chrome()
# driver.get('https://practice.automationtesting.in/')
# driver.maximize_window()
# driver.implicitly_wait(5)
# my_account = driver.find_element_by_id("menu-item-50")
# my_account.click()
# username= driver.find_element_by_id("username")
# username.send_keys("max@bk.ru")
# password = driver.find_element_by_id("password")
# password.send_keys("Maximus521!$")
# login_btn = driver.find_element_by_css_selector('[value="Login"]')
# login_btn.click()
# shop = driver.find_element_by_id("menu-item-40")
# shop.click()
# driver.execute_script("window.scrollBy(0, 600);")
# book = driver.find_element_by_css_selector('.post-182>:nth-child(2)')
# book.click()
# time.sleep(5)
# item = driver.find_element_by_css_selector(".cartcontents")
# item_checked = item.text
# assert item_checked == "1 Item"
# price = driver.find_element_by_css_selector(".wpmenucart-contents>.amount")
# price_checked = price.text
# assert price_checked == "₹180.00"
# basket = driver.find_element_by_css_selector(".wpmenucart-contents")
# basket.click()
# subtotal = WebDriverWait(driver, 5).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".cart-subtotal"), "180.00"))
# total = WebDriverWait(driver, 5).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".order-total"), "189.00"))
# driver.quit()

# Shop: работа в корзине

# import time
# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.get('https://practice.automationtesting.in/')
# driver.maximize_window()
# driver.implicitly_wait(5)
# shop = driver.find_element_by_id("menu-item-40")
# shop.click()
# time.sleep(3)
# driver.execute_script("window.scrollBy(0, 600);")
# book1 = driver.find_element_by_css_selector('.post-182>:nth-child(2)')
# book1.click()
# time.sleep(3)
# driver.execute_script("window.scrollBy(0, 500);")
# book2 = driver.find_element_by_css_selector('.post-165>:nth-child(2)')
# book2.click()
# basket = driver.find_element_by_css_selector(".wpmenucart-contents")
# basket.click()
# time.sleep(3)
# book1_remove = driver.find_element_by_css_selector('.post-182>:nth-child(2)')
# book1_remove.click()
# time.sleep(3)
# undo_btn = driver.find_element_by_link_text('Undo?')
# undo_btn.click()
# field = driver.find_element_by_name("cart[9766527f2b5d3e95d4a733fcfb77bd7e][qty]")
# field.clear()
# field.send_keys("3")
# update_basket = driver.find_element_by_name("update_cart")
# update_basket.click()
# book2_volume = driver.find_element_by_name("cart[9766527f2b5d3e95d4a733fcfb77bd7e][qty]")
# volume_check = book2_volume.get_attribute("value")
# if volume_check == "3":
#     print("True")
# else:
#     print("False")
# time.sleep(3)
# apply_btn = driver.find_element_by_name("apply_coupon")
# apply_btn.click()
# alert_script = driver.execute_script("alert('Please enter a coupon code.');")
# alert = driver.switch_to.alert
# alert_text = alert.text
# print(alert_text)
# driver.quit()


# Shop: покупка товара

# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# driver = webdriver.Chrome()
# driver.get('https://practice.automationtesting.in/')
# driver.maximize_window()
# driver.implicitly_wait(5)
# shop = driver.find_element_by_id("menu-item-40")
# shop.click()
# time.sleep(3)
# driver.execute_script("window.scrollBy(0, 600);")
# book1 = driver.find_element_by_css_selector("[data-product_id='182']")
# book1.click()
# time.sleep(3)
# basket = driver.find_element_by_css_selector(".wpmenucart-contents")
# basket.click()
# driver.execute_script("window.scrollBy(0, 300);")
# proceed_btn = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".checkout-button")))
# proceed_btn.click()
# first_name = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "billing_first_name")))
# first_name.send_keys("Max")
# last_name = driver.find_element_by_id("billing_last_name")
# last_name.send_keys("Maximus")
# email = driver.find_element_by_id("billing_email")
# email.send_keys("max@bk.ru")
# phone = driver.find_element_by_id("billing_phone")
# phone.send_keys("89119979997")
# driver.execute_script("window.scrollBy(0, 600);")
# country = driver.find_element_by_id("s2id_billing_country")
# country.click()
# field_country = driver.find_element_by_id("s2id_autogen1_search")
# field_country.send_keys("Russia")
# rus_country = driver.find_element_by_css_selector(".select2-match")
# rus_country.click()
# address = driver.find_element_by_id("billing_address_1")
# address.send_keys("Moscowskay street")
# address1 = driver.find_element_by_id("billing_address_2")
# address1.send_keys("apt. 56")
# city = driver.find_element_by_id("billing_city")
# city.send_keys("Saint-P")
# country1 = driver.find_element_by_id("billing_state")
# country1.send_keys("Russia")
# zip_code = driver.find_element_by_id("billing_postcode")
# zip_code.send_keys("198206")
# driver.execute_script("window.scrollBy(0, 800);")
# time.sleep(3)
# check_pay = driver.find_element_by_id("payment_method_cheque")
# check_pay.click()
# place_btn = driver.find_element_by_id("place_order")
# place_btn.click()
# text_thank_you = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".woocommerce-thankyou-order-received")))
# text_payment = WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "tfoot>:nth-child(3)>td"), "Check Payments"))
# driver.quit()

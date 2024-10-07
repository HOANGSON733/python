import os
import random
import time
import string
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

random_year = random.randint(1977, 2000)

list_first_name = [
    "Ánh", "Bích", "Châu", "Duyên", "Hà", "Hạnh", "Hoa", "Hương", "Linh",
    "Mai", "Ngọc", "Phương", "Quỳnh", "Trang", "Thu", "Thúy", "Tuyết", "Lan", "Vân"
]

list_last_name = [
    "Nguyễn", "Trần", "Lê", "Phạm", "Vũ", "Hoàng", "Đặng", "Bùi", "Ngô", "Dương"
]

list_email = [
    "nguykBJSBck",
    # "phuongnga9158",
]

# Path to your extension's .crx file or unpacked extension folder

def create_profile_chrome(email):
    chrome_options = Options()
    driver = webdriver.Chrome(options=chrome_options)
    driver.set_window_size(500, 800)  # width, height
    driver.get("https://signup.live.com/signup")

    time.sleep(5)
    
    # Continue with the rest of your steps as before
    print("#. Click tạo acc")
    driver.find_element(By.ID, "liveSwitch").click()
    time.sleep(random.randint(2, 3))
    
    print("#. Nhấn dropdown email")
    driver.find_element(By.CSS_SELECTOR, "option[value='hotmail.com']").click()
    time.sleep(random.randint(2, 3))

    print("#. Nhập email")
    driver.find_element(By.ID, "usernameInput").send_keys(email)
    time.sleep(random.randint(2, 3))

    print("#. Click next")
    driver.find_element(By.ID, 'nextButton').click()
    time.sleep(random.randint(2, 3))

    print("#. Enter password")
    driver.find_element(By.ID, 'Password').send_keys("Autotest@123")
    time.sleep(random.randint(2, 3))
    
    print("#. Click Next.")
    driver.find_element(By.ID, 'nextButton').click()
    time.sleep(random.randint(2, 3))
    
    print("#. Enter Last name")
    driver.find_element(By.NAME, 'lastNameInput').send_keys(list_last_name[random.randint(0, len(list_last_name) - 1)])
    time.sleep(random.uniform(1, 2))
    
    print("#. Enter First name")
    driver.find_element(By.NAME, 'firstNameInput').send_keys(list_first_name[random.randint(0, len(list_first_name) - 1)])
    time.sleep(random.uniform(1, 2))
   
    print("#. Click Tiếp theo")
    driver.find_element(By.ID, 'nextButton').click()
    time.sleep(random.randint(2, 3))
    
    print('#. Click day')
    dropdown = Select(driver.find_element(By.ID, "BirthDay"))
    options = dropdown.options[1:]
    random_option = random.choice(options)
    print(f"Randomly selected day: {random_option.text}")
    dropdown.select_by_visible_text(random_option.text)
    time.sleep(random.randint(2, 3))
    
    print("#. Click month")
    dropdown = Select(driver.find_element(By.ID, "BirthMonth"))
    options = dropdown.options[1:]
    random_option = random.choice(options)
    print(f"Randomly selected month: {random_option.text}")
    dropdown.select_by_visible_text(random_option.text)
    time.sleep(random.randint(2, 3))
    
    print("#. Click year")
    birth_year_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "BirthYear")))
    birth_year_input.send_keys(str(random_year))
    time.sleep(random.randint(2, 3))
    
    print("#. Click Tiếp theo")
    driver.find_element(By.ID, 'nextButton').click()

    time.sleep(30)  # Điều chỉnh theo thời gian CAPTCHA Arkose cần
    driver.quit()

if __name__ == '__main__':
    for email in list_email:
        print(f"Creating profile for email: {email}")
        create_profile_chrome(email)
        print(f"Profile creation completed for: {email}\n")

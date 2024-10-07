import os
import csv
import requests
import random
import time
import string
import threading
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from nextcaptcha import NextCaptchaAPI
list_email = [
    "ufombayoosafd@hotmail.com"
  
]
list_pass = [
    "IN2mEL696"
    
]

list_phone = [
    "522660941"
]


def generate_random_string(length=8):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

def create_profile_firefox(email):
    name_profile = generate_random_string()
    print(f"Random Name Profile: {name_profile}")



    firefox_path = r"C:\Program Files\Mozilla Firefox\firefox.exe"
    os.system(f'"{firefox_path}" -CreateProfile {name_profile}')    

    try:
        firefox_profiles_path = os.path.join(os.getenv('APPDATA'), 'Mozilla', 'Firefox', 'Profiles')
        os.chdir(firefox_profiles_path)

        profile_dir = next(filter(lambda d: name_profile in d, os.listdir('.')), None)

        if profile_dir is None:
            raise FileNotFoundError("Profile directory not found")

        os.chdir(profile_dir)
        profile_path = os.getcwd()

        print(f"Profile {name_profile} created successfully at {profile_path}.")

        open_browser(profile_path, email)

        os.chdir(os.getenv('windir'))

    except Exception as e:
        print(f"An error occurred: {e}")

def open_browser(profile_path, email):
    options = Options()
    options.profile = profile_path
    driver = webdriver.Firefox(options=options)
    driver.set_window_size(500, 800)  # width, height
    driver.get("https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=160&ct=1726717226&rver=7.5.2211.0&wp=MBI_SSL&wreply=https%3a%2f%2foutlook.live.com%2fowa%2f%3fnlp%3d1%26cobrandid%3dab0455a0-8d03-46b9-b18b-df2f57b9e44c%26RpsCsrfState%3d1c4dee99-6e96-6af5-9285-aa2d39ba4058&id=292841&aadredir=1&CBCXT=out&lw=1&fl=dob%2cflname%2cwld&cobrandid=ab0455a0-8d03-46b9-b18b-df2f57b9e44c")
    time.sleep(5)

    print("#. Enter email to login Hotmai")
    driver.find_element(By.NAME, "loginfmt").send_keys(email)
    time.sleep(random.randint(2, 3))

    print("#. Click login button")
    driver.find_element(By.ID, 'idSIButton9').click()
    time.sleep(random.randint(1,2))

    print("#. Enter password")
    driver.find_element(By.ID, 'i0118').send_keys(list_pass[0])
    time.sleep(random.randint(2, 3))
    
    print("#. Click Next.")
    driver.find_element(By.CLASS_NAME, 'ext-primary').click()
    time.sleep(random.randint(3,4))
   
    print("#. Click Tiếp theo")
    driver.find_element(By.ID, 'iLandingViewAction').click()
    time.sleep(random.randint(3,4))
    
    driver.find_element(By.ID, 'DisplayPhoneCountryISO').send_keys("Việt Nam (+84)")
    time.sleep(2)
    
    print("#. Click Next.")
    driver.find_element(By.ID, 'DisplayPhoneNumber').send_keys(list_phone[0])
    time.sleep(random.randint(3,4)) 
    
    print("#. Click Tiếp theo")
    driver.find_element(By.ID, 'iCollectPhoneViewAction').click()
    time.sleep(random.randint(4,5))
    
    print("#. Click Tiếp theo")
    driver.find_element(By.ID, 'nextButto').click()
    time.sleep(random.randint(4,5))
    
    # print("#. Open the email in the new tab and get the code")
    # driver.execute_script("window.open('https://viotp.com/Account/Login')")
    # time.sleep(4)
    # # driver.switch_to.window(driver.window_handles[1])#sử dụng để chuyển sang tab mới 
    # time.sleep(5)
    
    # print("#. Nhập UserName")
    # WebDriverWait(driver, 10).until(
    #     EC.presence_of_element_located((By.ID, 'UserName'))
    # ).send_keys('nghiathammy')
    
    # print("#. Nhập Passwword")
    # driver.find_element(By.ID, 'Password').send_keys('Hachitech611@')
    # time.sleep(3)
    
    # print("#. Click Check Captcha")
    # driver.find_element(By.ID, 'recaptcha-anchor').click()
    # time.sleep(random.randint(30))
    
    # print("#. Click đăng nhập")
    # driver.find_element(By.ID, 'iProof0').click()
    # time.sleep(random.randint(5,6))
    
    # print("#. Enter Age")
    # age_input = driver.find_element(By.XPATH, '//*[@data-testid="age-input-label"]/following::input[1]')
    # age_input.send_keys(str(random.randint(18, 35)))
    # time.sleep(random.randint(2, 3))

    # print("#. Click Create account")
    # driver.find_element(By.XPATH, "//button[@type='submit' and contains(text(),'Tạo tài khoản')]").click()
    # time.sleep(random.randint(3, 5))

    # print("#. Open the email in the new tab and get the code")
    # driver.execute_script("window.open('https://mail.nikolaxflem.com/')")
    # time.sleep(5)

    # driver.switch_to.window(driver.window_handles[1])
    # time.sleep(5)

    # print("#. Enter the email address")
    # driver.find_element(By.ID, 'username').send_keys(email)
    # time.sleep(2)

    # print("#. Enter the password")
    # driver.find_element(By.ID, 'password').send_keys('123456')
    # time.sleep(2)

    # print("#. Click the Sign In button")
    # driver.find_element(By.CSS_SELECTOR, '.ZLoginButton.DwtButton').click()
    # time.sleep(60)

    # print("#9. Get the code from the email")
    # driver.find_element(By.ID, 'zlif__CLV-main__-257__rw').click()  
    # time.sleep(5)

    # iframe = driver.find_element(By.TAG_NAME, "iframe")
    # driver.switch_to.frame(iframe)

    # element = driver.find_element(By.CSS_SELECTOR, "div[style*='font-size: 32px']")
    # code = element.text
    # print(f'++++++ code is {code}')

    # driver.switch_to.default_content()  

    # driver.switch_to.window(driver.window_handles[0])
    # time.sleep(5)

    # print("#. Enter code to login profile firefox")
    # input_field = driver.find_element(By.XPATH, '//*[@data-testid="confirm-signup-code-input-field"]')
    # input_field.send_keys(code)
    # time.sleep(random.randint(2, 3))

    # print("#. Click Submit btn")
    # submit_btn = driver.find_element(By.CLASS_NAME, "cta-primary")
    # submit_btn.click()
    # time.sleep(random.randint(4, 5))

    # print("#. Click Start Browser")
    # start_browser_btn = WebDriverWait(driver, 10).until(
    #     EC.element_to_be_clickable((By.ID, 'cad-not-now'))
    # )
    # start_browser_btn.click()
    # time.sleep(random.randint(4, 5))

    # print("#. Open facebook Browser")
    # driver.get("https://www.facebook.com/r.php")
    # time.sleep(random.randint(3,5))

    # print("#. Create account facebook")

    # print("#. Enter Last name")
    # driver.find_element(By.NAME, 'lastname').send_keys(list_last_name[random.randint(0,len(list_last_name) - 1)])
    # time.sleep(random.uniform(1,2))

    # print("#. Enter Firsrt name")
    # driver.find_element(By.NAME,'firstname').send_keys(list_first_name[random.randint(0,len(list_first_name) - 1)])
    # time.sleep(random.uniform(1,2))

    # print("#. Enter email")
    # driver.find_element(By.NAME, 'reg_email__').send_keys(email) 
    # time.sleep(random.uniform(1,2))

    # print("#. Enter password")
    # driver.find_element(By.ID, 'password_step_input').send_keys('123456A#')
    # time.sleep(random.uniform(1,2))

    # print("#. Select Birthday")
    # driver.find_element(By.NAME, 'birthday_day').send_keys(random.randint(1,29))
    # time.sleep(2)

    # driver.find_element(By.NAME, 'birthday_month').send_keys(f'Tháng {random.randint(1,13)}')
    # time.sleep(2)

    # driver.find_element(By.NAME, 'birthday_year').send_keys(random.randint(1997,2006))
    # time.sleep(2)

    # print("#. Select gender")
    # driver.find_element(By.XPATH, "//input[@name='sex' and @value='1']").click()
    # time.sleep(random.uniform(1,2))

    # print("#. Click register btn")
    # driver.find_element(By.NAME,'websubmit').click()
    # time.sleep(random.uniform(20,25))

    # print("#. Open the email in the new tab and get the code")
    # driver.execute_script("window.open('https://mail.nikolaxflem.com/')")
    # time.sleep(5)

    # driver.switch_to.window(driver.window_handles[1])
    # time.sleep(5)

    # print("#9. Get the code from the email")
    # code_element = WebDriverWait(driver, 10).until(
    #     EC.presence_of_element_located((By.ID, 'zlif__CLV-main__-259__su'))
    # )
    # code = code_element.text.split("FB-")[1].split(" ")[0]
    # print(f"code: {code}")

    # driver.switch_to.window(driver.window_handles[0])
    # time.sleep(5)

    # print("#. Enter code")
    # driver.find_element(By.ID, 'code_in_cliff').send_keys(code)
    # time.sleep(random.uniform(1,2))

    # print("#. Click continue btn")
    # driver.find_element(By.NAME, 'confirm').click()
    # time.sleep(random.uniform(4,5))

    # print("#. Click Ok btn")
    # driver.find_element(By.CLASS_NAME, '_42ft').click()
    # time.sleep(random.uniform(8,10))

    driver.quit()

if __name__ == '__main__':
    threads = []

    for email in list_email:
        thread = threading.Thread(target=create_profile_firefox, args=(email,))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

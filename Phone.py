import unittest
from appium import webdriver
from appium.options.android import UiAutomator2Options
import utils
from selenium.webdriver.common.keys import Keys
import time
import random
from appium.webdriver.common.appiumby import AppiumBy
import datetime
# import webbrowser
import pyperclip
import re   
import subprocess



list_first_name = [
    "Ánh", "Bích", "Châu", "Duyên", "Hà", "Hạnh", "Hoa", "Hương", "Linh",
    "Mai", "Ngọc", "Phương", "Quỳnh", "Trang", "Thu", "Thúy", "Tuyết", "Lan", "Vân",
    "Ngân", "Nhung", "Yến", "Hồng", "Sương", "Lệ", "Như", "Kim", "Đào", "Phượng",
    "Tâm", "Hiền", "Mỹ", "Bảo", "Linh", "Cẩm", "Hạnh", "Duyên", "Hòa", "Thủy",
    "Hòa", "Khanh", "Diễm", "Tuyết", "Quý", "Vân", "Thảo", "Linh", "Tuyết", "Khánh",
    "Hạ", "Nhã", "Như", "Dung", "An", "Bích", "Liên", "Mai", "Diệp", "Tâm"
]

list_last_name = [
    "Nguyễn", "Trần", "Lê", "Phạm", "Vũ", "Hoàng", "Đặng", "Bùi", "Ngô", "Dương",
    "Đỗ", "Hồ", "Lý", "Trương", "Tô", "Lưu", "Mai", "Tống", "Lâm", "Trịnh", "Đoàn", "Hà", "Lưu", "Nguyễn", "Phan", "Thái", "Trí", "Nhật", "Hưng",
    "Vương", "Hồng", "Hà", "Hải", "Phan", "Trịnh", "Mạnh", "Khưu", "Đoàn", "Lê",
    "Đinh", "Hoàng", "Nhâm", "Lâm", "Quách", "Trí", "Hồng", "Lại", "Bạch", "Bùi"
]

# # List of months
# list_month = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

# # List of days
# list_day = [f"{day:02}" for day in range(1, 32)]

# # List of years
# list_year = [year for year in range(2000, 2004)]

#List email
list_email = [
  'minhnhat1477@nikolaxflem.com'
]


# Capabilities configuration
capabilities = {
  "platformName": "Android",
  "appium:deviceName": "Samsung Galaxy S22 Ultra",
  "appium:automationName": "UiAutomator2",
  "appium:udid": "635e40ef",
  "appium:noReset": True,
  "appium:skipDeviceInitialization": True,
  "appium:skipServerInstallation": True,
  "appium:ignoreHiddenApiPolicyError": True
}

appium_server_url = "http://127.0.0.1:4723"

class TestAppium(unittest.TestCase):
    def setUp(self) -> None:
        options = UiAutomator2Options().load_capabilities(capabilities)
        self.driver = webdriver.Remote(appium_server_url, options=options)

    def tearDown(self) -> None:
        if self.driver:
            self.driver.quit()

    def test_basic(self) -> None:
         for i in range(0, len(list_email)):
            # Nếu i khác 0 và i chia hết cho 5 thì nghỉ 300 giây
            if i != 0 and i % 5 == 0:
                print(f"Pausing for 300 seconds at iteration {i}")
                time.sleep(300)
            else:
                #Open facebook
                print("Open facebook")
                # self.driver.find_element(by=AppiumBy.XPATH,value='//android.widget.TextView[@content-desc="Facebook clone"]').click()
                # time.sleep(random.uniform(2,3))
                
                # # CLick Create new account
                # print("Click Create new account")
                # self.driver.find_element(by=AppiumBy.XPATH,value='//android.view.View[@content-desc="Create new account"]').click()
                # time.sleep(random.uniform(3,4))
                
                # # Click get started
                # print("Click get started")
                # self.driver.find_element(by=AppiumBy.XPATH,value='//android.widget.Button[@content-desc="Get started"]/android.view.ViewGroup/android.view.ViewGroup').click()
                # time.sleep(random.uniform(6,7))
                
                # try:
                #     # Click deny
                #     print("Click Dont Alow")
                #     self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.Button[@resource-id="com.android.permissioncontroller:id/permission_deny_and_dont_ask_again_button"]').click()
                #     time.sleep(random.uniform(2,3))
                # except:
                #     pass
                
                # try:
                #     # Click Not now
                #     print("Click Not now")
                #     self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.Button[@resource-id="com.facebook.katana:id/(name removed)" and @text="NOT NOW"]').click()
                # except:
                #     pass
                
                # # Enter first name and last name
                # print("Enter first name and last name")
                
                # try:
                #     # Click Not now
                #     print("Click Not now")
                #     self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.Button[@resource-id="com.facebook.katana:id/(name removed)" and @text="NOT NOW"]').click()
                # except:
                #     pass
                
                # self.driver.find_element(by=AppiumBy.XPATH, value='//androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.widget.EditText').send_keys(list_first_name[random.randint(0,len(list_first_name)-1)])
                # time.sleep(random.uniform(2,3))
                
                
                
                # self.driver.find_element(by=AppiumBy.XPATH, value='//androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.widget.EditText'
                # ).send_keys(list_last_name[random.randint(0,len(list_last_name)-1)])
                # time.sleep(random.uniform(2,3))
                
                # #Click btn next
                # print("Click btn next")
                
                # self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.Button[@content-desc="Next"]/android.view.ViewGroup'
                # ).click()
                # time.sleep(random.uniform(1,2))
                
                # # Select birthday
                # print("Select birthday")
                # random_month = random.randint(1, 3)

                # for _ in range(random_month):
                #     self.driver.swipe(
                #         start_x=290,  # Start x coordinate
                #         start_y=1380, # Start y coordinate
                #         end_x=290,    # End x coordinate (same as start to keep it vertical)
                #         end_y=1025,   # End y coordinate
                #         duration=800  # Duration of the swipe
                #     )
                
                # random_day = random.randint(1,5)
                # for _ in range(0, random_day):
                #     self.driver.swipe(
                #         start_x=528,  # Start x coordinate
                #         start_y=1380, # Start y coordinate
                #         end_x=528,    # End x coordinate (same as start to keep it vertical)
                #         end_y=1025,   # End y coordinate
                #         duration=800  # Duration of the swipe
                #     )
                    
                    
                # random_year = random.randint(15,16)
                # for _ in range(0, random_year):
                #     self.driver.swipe(
                #         start_x=770,  # Start x coordinate
                #         start_y=1025, # Start y coordinate1025
                #         end_x=770,    # End x coordinate (same as start to keep it vertical)
                #         end_y=1380,   # End y coordinate
                #         duration=800  # Duration of the swipe
                #     )
                   
                # #Click btn set
                # print("# Click btn set")
                # self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.Button[@resource-id="android:id/button1"]'
                # ).click()
                # time.sleep(random.uniform(1,2))
                
                # # Click btn next
                # print("# Click btn next")
                # self.driver.find_element(by=AppiumBy.XPATH, value='//android.view.View[@content-desc="Next"]'
                # ).click()
                # time.sleep(random.uniform(1,2))
                
                # # CLick option Female
                # print("# Click option Female")
                # self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.Button[@content-desc="Female"]/android.view.ViewGroup/android.view.ViewGroup/android.widget.ImageView'
                # ).click()
                # time.sleep(random.uniform(1,2))
                
                # # Click btn next
                # print("# Click btn next")
                # self.driver.find_element(by=AppiumBy.XPATH, value='//android.view.View[@content-desc="Next"]'
                # ).click()
                # time.sleep(random.uniform(1,2))
                
                # try:
                #     # Click deny
                #     print("Click Deny")
                #     self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.Button[@resource-id="com.android.permissioncontroller:id/permission_deny_button"]').click()
                #     time.sleep(random.uniform(1,2))
                # except:
                #     pass
                
                # # CLick sign in width email
                # print("# Click sign in width email")
                # self.driver.find_element(by=AppiumBy.XPATH, value='//android.view.View[@content-desc="Sign up with email"]'
                # ).click()
                # time.sleep(random.uniform(1,2))
                
                # # Enter email
                # print("# Enter email")
                # self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText'
                # ).send_keys(list_email[i])
                # time.sleep(random.uniform(1,2))
                
                # # Click btn next
                # print("# Click btn next")
                # self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.Button[@content-desc="Next"]/android.view.ViewGroup'
                # ).click()
                # time.sleep(random.uniform(1,2))
                
                # # Enter password
                # password = '123456A@'
                # print("# Enter password")
                # self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText'
                # ).send_keys(password)
                # time.sleep(random.uniform(1,2))
                
                # # Click btn next
                # print("# Click btn next")
                # self.driver.find_element(by=AppiumBy.XPATH, value= '//android.widget.Button[@content-desc="Next"]/android.view.ViewGroup'
                # ).click()
                # time.sleep(random.uniform(1,2))
                
                # try:
                #     # Click Not now
                #     print("# Click Not now")    
                #     self.driver.find_element(by=AppiumBy.XPATH, value='//android.view.View[@content-desc="Not now"]'
                #     ).click()
                #     time.sleep(random.uniform(1,2))
                # except:
                #     pass
                
                # # Click btn I Agree
                # print("# Click btn I Agree")
                # self.driver.find_element(by=AppiumBy.XPATH, value='//android.view.View[@content-desc="I agree"]'
                # ).click()
                # time.sleep(random.uniform(12,15))
                
                # try:
                #     self.driver.find_element(
                #         by=AppiumBy.XPATH,
                #         value='//android.widget.Button[@resource-id="com.facebook.katana:id/(name removed)"]'
                #     ).click()
                # except:
                #     pass
                # time.sleep(random.uniform(22,25))
                # # Back to home phone
                # print("# Back to home phone")
                # self.driver.press_keycode(3)
                # time.sleep(random.uniform(2,3))
                
                # # Click browser
                # print("# Click browser")
                # self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@content-desc="Chrome"]'
                # ).click()
                # time.sleep(random.uniform(1,2))
                
                # print("# Click 3 chấm")
                # self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@resource-id="com.android.chrome:id/search_box_text"]'
                # ).click()
                # time.sleep(random.uniform(2, 3))
                
                # print("# Click new tab")
                # self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@resource-id="com.android.chrome:id/url_bar"]'
                # ).send_keys('https://mail.nikolaxflem.com/')
                # time.sleep(random.uniform(3, 4))
                
                # # Enter link mail server
                # print("# Enter link mail server")   
                # self.driver.press_keycode(66)              
                # time.sleep(random.uniform(1,2))
                
                
                
                # Login mail server
                # print("# Login mail server")
                
                # #Enter Username
                # print("## Enter username")
                # self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@resource-id="username"]'
                # ).send_keys(list_email[i])
                # time.sleep(random.uniform(2,3))
                
                # ##Enter Password
                # print("## Enter Password")
                # self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@resource-id="password"]'
                # ).send_keys("123456")
                # time.sleep(random.uniform(2,3))
                
                # # Click Sign in
                # print("# Click Sign in")
                # self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.Button[@text="Sign In"]'
                # ).click()
                # time.sleep(random.uniform(6,8))
                
                # # Click hold with loc to copy otp
                # print("# Click hold with loc to copy otp")
                # self.driver.tap(
                #     [(244, 781)],
                #     duration=2000
                # )
                # time.sleep(random.uniform(1,2))
                
                # # Click with loc
                # print("# Click with")
                # self.driver.tap(
                #     [(400, 628)],
                #     duration=300
                # )
                # time.sleep(random.uniform(1,2))
                
                # Click logout mail server
                print("# Click logout mail server") 
                self.driver.find_element(
                AppiumBy.XPATH,value= '//android.widget.TextView[@text="Log Out"]'
                ).click()
                time.sleep(random.uniform(1,2))
                
                print("# Back to home phone")
                self.driver.press_keycode(3)
                time.sleep(random.uniform(3, 4))
                # Open facebook
                print("Open facebook")
                self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@content-desc="Facebook clone"]'
                ).click()
                time.sleep(random.uniform(3,5))
                
                # Enter OTP
                print("# Enter OTP")
                self.driver.tap(
                    [(168, 699)],
                    duration=3000
                )
                time.sleep(random.uniform(2,3))

                # Click paste otp
                print("# Click paste otp")
                self.driver.tap(
                    [(163, 544)],
                    duration=300
                )
                time.sleep(random.uniform(2,3))
                
                # Click Next btn
                print("# Click Next btn")
                self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.Button[@content-desc="Next"]/android.view.ViewGroup'
                ).click()
                time.sleep(random.uniform(2,3))
                
                # # Click skip add picture
                # print("# Click skip add picture")
                # utils.get_element_wait_by_xpath(
                #     driver=self.driver,
                #     xpath='//android.view.View[@content-desc="Skip"]'
                # ).click()
                # time.sleep(random.uniform(10,12))
                
                # # Click Not now
                # print("# Click Not now")
                # utils.get_element_wait_by_xpath(
                #     driver=self.driver,
                #     xpath='//android.view.View[@content-desc="Not now"]'
                # ).click()
                # time.sleep(random.uniform(2,3))
                
                # # Click Skip
                # print("# Click Skip")
                # utils.get_element_wait_by_xpath(
                #     driver=self.driver,
                #     xpath='//android.widget.Button[@resource-id="com.facebook.katana:id/(name removed)" and @text="SKIP"]'
                # ).click()
                # time.sleep(random.uniform(1,2))
                
                # try:
                #     #Click next btn
                #     print("# Click next btn")   
                #     utils.get_element_wait_by_xpath(
                #         driver=self.driver,
                #         xpath='//android.widget.Button[@content-desc="Next"]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup'
                #     ).click()
                #     time.sleep(random.uniform(1,2))
                # except: 
                #     pass
                
                # # Click Skip
                # try:
                #     print("# Click Skip")
                #     self.driver.find_element(
                #         by=AppiumBy.XPATH,
                #         value='//android.widget.Button[@content-desc="Skip"]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup'
                #     ).click()
                # except:
                #     pass
                # time.sleep(random.uniform(7,8))
                
                # print("# Open multitasking")
                # self.driver.press_keycode(187)
                # time.sleep(random.uniform(3,4)) 
                
                
                # # Scroll to close tab facebook
                # print("# Scroll to close tab facebook")
                # utils.scroll_by_vertical(
                #     driver=self.driver,
                #     x_loc=536,
                #     y_start=1289,
                #     y_end=128
                # )
                # time.sleep(random.uniform(2,3)) 
                    

                # print("# Back to home phone")
                # self.driver.press_keycode(3)
                # time.sleep(random.uniform(2,3)) 
                
                # #Open facebook
                # print("Open facebook")
                # utils.get_element_wait_by_xpath(
                #     driver=self.driver,
                #     xpath='//android.widget.TextView[@content-desc="Facebook"]'
                # ).click()
                # time.sleep(random.uniform(3,5))
                
                # # Click Menu tab
                # print("# Click Menu tab")
                # # menu_element = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value='new UiSelector().descriptionContains("Menu")')
                # # menu_element.click()
                # utils.get_element_wait_by_xpath(
                #     driver=self.driver,
                #     xpath='//android.view.View[contains(@content-desc, "Menu, tab 5 of") or contains(@content-desc, "Menu, tab 6 of")]'
                # ).click()
                # time.sleep(random.uniform(2,3))
                
                # try:
                #     # Click Skip    
                #     print("# Click Skip")
                #     self.driver.find_element(
                #         by=AppiumBy.XPATH,
                #         value='//android.view.View[@text="Skip"]'
                #     ).click()
                #     time.sleep(2)
                # except:
                #     pass
                
                # # CLick see your profile
                # print("# CLick see your profile")
                # utils.get_element_wait_by_xpath(
                #     driver=self.driver,
                #     xpath='//androidx.recyclerview.widget.RecyclerView[@resource-id="com.facebook.katana:id/(name removed)"]/android.view.ViewGroup[1]/android.view.ViewGroup'
                # ).click()
                # time.sleep(random.uniform(2,3))
                
                # try:
                #     # Click Skip    
                #     print("# Click Skip")
                #     self.driver.find_element(
                #         by=AppiumBy.XPATH,
                #         value='//android.view.View[@text="Skip"]'
                #     ).click()
                #     time.sleep(2)
                # except:
                #     pass
                
                # try:
                #     # Click Cancel
                #     print("# Click Cancel") 
                #     self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.Button[@content-desc="Cancel"]/android.widget.ImageView').click()
                #     time.sleep(random.uniform(2,3))
                    
                #     # Click Stop
                #     print("# Click Stop")
                #     self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.Button[@resource-id="android:id/button1"]').click()
                #     time.sleep(random.uniform(2,3))
                    
                # except:
                #     pass 
                
                # # Click see more profile
                # print("# Click see more profile")
                # utils.get_element_wait_by_xpath(
                #     driver=self.driver,
                #     xpath='//android.widget.Button[@content-desc="See more"]'
                # ).click()
                # time.sleep(random.uniform(2,3))
                
                # # Scroll until the "Copy link" profile button is found
                # print("# Scroll until to find copy link profile button")
                # for _ in range(0, 3):
                #     utils.scroll_by_vertical(
                #         driver=self.driver,
                #         x_loc=500,
                #         y_start=1530,
                #         y_end=500
                #     )
                # time.sleep(random.uniform(2, 3))

                # # Click the "Copy profile link" button
                # print("# Click copy profile link")
                # try:
                #     utils.click_with_loc(
                #         driver=self.driver,
                #         x_loc=500,
                #         y_loc=1820
                #     )
                #     self.driver.find_element(by=AppiumBy.XPATH, value='//androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[14]').click()
                # except:
                #     pass
                
                # try:
                #     self.driver.find_element(by=AppiumBy.XPATH, value='//android.view.ViewGroup[@content-desc="Copy link"]').click()
                # except:
                #     pass
                
                # time.sleep(random.uniform(2,3))
                    
                # try:
                #     utils.get_element_wait_by_xpath(
                #         driver=self.driver,
                #         xpath='//android.view.ViewGroup[@content-desc="Copy link"]'
                #     ).click()
                # except Exception as e:
                #     print(f"Primary click failed: {e}. Trying alternate path.")
                #     utils.get_element_wait_by_xpath(
                #         driver=self.driver,
                #         xpath='//androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[14]'
                #     ).click()

                
                # Lấy dữ liệu từ bộ nhớ tạm (clipboard)
                # copied_uid = pyperclip.paste()

                # # In dữ liệu đã copy
                # print("******Dữ liệu đã copy:", copied_uid)
                # match = re.search(r'id=(\d+)', copied_uid)

                # if match:
                #     # Lưu chuỗi số vào biến khác
                #     profile_id = match.group(1)
                #     with open("account.txt", "a") as file:
                #         file.write(f"{profile_id}|{list_email[i]}|{password} \n")
                #     print("Chuỗi số đã trích xuất:", profile_id)
                # else:
                #     print("Không tìm thấy chuỗi số trong URL.")
    
                # # Click back
                # print("# Click back")
                # utils.get_element_wait_by_xpath(
                #     driver=self.driver,
                #     xpath='//android.view.ViewGroup[@content-desc="Back"]'
                # ).click()
                # time.sleep(random.uniform(2,3))
                
                # # Click Menu tab
                # print("# Click Menu tab")
                # # menu_element = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value='new UiSelector().descriptionContains("Menu")')
                # # menu_element.click()
                # utils.get_element_wait_by_xpath(
                #     driver=self.driver,
                #     xpath='//android.view.View[contains(@content-desc, "Menu, tab 5 of") or contains(@content-desc, "Menu, tab 6 of")]'
                # ).click()
                # time.sleep(random.uniform(2,3))
                
                # # Scroll to find log out btn to log out
                # print("# Scroll to find logout btn to logout")
                # utils.scroll_vertical_until_find_element_by_xpath(
                #     driver=self.driver,
                #     xpath='//android.view.ViewGroup[@content-desc="Log out"]',
                #     y_start=1600,
                #     y_end=600  
                # )
                
                # # Click logout btn
                # print("# Click logout btn")
                # utils.get_element_wait_by_xpath(
                #     driver=self.driver,
                #     xpath='//android.view.ViewGroup[@content-desc="Log out"]'
                # ).click()
                # time.sleep(random.uniform(2,3))
                
                # # CLick Not Now
                # print("# Click Not Now")
                # utils.get_element_wait_by_xpath(
                #     driver=self.driver,
                #     xpath='//android.widget.Button[@resource-id="com.facebook.katana:id/(name removed)" and @text="NOT NOW"]'
                # ).click()
                # time.sleep(random.uniform(2,3)) 
                
                # # Click logout
                # print("# Click logout")
                # utils.get_element_wait_by_xpath(
                #     driver=self.driver,
                #     xpath='//android.widget.Button[@resource-id="com.facebook.katana:id/(name removed)" and @text="LOG OUT"]'
                # ).click()
                # time.sleep(random.uniform(2,3)) 
                
                # # with open("account.txt", "a") as file:
                # #     file.write(f"{list_email[i]}|{password} \n")
                
                # #
                # print("# Open multitasking")
                # self.driver.press_keycode(187)
                # time.sleep(random.uniform(2,3)) 
                
                
                # # Scroll to close tab facebook
                # print("# Scroll to close tab facebook")
                # utils.scroll_by_vertical(
                #     driver=self.driver,
                #     x_loc=536,
                #     y_start=1289,
                #     y_end=128
                # )
                # time.sleep(random.uniform(2,3)) 
                
                # print("# Back to home phone")
                # self.driver.press_keycode(3)
                
                # Click hold facebook
                # print("# Click hold facebook")
                # fb_loc = utils.get_element_wait_by_xpath(
                #     driver=self.driver,
                #     xpath='//android.widget.TextView[@content-desc="Facebook"]'
                # )
                
                # x_loc = fb_loc.location["x"] + 145
                # y_loc = fb_loc.location["y"] + 112
                
                # print(f"x_loc=== {x_loc}, y_loc==== {y_loc}")
                
                # utils.click_hold_with_loc(
                #     driver=self.driver,
                #     x_loc=x_loc,
                #     y_loc=y_loc,
                # )
                # time.sleep(random.uniform(2,3)) 
                
                # Click APP info
                
                # app_info_element = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value='new UiSelector().descriptionContains("App info")')
                # app_info_element.click()
                print("# Click hold")
                self.driver.tap(
                    [(924, 294)],
                    duration=3000
                )
                time.sleep(random.uniform(2,3))
            
                print("# Click App infor")
                self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@resource-id="com.android.launcher:id/bubble_text" and @text="App info"]'
                ).click()
                time.sleep(random.uniform(3,4))
                
                # Click Storage & cache
                print("# Click clear cache")
                self.driver.find_element(by=AppiumBy.XPATH, value='//androidx.recyclerview.widget.RecyclerView[@resource-id="com.android.settings:id/recycler_view"]/android.widget.LinearLayout[5]/android.widget.RelativeLayout'
                ).click()
                time.sleep(random.uniform(2,3))
                
                
                # Click clear cache
                print("# Click clear cache")
                self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.Button[@resource-id="com.android.settings:id/button" and @text="Clear cache"]'
                ).click()
                time.sleep(random.uniform(2,3))
                
                # Click Clear storage
                print("# Click Clear storage")
                self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.Button[@resource-id="com.android.settings:id/button" and @text="Manage space"]'
                ).click()
                time.sleep(random.uniform(2,3))
                
                # Click ok 
                print("# Click ok")
                self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.Button[@resource-id="android:id/button1"]'
                ).click()
                time.sleep(random.uniform(8,10))
                
                print("# Open multitasking")
                self.driver.press_keycode(187)
                time.sleep(random.uniform(3,4)) 
                
                
                # Scroll to close tab facebook
                
                for _ in range(0, 2):
                    # Perform swipe without duplicate x_loc argument
                    self.driver.swipe(
                        start_x=536,  # Start x coordinate
                        start_y=1572, # Start y coordinate
                        end_x=557,    # End x coordinate (same as start to keep it vertical)
                        end_y=904,   # End y coordinate
                        duration=800  # Duration of the swipe
                    )
                    time.sleep(random.uniform(2,3)) 

                print("# Back to home phone")
                self.driver.press_keycode(3)
                time.sleep(random.uniform(30, 45)) 

if __name__ == '__main__':
    unittest.main()
    
    

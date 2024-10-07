import os
import random
import time
import threading
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

list_first_name = [
    "An", "Bảo", "Cúc", "Diễm", "Dung", "Giang", "Hiền", "Hương", "Hạnh", 
    "Kim", "Lan", "Linh", "Mai", "Mỹ", "Ngân", "Ngọc", "Nhung", "Như", "Oanh", "Phương", "Quỳnh", 
    "Thanh", "Thảo", "Thúy", "Thủy", "Trang", "Tuyết", "Trúc", "Uyên", "Vân", "Vi", "Vy", "Yến", 
    "Hoa", "Hà", "Thu", "Hồng", "Duyên", "Sương", "Liên", "Phượng", "Nhã", "Lệ", "Khanh", "Diệp", 
    "Bích", "Ánh", "Loan", "Khánh", "Hòa", "Tâm", "Tường", "Ái", "Mẫn", "Thắm", "Quế", "Tiên", "Thy", "Hạ"
]

list_last_name = [
    "Nguyễn", "Trần", "Lê", "Phạm", "Vũ", "Hoàng", "Đặng", "Bùi", "Ngô", "Dương",
    "Đỗ", "Hồ", "Lý", "Trương", "Tô", "Lưu", "Mai", "Tống", "Lâm", "Trịnh", "Đoàn", "Hà", "Nguyễn", 
    "Phan", "Thái", "Trí", "Nhật", "Hưng", "Vương", "Hồng", "Hà", "Hải", "Mạnh", "Khưu", "Đoàn", 
    "Lê", "Đinh", "Nhâm", "Lâm", "Quách", "Trí", "Hồng", "Lại", "Bạch", "Bùi"
]

list_email = [
    "vokhoa7574@nikolaxflem.com",
    "tinhviet8742@nikolaxflem.com",
    "nghiemtrang4061@nikolaxflem.com"
]

def create_profile_firefox(email):
    open_browser(email)

def open_browser(email):
    # Tạo options cho Firefox
    options = Options()
    options.set_preference("dom.webnotifications.enabled", False)  # Tắt thông báo
    # Khởi tạo WebDriver mới với các options đã cấu hình
    driver = webdriver.Firefox(options=options) 
    driver.set_window_size(500, 800)  # Thiết lập kích thước cửa sổ
    time.sleep(5)
    try:
        print(f"#. Mở trình duyệt cho email: {email}")
        driver.get("https://www.facebook.com/r.php")
        time.sleep(random.randint(3, 5))

        # Nhập thông tin để tạo tài khoản
        print("#. Nhập họ")
        driver.find_element(By.NAME, 'lastname').send_keys(random.choice(list_last_name))
        time.sleep(random.uniform(1, 2))

        print("#. Nhập tên")
        driver.find_element(By.NAME, 'firstname').send_keys(random.choice(list_first_name))
        time.sleep(random.uniform(1, 2))

        print("#. Nhập email")
        driver.find_element(By.NAME, 'reg_email__').send_keys(email)
        time.sleep(random.uniform(1, 2))

        print("#. Nhập mật khẩu")
        driver.find_element(By.ID, 'password_step_input').send_keys('123456A@')
        time.sleep(random.uniform(1, 2))

        # Chọn ngày tháng năm sinh
        print("#. Chọn ngày sinh")
        driver.find_element(By.NAME, 'birthday_day').send_keys(random.randint(1, 29))
        time.sleep(1)

        birthday_month = random.randint(1, 12)  # Tháng từ 1 đến 12
        driver.find_element(By.NAME, 'birthday_month').send_keys(f'Tháng {birthday_month}')
        time.sleep(1)

        driver.find_element(By.NAME, 'birthday_year').send_keys(random.randint(1987, 2006))
        time.sleep(1)

        # Chọn giới tính
        print("#. Chọn giới tính")
        driver.find_element(By.XPATH, "//input[@name='sex' and @value='1']").click()
        time.sleep(random.uniform(1, 2))

        # Nhấn nút đăng ký
        print("#. Nhấn nút đăng ký")
        driver.find_element(By.NAME, 'websubmit').click()
        time.sleep(random.uniform(20, 25))

        # Mở tab mới để lấy mã xác nhận từ email
        print("#. Mở email và lấy mã xác nhận")
        driver.execute_script("window.open('https://mail.nikolaxflem.com/')")
        time.sleep(5)

        driver.switch_to.window(driver.window_handles[1])
        time.sleep(5)

        print("#. Lấy mã xác nhận từ email")
        code_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'zlif__CLV-main__-259__su'))
        )
        code = code_element.text.split("FB-")[1].split(" ")[0]
        print(f"Mã xác nhận: {code}")

        # Quay lại tab đăng ký Facebook và nhập mã
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(5)

        print("#. Nhập mã xác nhận")
        driver.find_element(By.ID, 'code_in_cliff').send_keys(code)
        time.sleep(random.uniform(1, 2))

        # Nhấn nút tiếp tục để hoàn thành đăng ký
        print("#. Nhấn nút tiếp tục")
        driver.find_element(By.NAME, 'confirm').click()
        time.sleep(random.uniform(4, 5))

        print("Tài khoản đã được tạo thành công!")
        time.sleep(10)

    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")
    finally:
        driver.quit()

if __name__ == '__main__':
    threads = []

    # Khởi tạo 3 luồng để xử lý danh sách email
    for email in list_email:
        thread = threading.Thread(target=create_profile_firefox, args=(email,))
        thread.start()
        threads.append(thread)

        # Chỉ chạy tối đa 2 luồng cùng lúc
        if len(threads) == 1:
            for thread in threads:
                thread.join()
            threads = []  # Xóa danh sách luồng sau khi hoàn thành

    # Đợi các luồng còn lại hoàn tất
    for thread in threads:
        thread.join()

dfgf
import pyautogui
import time
import random
import string

# Configuration
DELAY_BETWEEN_ACTIONS = 2  # Default delay between actions
LONG_DELAY = 5  # Longer delay for certain actions

def wait(duration=DELAY_BETWEEN_ACTIONS):
    time.sleep(duration)

def click_at_position(x, y, clicks=1, button='left'):
    pyautogui.click(x=x, y=y, clicks=clicks, button=button)
    wait(2)

def type_text(text):
    pyautogui.write(text)
    wait(4)

def click_and_type(x, y, text, clicks=1):
    click_at_position(x, y, clicks)
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.press('backspace')
    type_text(text)

def generate_random_name(length=5):
    name = ''.join(random.choices(string.ascii_letters, k=length))
    number = random.randint(1, 99)
    return f"{name}{number}"

def perform_actions(actions):
    for action in actions:
        if action['type'] == 'click':
            click_at_position(action['x'], action['y'], action.get('clicks', 1), action.get('button', 'left'))
        elif action['type'] == 'type':
            type_text(action['text'])
        elif action['type'] == 'click_and_type':
            click_and_type(action['x'], action['y'], action['text'])
        elif action['type'] == 'wait':
            wait(action.get('duration', DELAY_BETWEEN_ACTIONS))
        elif action['type'] == 'hotkey':
            pyautogui.hotkey(*action['keys'])

        # In thông báo với khóa 'description' an toàn
        print(f"Performed action: {action.get('description', 'No description provided')}")

list_first_name = [
    "An", "Bảo", "Cúc", "Diễm", "Dung", "Giang", "Hiền", "Hương", "Hạnh", 
    "Kim", "Lan", "Linh", "Mai", "Mỹ", "Ngân", "Ngọc", "Nhung", "Như", "Oanh", "Phương", "Quỳnh", 
    "Thanh", "Thảo", "Thúy", "Thủy", "Trang", "Tuyết", "Trúc", "Uyên", "Vân", "Vi", "Vy", "Yến", 
    "Hoa", "Hà", "Thu", "Hồng", "Duyên", "Sương", "Liên", "Phượng", "Nhã", "Lệ", "Khanh", "Diệp", 
    "Bích", "Ánh", "Loan", "Khánh", "Hòa", "Tâm", "Tường", "Ái", "Mẫn", "Thắm", "Quế", "Tiên", "Thy", "Hạ"
]
list_last_name = [
    "Nguyễn", "Trần", "Lê", "Phạm", "Vũ", "Hoàng", "Đặng", "Bùi", "Ngô", "Dương",
    "Đỗ", "Hồ", "Lý", "Trương", "Tô", "Lưu", "Mai", "Tống", "Lâm", "Trịnh", "Đoàn", "Hà", "Lưu", "Nguyễn", "Phan", "Thái", "Trí", "Nhật", "Hưng",
    "Vương", "Hồng", "Hà", "Hải", "Phan", "Trịnh", "Mạnh", "Khưu", "Đoàn", "Lê",
    "Đinh", "Hoàng", "Nhâm", "Lâm", "Quách", "Trí", "Hồng", "Lại", "Bạch", "Bùi"
]

# Main execution
if __name__ == "__main__":
    wait(3)  # Initial delay to position the mouse

    # Generate random names and emails
    names = [generate_random_name(5) for _ in range(10)]
    random_name = random.choice(names)
    list_email = [
        "thitu1106@nikolaxflem.com"
        # "luongtuong7047@nikolaxflem.com"
    ]

    for email in list_email:
        random_name = random.choice(names)
        actions = [
            # Initial setup actions
            {'type': 'click', 'x': 247, 'y': 553, 'clicks': 2, 'description': "Double click at initial position"},
            {'type': 'click', 'x': 860, 'y': 475, 'description': "Click at position 1"},
            {'type': 'click', 'x': 1080, 'y': 718, 'description': "Click at position 2"},
            {'type': 'click', 'x': 802, 'y': 467, 'description': "Click at position 3"},
            {'type': 'click_and_type', 'x': 808, 'y': 467, 'text': random_name, 'description': "Enter random name"},
            {'type': 'click', 'x': 1089, 'y': 715, 'description': "Click at position 4"},
            {'type': 'click', 'x': 985, 'y': 680, 'description': "Click at position 5"},
            {'type': 'wait', 'duration': 3, 'description': "Wait for 5 seconds"},
            {'type': 'click', 'x': 1191, 'y': 65, 'description': "Click at position 6"},
            {'type': 'click', 'x': 1000, 'y': 120, 'description': "Click at position 7"},
            {'type': 'click_and_type', 'x': 474, 'y': 542, 'text': email, 'description': "Enter email"},
            {'type': 'click', 'x': 640, 'y': 620, 'description': "Click login button"},
            {'type': 'wait', 'duration': 3, 'description': "Wait for 5 seconds"},
            {'type': 'click_and_type', 'x': 500, 'y': 370, 'text': "123456A@", 'description': "Enter password"},
            {'type': 'wait', 'duration': 3, 'description': "Wait for 5 seconds"},
            {'type': 'click_and_type', 'x': 494, 'y': 430, 'text': "123456A@", 'description': "Confirm password"},
            {'type': 'click_and_type', 'x': 480, 'y': 498, 'text': "25", 'description': "Enter age"},
            {'type': 'click', 'x': 629, 'y': 811, 'description': "Click enter"},
            {'type': 'click', 'x': 789, 'y': 26, 'description': "Open new tab"},
            {'type': 'click_and_type', 'x': 283, 'y': 64, 'text': "https://mail.nikolaxflem.com/?loginOp=logout", 'description': "Enter domain"},
            {'type': 'hotkey', 'keys': ['enter'], 'description': "Press Enter"},
            {'type': 'click_and_type', 'x': 624, 'y': 393, 'text': email, 'description': "Enter email on nikolax"},
            {'type': 'click_and_type', 'x': 598, 'y': 424, 'text': "123456", 'description': "Enter password on nikolax"},
            {'type': 'click', 'x': 786, 'y': 460, 'description': "Click login on nikolax"},
            {'type': 'wait', 'duration': 3, 'description': "Wait for 3 seconds"},
            {'type': 'click', 'x': 1263, 'y': 113, 'description': "Click X"},
            {'type': 'click', 'x': 223, 'y': 270, 'description': "Click mozilla"},
            {'type': 'click', 'x': 956, 'y': 700, 'clicks': 2, 'description': "Double click"},
            {'type': 'click', 'x': 956, 'y': 700, 'button': 'right', 'description': "Right click"},
            {'type': 'click', 'x': 1000, 'y': 720, 'description': "Click copy"},
            {'type': 'click', 'x': 645, 'y': 19, 'description': "Click old tab"},
            {'type': 'click', 'x': 463, 'y': 668, 'description': "Click input"},
            {'type': 'click', 'x': 463, 'y': 668, 'button': 'right', 'description': "Right click"},
            {'type': 'click', 'x': 506, 'y': 823, 'description': "Click paste"},
            {'type': 'click', 'x': 634, 'y': 735, 'description': "Click confirm"},
            {'type': 'click', 'x': 634, 'y': 779, 'description': "Click start"},
            {'type': 'hotkey', 'keys': ['ctrl', 't'], 'description': "Open new tab"},
            {'type': 'click_and_type', 'x': 307, 'y': 69, 'text': "https://www.facebook.com/r.php "},
            {'type': 'hotkey', 'keys': ['enter'], 'description': "Press Enter"},
            {'type': 'wait', 'duration': 4, 'description': "Wait for 6 seconds"},
            {'type': 'click_and_type', 'x': 479, 'y': 318, 'text': random.choice(list_last_name), 'description': "Enter last name"},
            {'type': 'click_and_type', 'x': 676, 'y': 318, 'text': random.choice(list_first_name), 'description': "Enter first name"},
            {'type': 'click_and_type', 'x': 465, 'y': 511, 'text': email, 'description': "Enter email on Facebook"},
            {'type': 'click', 'x': 986, 'y': 372, 'description': "Click"},
            {'type': 'click_and_type', 'x': 461, 'y': 563, 'text': "123456A@", 'description': "Enter password on Facebook"},
            {'type': 'click', 'x': 640, 'y': 395, 'description': "Click month"},
            {'type': 'click', 'x': 643, 'y': 727, 'description': "Select month"},
            {'type': 'click', 'x': 781, 'y': 392, 'description': "Click year"},
            {'type': 'click', 'x': 832, 'y': 542, 'description': "Select year"},
            {'type': 'click', 'x': 770, 'y': 640, 'description': "Confirm year"},
            {'type': 'click', 'x': 667, 'y': 462, 'description': "Select gender"},
            {'type': 'click', 'x': 643, 'y': 733, 'description': "Click register"},
            {'type': 'click', 'x': 443, 'y': 306, 'description': "Click save"},
            {'type': 'click', 'x': 743, 'y': 24, 'description': "Switch to code tab"},
            {'type': 'click', 'x': 104, 'y': 69, 'description': "Reload page"},
            {'type': 'wait', 'duration': 5, 'description': "Wait for 5 seconds"},
            {'type': 'click', 'x': 104, 'y': 69, 'description': "Reload page again"},
            {'type': 'wait', 'duration': 3, 'description': "Wait for 5 seconds"},
            {'type': 'click', 'x': 228, 'y': 257, 'description': "Get code"},
            {'type': 'click', 'x': 715, 'y': 205, 'clicks': 2, 'description': "Double click code"},
            {'type': 'click', 'x': 715, 'y': 205, 'button': 'right', 'description': "Right click code"},
            {'type': 'click', 'x': 752, 'y': 226, 'description': "Click copy"},
            {'type': 'click', 'x': 921, 'y': 19, 'description': "Switch to Facebook tab"},
            {'type': 'click', 'x': 454, 'y': 347, 'description': "Click Facebook input"},
            {'type': 'click', 'x': 454, 'y': 347, 'button': 'right', 'description': "Right click Facebook input"},
            {'type': 'click', 'x': 505, 'y': 499, 'description': "Click paste"},
            {'type': 'click', 'x': 808, 'y': 470, 'description': "Click continue"},
            {'type': 'wait', 'duration': 7, 'description': "Wait for 7 seconds"},
            {'type': 'click', 'x': 899, 'y': 467, 'description': "Click OK"},
            {'type': 'wait', 'duration': 10, 'description': "Wait for 10 seconds"},
            {'type': 'click', 'x': 1172, 'y': 24, 'description': "Final click"}            
        ]
        perform_actions(actions)
        print(f"Completed actions with email: {email}")
    
    print("Automation completed.")

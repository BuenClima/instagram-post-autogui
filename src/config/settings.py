from dotenv import load_dotenv
from pathlib import Path
import pyautogui
import os

def set_image_file_path(screenshot_path):
    script_dir = os.path.dirname(__file__)
    return os.path.join(script_dir, "../assets/instagram/" + screenshot_path)

class Envinronment:

    def __init__(self) -> None:
        load_dotenv()
        env_path = Path('./../')/'.env'
        load_dotenv(dotenv_path=env_path)

    def get_username():
        return os.getenv("INSTAGRAM_USERNAME")

    def get_password():
        return os.getenv("INSTAGRAM_PASSWORD")

class Positions:
    
    def __init__(self) -> None:
        pass

    def current_position(self):
        while True:
            print(pyautogui.position())

    def get_accept_cookies_position():
        (x,y) = (955,639)
        return (x,y)

    def get_login_username_position():
        (x,y) = (1147,367)
        return (x,y)
    
    def get_login_password_position():
        (x,y) = (1147,424)
        return (x,y)

    def get_login_button_position():
        (x,y) = (1147,466)
        return (x,y)
    
    def get_post_button_position():
        (x,y) = (1277,126)
        return (x,y)
    
    def get_select_from_computer_button_position():
        (x,y) = (964,673)
        return (x,y)

    def get_crop_next_button_position():
        (x,y) = (1307,206)
        return (x,y)
    
    def get_filter_next_button_position():
        (x,y) = (1476,206)
        return (x,y)

    def get_caption_text_box_position():
        (x,y) = (1338,312)
        return (x,y)

    def get_share_button_position():
        (x,y) = (1476,206)
        return (x,y)

class Screenshots:

    def __init__(self) -> None:
        pass

    def get_accept_cookies_screenshot():
        return set_image_file_path("accept_all_cookies.png")

    def get_username_screenshot():
        return set_image_file_path("username.png")

    def get_password_screenshot():
        return set_image_file_path("password.png")

    def get_login_screenshot():
        return set_image_file_path("login.png")

    def get_post_screenshot():
        return set_image_file_path("post.png")

    def get_select_from_computer_screenshot():
        return set_image_file_path("select_from_computer.png")

    def get_next_screenshot():
        return set_image_file_path("next.png")

    def get_next2_screenshot():
        return set_image_file_path("next2.png")

    def get_caption_screenshot():
        return set_image_file_path("caption.png")
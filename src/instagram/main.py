from config.settings import Positions
from config.settings import Screenshots
from config.settings import Envinronment
from utils.main import Mouse
from utils.main import KeyBoard
from utils.main import Logger
from db.main import DB
import utils.main as Utils

class Instagram:

    def __init__(self) -> None:
        self.caption_position = None
        self.sharey_x_y = None
        self.db = DB()

    def accept_all_cookies(self):
        Logger.log("Accepting all cookies...")
        Utils.sleep(3)
        Mouse.move_and_click(Positions.get_accept_cookies_position())
    
    def fill_username(self):
        Logger.log("Filling username...")
        Utils.sleep(3)
        Mouse.move_and_click(Positions.get_login_username_position())
        KeyBoard.copy_and_paste(Envinronment.get_username())

    def fill_password(self):
        Logger.log("Filling password...")
        Utils.sleep(3)
        KeyBoard.tab()
        KeyBoard.copy_and_paste(Envinronment.get_password())
    
    def login(self):
        Logger.log("Login...")
        KeyBoard.enter()

    def start_post(self):
        Logger.log("Starting post creation...")
        Utils.sleep(3)
        Mouse.move_and_click(Positions.get_post_button_position())

    def is_session_active(self):
        Utils.sleep(3)
        if Mouse.locate_on_screen(Screenshots.get_post_screenshot()) is not None:
            Logger.log("IG Session is active...")
            return True
        Logger.log("IG Session is not active... ")
        return False

    def select_from_computer(self):
        Logger.log("Selecting picture from computer...")
        Utils.sleep(3)
        Mouse.move_and_click(Positions.get_select_from_computer_button_position())

    def search_picture(self, path):
        Logger.log("Searching image " + path)
        Utils.sleep(3)
        KeyBoard.search_bar()
        KeyBoard.delete()
        KeyBoard.copy_and_paste(path)
        KeyBoard.enter()
    
    def crop_picture(self):
        Logger.log("Cropping picture...")
        Utils.sleep(3)
        Mouse.move_and_click(Positions.get_crop_next_button_position())

    def filters_picture(self):
        Logger.log("Filtering picture...")
        Utils.sleep(3)
        Mouse.move_and_click(Positions.get_filter_next_button_position())

    def share(self):
        Logger.log("Sharing picture...")
        Utils.sleep(3)
        Mouse.move_and_click(Positions.get_share_button_position())

    def format_users(self, users):
        users_message = ""
        for user in users:
            if str(user).startswith('@'):
                users_message += user + " "
            else:
                users_message += "@" + user + " "
        return users_message
    
    def fill_caption(self, caption, users, tka_caption):
        Logger.log("Filling caption " + caption)
        Utils.sleep(3)
        Mouse.move_and_click(Positions.get_caption_text_box_position())
        KeyBoard.write(caption)
        KeyBoard.enter()
        KeyBoard.copy_and_paste(self.format_users(users))
        KeyBoard.enter()
        KeyBoard.copy_and_paste(tka_caption)

    def fill_ig_user(self, username, x_distance, y_distance):
        Logger.log("Filling ig user " + username)
        first_select_y_position = 80
        first_select_x_position = 100 + x_distance
        Utils.sleep(3)
        x = self.caption_position.left - first_select_x_position
        y = self.caption_position.top + y_distance
        Mouse.move_and_click(x, y)
        Utils.write(username)
        x = self.caption_position.left - first_select_x_position
        y = self.caption_position.top + first_select_y_position
        Utils.sleep(3)
        Mouse.move_and_click(x, y)

    def fill_ig_users(self, users):
        for i in range(len(users)):
            self.fill_ig_user(users[i], i*50, i*5)

    def post(self, posts):
        for post in posts:
            self.start_post()
            self.select_from_computer()
            self.search_picture(post['path'])
            self.crop_picture()
            self.filters_picture()
            self.fill_caption(post['caption'], post['users'], Utils.get_tka_caption())
            # self.fill_ig_users(post['users'])
            # self.share()
            self.db.update_post_as_published(post['id'])
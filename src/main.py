from browser.main import Browser as Browser
from instagram.main import Instagram as Instagram
from db.main import DB

class IGSession:
    
    def __init__(self) -> None:
        self.browser = Browser()
        self.instagram = Instagram()
        self.db = DB()
    
    def start_browser(self):
        self.browser.open_browser()

    def kill_session(self):
        self.db.close_connection()
        self.browser.close_browser()

    def login(self):
        self.instagram.accept_all_cookies()
        self.instagram.fill_username()
        self.instagram.fill_password()
        self.instagram.login()

    def get_posts(self):
        return self.db.get_unpublished_posts()
        

    def post_pictures(self):
        self.instagram.post(self.get_posts())


    def start_session(self):
        self.start_browser()
        if self.instagram.is_session_active() is False:
            self.login()
        self.post_pictures()


ig_session = IGSession()
ig_session.start_session()
ig_session.post_pictures()
ig_session.kill_session()
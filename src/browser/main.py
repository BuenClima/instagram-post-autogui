import webbrowser
import os

class Browser:

    chrome_executable_path = None

    def __init__(self) -> None:
        whereis_chrome = os.popen("whereis google-chrome-stable").read()
        if len(whereis_chrome) > 0:
            self.chrome_executable_path = whereis_chrome.split()[1]
            webbrowser.register('chrome',
                None,
                webbrowser.BackgroundBrowser(self.chrome_executable_path))

    def open_browser(self):
        webbrowser.get('chrome').open("https://www.instagram.com/")

    def close_browser(self):
        os.system("pkill chrome")
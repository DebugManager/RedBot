import easygui
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from pynput.keyboard import Key, Controller
import os


USER_LOGIN =
USER_PASSWORD =


class GifBot:
    def __init__(self):
        self.browser = webdriver.Firefox()
        self.allowed_formats = ['avi', 'divx', 'drc', 'flv', 'm4v', 'mkv', 'mov',
                                'mp4', 'mpeg', 'mpg', 'ogv',
                                'ogx', 'rm', 'rmvb', 'svi', 'vob', 'webm', 'wmv']
        self.video_names = []

    def allowed_video_from_path(self):
        files_and_directories = os.listdir(VIDEOS_PATH)
        file_names = [file for file in files_and_directories if os.path.isfile(os.path.join(VIDEOS_PATH, file))]
        self.video_names = list(filter(lambda i: i.split('.')[1] in self.allowed_formats, file_names))

    def open_main_page(self):
        self.browser.get('https://www.redgifs.com')

    def open_create_page(self):
        self.browser.get('https://www.redgifs.com/create')

    def open_login(self):
        self.browser.find_element(By.XPATH, "//button[@class='TabLink TabLink_isProfile']").click()

    def write_login_password(self, login, password):
        self.browser.find_element(By.XPATH, "//input[@id=':r0:']").send_keys(login)
        self.browser.find_element(By.XPATH, "//input[@id=':r1:']").send_keys(password)

    def click_video_select(self):
        self.browser.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div/div[2]/label/div/div[1]/div/button[1]').click()

    def open_video(self, video_name):
        keyboard = Controller()
        keyboard.type(VIDEOS_PATH + video_name)
        sleep(4)
        keyboard.press(Key.enter)
        sleep(1)
        keyboard.release(Key.enter)
        sleep(1)

    def click_button_by_text(self, text):
        self.browser.find_element(By.XPATH, f'//button[normalize-space()="{text}"]').click()


    def wait_while_upload(self):
        while True:
            try:
                self.browser.find_element(By.XPATH, f'//button[normalize-space()="Publish"]')
                return
            except:
                pass

    def start(self):
        self.allowed_video_from_path()
        print(self.video_names)
        self.open_main_page()
        self.open_login()
        self.write_login_password(USER_LOGIN, USER_PASSWORD)
        self.browser.implicitly_wait(3)
        sleep(30)
        for i in self.video_names:
            self.open_create_page()
            self.click_video_select()
            self.open_video(i)
            sleep(2)
            self.click_button_by_text('Next')
            sleep(2)
            self.click_button_by_text('Next')
            sleep(2)
            self.click_button_by_text('Cum')
            self.click_button_by_text('BBC')
            self.click_button_by_text('Ass')
            self.click_button_by_text("Next")
            self.wait_while_upload()
            self.click_button_by_text('Publish')
            sleep(5)


if __name__ == "__main__":
    VIDEOS_PATH = easygui.diropenbox(title="Choose folder", default="\\")
    if len(VIDEOS_PATH) > 2:
        VIDEOS_PATH += '\\'
        bot = GifBot()
        bot.start()
    else:
        print('Please choose folder')

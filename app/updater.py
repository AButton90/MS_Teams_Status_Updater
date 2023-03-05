from webdriver_manager.chrome import ChromeDriverManager

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

import PySimpleGUI as sg

from time import sleep


class UpdateTeams:

    def __init__(self):

        self.set_webdriver()
        # self.open_sites()

    def set_webdriver(self):

        # CMD chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\selenum\ChromeProfile"

        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        chrome_options = Options()
        chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), chrome_options=chrome_options)

    def open_sites(self):

        # try:
        ActionChains(self.driver).key_down(Keys.CONTROL).send_keys('t').key_up(Keys.CONTROL).perform()
        # WebDriverWait(driver=self.driver, timeout=60).until(EC.presence_of_element_located((By.TAG_NAME, "body"))).send_keys(Keys.COMMAND + "t")
        self.driver.switch_to.window(self.driver.window_handles[-1])
        # Open MS Teams
        self.driver.get("https://teams.microsoft.com/")

        while "login.microsoftonline" in self.driver.current_url:
            sg.theme('DarkBlack')
            layout_login = [[sg.Text('Please log into your MS Teams account.')],
                            [sg.Text('Click continue when you are logged in.')],
                            [sg.Button('Continue')]]

            window_login = sg.Window('Sign In Required', layout_login)
            event, values = window_login.read()
            window_login.close()

            # Open Local Host
            # WebDriverWait(driver=self.driver, timeout=60).until(EC.presence_of_element_located((By.CLASS_NAME, "user-picture"))).send_keys(Keys.CONTROL + "t")
            # self.driver.switch_to.window(self.driver.window_handles[-1])
            # self.driver.get("http://localhost:8003/")

        # except Exception as e:
        #     print(e)

    def go_to_local_host(self):

        for handle in self.driver.window_handles:
            self.driver.switch_to.window(handle)

            if "localhost:8003" in self.driver.current_url:
                break

    def go_to_teams(self):
        """Function that navigates to Teams online."""

        for handle in self.driver.window_handles:
            self.driver.switch_to.window(handle)

            if "teams" in self.driver.current_url:
                break

        WebDriverWait(driver=self.driver, timeout=60).until(EC.presence_of_element_located((By.CLASS_NAME, "user-picture")))

    def update_status(self, status, message):
        """Function that sets a user's status message on MS Teams with Selenium Webdriver"""

        self.go_to_teams()

        sleep(5)

        # Set Status
        WebDriverWait(driver=self.driver, timeout=60).until(EC.presence_of_element_located((By.CLASS_NAME, "user-picture"))).click()
        WebDriverWait(driver=self.driver, timeout=20).until(EC.presence_of_element_located((By.ID, "personal-skype-status-text"))).click()  # Status

        sleep(5)

        if status.lower() == "available":
            WebDriverWait(driver=self.driver, timeout=20).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[8]/ul/li[1]/button/static-skype-status/span/span/span[3]"))).click()
        elif status.lower() == "busy":
            WebDriverWait(driver=self.driver, timeout=20).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[8]/ul/li[2]/button/static-skype-status/span/span/span[3]"))).click()
        elif status.lower() == "dnd":
            WebDriverWait(driver=self.driver, timeout=20).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[8]/ul/li[3]/button/static-skype-status/span/span/span[3]"))).click()
        elif status.lower() == "brb":
            WebDriverWait(driver=self.driver, timeout=20).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[8]/ul/li[4]/button/static-skype-status/span/span/span[3]"))).click()
        elif status.lower() == "away":
            WebDriverWait(driver=self.driver, timeout=20).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[8]/ul/li[5]/button/static-skype-status/span/span/span[3]"))).click()
        elif status.lower() == "offline":
            WebDriverWait(driver=self.driver, timeout=20).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[8]/ul/li[6]/button/static-skype-status/span/span/span[3]"))).click()

        sleep(5)

        # Set Message
        WebDriverWait(driver=self.driver, timeout=60).until(EC.presence_of_element_located((By.CLASS_NAME, "user-picture"))).click()
        WebDriverWait(driver=self.driver, timeout=20).until(EC.presence_of_element_located((By.ID, "settings-dropdown-update-status-button"))).click()
        WebDriverWait(driver=self.driver, timeout=20).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[7]/settings-dropdown/div/div[2]/div[1]/div[1]/div[2]/div[2]/div/div/div"))).send_keys(message)
        WebDriverWait(driver=self.driver, timeout=20).until(EC.presence_of_element_located((By.ID, "setStatusNoteDone"))).click()

        self.go_to_local_host()

    def reset_status(self):

        self.go_to_teams()
        # Reset Status
        WebDriverWait(driver=self.driver, timeout=60).until(EC.presence_of_element_located((By.CLASS_NAME, "user-picture"))).click()
        WebDriverWait(driver=self.driver, timeout=10).until(EC.presence_of_element_located((By.ID, "personal-skype-status-text"))).click()  # Status
        WebDriverWait(driver=self.driver, timeout=10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[8]/ul/li[10]/button/span"))).click()  # Reset Status

        # Reset Message
        WebDriverWait(driver=self.driver, timeout=60).until(EC.presence_of_element_located((By.CLASS_NAME, "user-picture"))).click()
        WebDriverWait(driver=self.driver, timeout=10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[7]/settings-dropdown/div/div/ul/li[2]/button[2]/ng-include/svg/g/path[1]"))).click()  # Delete

        self.go_to_local_host()


if __name__ == '__main__':
    ut = UpdateTeams()

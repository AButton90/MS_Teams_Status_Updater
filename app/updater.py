from webdriver_manager.chrome import ChromeDriverManager

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

import time


import psutil
# from chromedevtools import ChromeDevTools


class UpdateTeams:

    def __init__(self):

        self.set_webdriver()
        


    def setup_driver(self):
        """Function that sets up the Selenium driver.  
           This function gets the session ID of an active browser session where the user is logged into their MS account"""

        pid_list = []
        # Find the PID of the browser window
        for proc in psutil.process_iter():
            if proc.name() == "chrome.exe":
                browser_pid = proc.pid
                for conn in psutil.net_connections(kind='inet'):
                    if conn.pid == browser_pid and conn.laddr.port != 0:
                        if conn.status == 'ESTABLISHED':
                            active_pid = proc.pid
                            break

        
        # # Get a list of all the open tabs in the browser
        # for browser_pid in pid_list:
        #     tabs = []
        #     if browser_pid is not None:
        #         for conn in psutil.net_connections(kind='inet'):
        #             if conn.pid == browser_pid and conn.laddr.port != 0:
        #                 tab = {
        #                     'url': conn.laddr.ip + ':' + str(conn.laddr.port),
        #                     'process_id': conn.pid,
        #                     'status': 'active' if conn.status == 'ESTABLISHED' else 'inactive'
        #                 }
        #                 tabs.append(tab)

        #     print(tabs)
        

        # Create a new WebDriver instance and attach it to the browser session
        # self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

        self.driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', desired_capabilities={})
        self.driver.session_id = active_pid

        # print(self.driver.execute_cdp_cmd('version', {}))
        # self.driver.command_executor._commands["send_command"] = ("POST", '/session/$sessionId/chromium/send_command')
        # params = {'cmd': 'Page.setDownloadBehavior', 'params': {'behavior': 'allow', 'downloadPath': 'C:\\Downloads'}}
        # command_result = self.driver.execute("send_command", params)
        # device_metrics = {
        #     'width': 375,
        #     'height': 667,
        #     'deviceScaleFactor': 2.0,
        #     'mobile': True
        # }
        # self.driver.execute_cdp_cmd("Emulation.setDeviceMetricsOverride", device_metrics)
        
        # # self.driver.execute_cdp_cmd("Browser.setBrowserContextForceContext", {"forceContext": True})
        # self.driver.execute_cdp_cmd("Target.attachToBrowserTarget", {"browserTargetId": f"target-1-{active_pid}"})

        self.driver.maximize_window()

    def go_to_local_host(self):

        self.driver.get("http://localhost:8003/")


    def set_webdriver(self):

        # CMD chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\selenum\ChromeProfile"

        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        chrome_options = Options()
        chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), chrome_options=chrome_options)

        print(self.driver.title)


    def go_to_teams(self):
        """Function that navigates to Teams online."""

        self.driver.find_element_by_tag_name("body").send_keys(CONTROL + "t")
        self.driver.switch_to.window(driver.window_handles[-1])

        self.driver.get("https://teams.microsoft.com/")

        try:
            WebDriverWait(driver=self.driver, timeout=60).until(EC.presence_of_element_located((By.CLASS_NAME, "user-picture")))
        
        except Exception as e:
            print(e)

    def update_status(self, status, message):
        """Function that sets a user's status message on MS Teams with Selenium Webdriver"""

        self.go_to_teams()

        # Set Status
        WebDriverWait(driver=self.driver, timeout=60).until(EC.presence_of_element_located((By.CLASS_NAME, "user-picture"))).click()
        WebDriverWait(driver=self.driver, timeout=10).until(EC.presence_of_element_located((By.ID, "personal-skype-status-text"))).click()  # Status

        if status == "available":
            WebDriverWait(driver=self.driver, timeout=10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[8]/ul/li[1]/button/static-skype-status/span/span/span[3]"))).click()
        elif status == "busy":
            WebDriverWait(driver=self.driver, timeout=10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[8]/ul/li[2]/button/static-skype-status/span/span/span[3]"))).click()
        elif status == "dnd":
            WebDriverWait(driver=self.driver, timeout=10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[8]/ul/li[3]/button/static-skype-status/span/span/span[3]"))).click()
        elif status == "brb":
            WebDriverWait(driver=self.driver, timeout=10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[8]/ul/li[4]/button/static-skype-status/span/span/span[3]"))).click()
        elif status == "away":
            WebDriverWait(driver=self.driver, timeout=10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[8]/ul/li[5]/button/static-skype-status/span/span/span[3]"))).click()
        elif status == "offline":
            WebDriverWait(driver=self.driver, timeout=10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[8]/ul/li[6]/button/static-skype-status/span/span/span[3]"))).click()
        
        # Set Message
        WebDriverWait(driver=self.driver, timeout=60).until(EC.presence_of_element_located((By.CLASS_NAME, "user-picture"))).click()
        WebDriverWait(driver=self.driver, timeout=10).until(EC.presence_of_element_located((By.ID, "settings-dropdown-update-status-button"))).click()        
        WebDriverWait(driver=self.driver, timeout=10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[7]/settings-dropdown/div/div[2]/div[1]/div[1]/div[2]/div[2]/div/div/div"))).send_keys(message)
        WebDriverWait(driver=self.driver, timeout=10).until(EC.presence_of_element_located((By.ID, "setStatusNoteDone"))).click()
    
    def reset_status(self):

        # Reset Status
        WebDriverWait(driver=self.driver, timeout=60).until(EC.presence_of_element_located((By.CLASS_NAME, "user-picture"))).click()
        WebDriverWait(driver=self.driver, timeout=10).until(EC.presence_of_element_located((By.ID, "personal-skype-status-text"))).click()  # Status
        WebDriverWait(driver=self.driver, timeout=10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[8]/ul/li[10]/button/span"))).click()  # Reset Status
        
        # Reset Message
        WebDriverWait(driver=self.driver, timeout=60).until(EC.presence_of_element_located((By.CLASS_NAME, "user-picture"))).click()
        WebDriverWait(driver=self.driver, timeout=10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[7]/settings-dropdown/div/div/ul/li[2]/button[2]/ng-include/svg/g/path[1]"))).click()  # Delete
    

    def test(self):

        # navigate to the initial URL in the first tab
        self.driver.get("https://www.google.com")

        time.sleep(10)
        WebDriverWait(driver=self.driver, timeout=10).until(EC.presence_of_element_located((By.TAG_NAME, "body"))).send_keys(Keys.CONTROL + "t")
        self.driver.switch_to.window(self.driver.window_handles[-1])

        # open a new tab and navigate to a URL
        self.driver.get("https://www.python.org/")

        time.sleep(10)
        WebDriverWait(driver=self.driver, timeout=10).until(EC.presence_of_element_located((By.TAG_NAME, "body"))).send_keys(Keys.CONTROL + "t")
        self.driver.switch_to.window(self.driver.window_handles[-1])

        # open another new tab and navigate to a URL
        self.driver.get("https://www.github.com")

        time.sleep(10)

        # iterate through the open tabs and print their window handles
        for handle in self.driver.window_handles:
            self.driver.switch_to.window(handle)
            print("Window handle: ", self.driver.title)

if __name__ == '__main__':
    ut = UpdateTeams()
    
    for handle in ut.driver.window_handles:
        ut.driver.switch_to.window(handle)
        print("Window handle: ", ut.driver.title)
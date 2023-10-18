from selenium import webdriver
from dotenv import load_dotenv
import os
load_dotenv('.env')
LT_USERNAME: str = os.getenv("LT_USERNAME")
LT_ACCESS_KEY: str = os.getenv("LT_ACCESS_KEY")
EXEC_PLATFORM: str = os.getenv('EXEC_PLATFORM')
class Setting:    
    def __init__(self, test_name: str):
        self.test_name: str = test_name
        if EXEC_PLATFORM=='cloud':
            options = webdriver.ChromeOptions()
            options.browser_version = "latest"
            options.platform_name = "Windows 10"
            lt_options = {}
            lt_options["username"] = os.getenv("LT_USERNAME")
            lt_options["accessKey"] = os.getenv("LT_ACCESS_KEY")
            lt_options["build"] = "JavaScript execution demos"
            lt_options["project"] = "Elements Check Tests"
            lt_options["name"] = self.test_name
            lt_options["console"] = "error"
            lt_options["w3c"] = True
            lt_options["plugin"] = "python-python"

            options.set_capability('LT:Options', lt_options)

            gridURL: str = f"https://{LT_USERNAME}:{LT_ACCESS_KEY}@hub.lambdatest.com/wd/hub"

            self.driver: webdriver = webdriver.Remote(command_executor=gridURL, options= options)
        elif EXEC_PLATFORM=='local':
            self.chrome_options = webdriver.ChromeOptions()
            # self.chrome_options.add_argument("--headless=new")
            self.driver: webdriver = webdriver.Chrome(options=self.chrome_options)
  
    def setUp(self)->None:
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
    def tearDown(self)->None:
        if (self.driver != None):
            self.driver.quit()
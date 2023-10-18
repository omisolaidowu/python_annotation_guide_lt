import sys
sys.path.append(sys.path[0] + "/..")
from setup.Setup import Setting
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# The following is imported for type-hinting purpose
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.chrome.webdriver import WebDriver


settings: Setting = Setting("Login test annotation demo")

driver: WebDriver = settings.driver

wait= WebDriverWait(driver, 5)

class PageObjects:
    email_id: str = "input-email"
    password_id: str = "input-password"
    button_value: str = "Login"
    ecom_url: str = "https://ecommerce-playground.lambdatest.io/index.php?route=account/login"


class Test_Ecom_Login(PageObjects):
    def test_should_login(self)->None:
        settings.setUp()
        driver.get(self.ecom_url)

        email_field: WebElement = wait.until(EC.presence_of_element_located((By.ID, self.email_id)))
        password_field: WebElement = wait.until(EC.presence_of_element_located((By.ID, self.password_id)))
        submit_button: WebElement = wait.until(EC.presence_of_element_located((By.XPATH, f'//input[@value="{self.button_value}"]')))

        email_field.send_keys("testemail@gmail.com")
        password_field.send_keys("wrongpassword")
        submit_button.click()
        settings.tearDown()



        


        


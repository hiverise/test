from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re


class test_Login_With_An_Invalid_Password(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://144.76.236.188/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_login_with_an_invalid_password(self):
        driver = self.driver
        driver.refresh()
        driver.get(self.base_url + "en/#/")
        for i in range(60):
            try:
                if self.is_element_present(By.XPATH, "//div[@id='app-search']/header/div/div/div/div[3]/div/a"): break
            except:
                pass
            time.sleep(1)
        else:
            self.fail("time out")
        driver.find_element_by_xpath("//div[@id='app-search']/header/div/div/div/div[3]/div/a").click()
        driver.find_element_by_id("form-id_username").clear()
        driver.find_element_by_id("form-id_username").send_keys("s.a.korotkii@gmail.com")
        driver.find_element_by_id("form-id_password").clear()
        driver.find_element_by_id("form-id_password").send_keys("12345678")
        driver.find_element_by_xpath("//button[@type='submit']").click()
        for i in range(60):
            try:
                if self.is_element_present(By.CSS_SELECTOR, "div.alert__content"): break
            except:
                pass
            time.sleep(1)
        else:
            self.fail("time out")
        text_error = driver.find_element_by_css_selector("div.alert__content").text
        try:
            self.assertEqual(text_error, driver.find_element_by_css_selector("div.alert__content").text)
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        driver.find_element_by_css_selector(
            "div.popup-wrapper.show > div.popup > div.popup__unit.is-outside-popup > a.popup__close.icon-mob3").click()
        driver.refresh()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()

import unittest
import time
from selenium import webdriver


class TestFormFill(unittest.TestCase):

    def test_formFill01(self):
        fields = ['First name*', 'Last name*', 'Email*']
        browser = webdriver.Chrome()
        browser.get("http://suninjuly.github.io/registration1.html")
        for field in fields:
            input_text = browser.find_element_by_xpath(f'//label[text()="{field}"]/following-sibling::input')
            input_text.send_keys('Any text')
        time.sleep(1)
        browser.find_element_by_css_selector('button.btn').click()
        time.sleep(1)
        success_text = browser.find_element_by_tag_name('h1').text
        self.assertEqual("Congratulations! You have successfully registered!", success_text, "Congratulations page "
                                                                                             "did not load.")
        time.sleep(3)
        browser.quit()


    def test_formFill02(self):
        fields = ['First name*', 'Last name*', 'Email*']
        browser = webdriver.Chrome()
        browser.get("http://suninjuly.github.io/registration2.html")
        for field in fields:
            input_text = browser.find_element_by_xpath(f'//label[text()="{field}"]/following-sibling::input')
            input_text.send_keys('Any text')
        time.sleep(1)
        browser.find_element_by_css_selector('button.btn').click()
        time.sleep(1)
        success_text = browser.find_element_by_tag_name('h1').text
        self.assertEqual("Congratulations! You have successfully registered!", success_text, "Congratulations page "
                                                                                             "did not load.")
        time.sleep(1)
        browser.quit()



if __name__ == "__main__":
    unittest.main()
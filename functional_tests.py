from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        print('setUp')
        self.browser = webdriver.Firefox()


    def tearDown(self):
        print('tearDown')
        self.browser.quit()


    def test_can_start(self):
        print('tear_can_start')
        self.browser.get('http://127.0.0.1:8000/')
        self.assertIn('to-Do', self.browser.title)
        self.fail('Final do Teste')

if __name__ == '__main__':
    unittest.main()


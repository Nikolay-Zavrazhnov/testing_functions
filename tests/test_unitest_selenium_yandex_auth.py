from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
import unittest
from Testing_functions.selenium_task import YandexPasportCheck
import os
from dotenv import load_dotenv, find_dotenv

class LoginPassw(unittest.TestCase):

    def test_authorization(self):

        load_dotenv(find_dotenv())
        yandex = YandexPasportCheck()

        result = yandex.authorization(login=os.getenv('YA_LOGIN'), password=os.getenv('YA_PASSWORD'))
        etalon = {'login': 'password'}

        self.assertEqual(etalon, result)

if __name__ == '__main__':
    unittest.main()

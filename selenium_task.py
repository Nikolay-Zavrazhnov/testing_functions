from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service

import os
from dotenv import load_dotenv, find_dotenv


class YandexPasportCheck:

    def __init__(self):
        path = Service('C:/Users/nikoanna/Desktop/Prifessional_work_Python/venv/geckodriver.exe')
        self.driver = webdriver.Firefox(service=path)


    def authorization(self, login, password):
        self.driver.get('https://passport.yandex.ru/auth/')

        self.driver.find_element(By.XPATH, '//input[@id="passp-field-login"]').send_keys(login)
        self.driver.find_element(By.XPATH, '//button[@id="passp:sign-in"]').click()
        self.driver.find_element(By.XPATH, '//input[@id="passp-field-passwd"]').send_keys(password)
        self.driver.find_element(By.XPATH, '//button[@id="passp:sign-in"]').click()

        return {login: password}




if __name__ == '__main__':
    yandex = YandexPasportCheck()
    load_dotenv(find_dotenv())

    yandex.authorization(os.getenv('YA_LOGIN'), os.getenv('YA_PASSWORD'))


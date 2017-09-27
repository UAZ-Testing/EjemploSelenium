# coding=utf-8

import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import unittest


class TestSelenium(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://www.google.com")

    def tearDown(self):
        self.driver.close()

    def test_prueba_selenium(self):
        caja = self.driver.find_element_by_name('q')
        caja.send_keys('Ingeniería de Software')
        caja.send_keys(Keys.RETURN)

        time.sleep(5)

        div = self.driver.find_element_by_id('res')
        lista = div.find_elements_by_tag_name('a')

        for elemento in lista:
            if elemento.text != '':
                print(elemento.text)


# Ejecuta las pruebas implementadas
if __name__ == '__main__':
    unittest.main()

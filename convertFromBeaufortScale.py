# -*- coding: UTF-8 -*-
from appium import webdriver
from time import sleep
import unittest
import page


class ConvertFromBeaufortScale(unittest.TestCase):
    def setUp(self):
        desired_caps = {
            'platformName': 'Android',
            #'platformVersion': '5.1',
            'deviceName': 'emulator-5554',
            #'deviceName': 'real_device_name',
            'appPackage': 'kr.sira.unit',
            'appActivity': 'kr.sira.unit.SmartUnit'
        }
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

        # sleep jest niewskazany - wywalić go i sprawdzić czy trwa ładowanie strony
        sleep(3.5)

    def tearDown(self):
        self.driver.quit()

    def test_convert_from_beaufort_scale(self):
        velocity_value = "7"
        velocity_unit = "Beaufort"
        expected_speed_kmh = "51"
        expected_speed_knot = "28"
        expected_speed_ms = "14"

        app_page = page.AppPage(self.driver)

        living_page = app_page.go_to_living_page()
        self.assertTrue(living_page.is_page_selected())

        living_page.click_velocity_element()\
            .click_input_element()\
            .enter_input(velocity_value)\
            .accept_input()\
            .click_unit_selector()\
            .select_unit(velocity_unit)\
            .swipe_down_using_specific_element(
            living_page.get_swipeable_life_area())

        self.assertTrue(living_page.get_value_kmh().text.startswith(expected_speed_kmh))
        self.assertTrue(living_page.get_value_knot().text.startswith(expected_speed_knot))
        self.assertTrue(living_page.get_value_ms().text.startswith(expected_speed_ms))

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(ConvertFromBeaufortScale)
unittest.TextTestRunner(verbosity=2).run(suite)

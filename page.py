# -*- coding: UTF-8 -*-
from pageElements import PageElements
from time import sleep


class AppPage(object):
    def __init__(self, driver):
        self.driver = driver
        self.category = "Default"

        # uwaga! Test jest wrażliwy na wersję językową!
        self.basic_page_title = "BASIC"
        # self.basic_page_title = "Podst."
        self.living_page_title = "LIVING"
        # self.living_page_title = "Życie"

    def get_current_page_category(self):
        return self.driver.find_element_by_xpath(
            "//*[contains(@resource-id, 'android:id/title') and @text='" + self.category + "']")

    def is_page_selected(self):
        return self.get_current_page_category().is_selected()

    def go_to_basic_page(self):
        self.get_page_category(self.basic_page_title).click()
        sleep(0.5)
        return BasicPage(self.driver)

    def go_to_living_page(self):
        self.get_page_category(self.living_page_title).click()
        sleep(0.5)
        return LivingPage(self.driver)

    def get_page_category(self, destination_category):
        return self.driver.find_element_by_xpath(
            "//*[contains(@resource-id, 'android:id/title') and @text='" + destination_category + "']")

    # Uwaga! "return self" może prowadzić do błędów jeśli zmieni sie stan strony!
    def swipe_left_using_specific_element(self, getter_method):
        dimensions = PageElements(getter_method()).get_dimensions()
        self.driver.swipe(dimensions.x + dimensions.width - 1, dimensions.y, 1, dimensions.y, 600)
        return self

    # Uwaga! "return self" może prowadzić do błędów jeśli zmieni sie stan strony!
    def swipe_down_using_specific_element(self, element_getter):
        dimensions = PageElements(element_getter).get_dimensions()
        self.driver.swipe(dimensions.x, dimensions.y + 1, dimensions.x, dimensions.y + dimensions.height - 1, 600)
        return self

    def click_velocity_element(self):
        element = self.driver.find_element_by_id("kr.sira.unit:id/tab1_layout3")
        element.click()
        return self

    def click_input_element(self):
        element = self.driver.find_element_by_id("kr.sira.unit:id/tab1_input")
        element.click()
        return self

    def enter_input(self, unit_value):
        element = self.driver.find_element_by_id("kr.sira.unit:id/tab1_num" + unit_value)
        element.click()
        return self

    def accept_input(self):
        element = self.driver.find_element_by_id("kr.sira.unit:id/tab1_numok")
        element.click()
        return self

    def click_unit_selector(self):
        element = self.driver.find_element_by_id("kr.sira.unit:id/tab1_selector")
        element.click()
        return self

    def select_unit(self, unit):
        element = self.driver.find_element_by_xpath(
            "//*[contains(@resource-id, 'android:id/text1') and @text='" + unit + "']")
        element.click()
        return self


    def get_swipeable_basic_area(self):
        return self.driver.find_element_by_id("kr.sira.unit:id/tab0_list")

    def get_swipeable_life_area(self):
        return self.driver.find_element_by_id("kr.sira.unit:id/tab1_list")

    def get_value_kmh(self):
        return self.driver.find_element_by_xpath(
            "//*[contains(@resource-id, 'kr.sira.unit:id/unit_kind') and @text='km/h']/../*[1]")

    def get_value_knot(self):
        return self.driver.find_element_by_xpath(
            "//*[contains(@resource-id, 'kr.sira.unit:id/unit_kind') and @text='knot']/../*[1]")

    def get_value_ms(self):
        return self.driver.find_element_by_xpath(
            "//*[contains(@resource-id, 'kr.sira.unit:id/unit_kind') and @text='m/s']/../*[1]")


class BasicPage(AppPage):
    def __init__(self, driver):
        AppPage.__init__(self, driver)
        self.category = self.basic_page_title


class LivingPage(AppPage):
    def __init__(self, driver):
        AppPage.__init__(self, driver)
        self.category = self.living_page_title


#living page - selected // true
#w przypadku speed nie da się zrobić asercji selected
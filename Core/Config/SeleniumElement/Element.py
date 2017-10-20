from selenium.webdriver.remote.webelement import WebElement

from Core.Config.DriverFactory import DriverFactory

__author__ = 'hnminh@outlook.com'


class BaseElement(object):
	def __init__(self, by, locator, is_list_element=False):
		self.__wrapper_element = self.__get_wrapper_element(by, locator, is_list_element)

	def click_to_element(self):
		self.__wrapper_element.click()

	def get_element_tag_name(self):
		return self.__wrapper_element.tag_name

	def get_element_text(self):
		return self.__wrapper_element.text

	def get_element_attribute(self, attribute_key):
		return self.__wrapper_element.get_attribute(attribute_key)

	def get_element_css_property(self, property_name):
		return self.__wrapper_element.get_property(property_name)

	def is_enable(self):
		return self.__wrapper_element.is_enabled()

	def is_selected(self):
		return self.__wrapper_element.is_selected()

	def is_displayed(self):
		return self.__wrapper_element.is_displayed()



	@staticmethod
	def __get_wrapper_element(by, locator, is_list_element):
		driver = DriverFactory.get_driver()
		if not is_list_element:
			return driver.find_element(by, locator)
		else:
			return driver.find_elements(by, locator)

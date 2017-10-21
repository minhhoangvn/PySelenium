__author__ = 'hnminh@outlook.com'


class BaseElement(object):
	def __init__(self, element):
		self.__wrapper_element = element

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

	@property
	def get_wrapper_element(self):
		return self.__wrapper_element

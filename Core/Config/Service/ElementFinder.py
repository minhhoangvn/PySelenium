from selenium.webdriver.remote.webelement import WebElement

from Core.Config.Settings import Settings
from Core.Exceptions.TestContextException import TestContextException
from Core.Utils.Constant import Constant

__author__ = 'hnminh@outlook.com'


class Find(object):
	__parent_element = None
	__target_element = None

	def __init__(self, by, locator, element_cls, parent_element=WebElement):
		self.__by = by
		self.__locator = locator
		self.__element_cls = element_cls
		self.__parent_element = parent_element
		self.__validate_params()

	@property
	def __driver(self):
		return Settings.THREAD_LOCAL.web_driver

	def __get__(self, obj, *args):
		self._wrapped_element()
		return self.__target_element

	def __getattribute__(self, item):
		if hasattr(Find, item):
			return object.__getattribute__(self, item)
		return self.__target_element.__getattribute__(item)

	def __getitem__(self, key):
		self._wrapped_element()
		return self.__target_element.__getitem__(key)

	def _wrapped_element(self):
		element = self._search_element()
		self.__target_element = self.__element_cls(element)

	def _search_element(self):
		if self.__parent_element is not None:
			return self.__parent_element.find_element(by=self.__by, value=self.__locator)
		else:
			return self.__driver.find_element(by=self.__by, value=self.__locator)

	def __validate_params(self):
		if self.__by is None:
			raise TestContextException("By value cannot be None type")
		if self.__locator is None:
			raise TestContextException("locator value cannot be None type")
		if self.__element_cls not in Constant.WEB_ELEMENT_CLASS:
			raise TestContextException(
				"Element Class is invalid, please using list classes below " + str(Constant.WEB_ELEMENT_CLASS))


class Finds(Find):
	pass


class FindUntil(Find):
	pass

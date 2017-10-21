from selenium.webdriver.remote.webelement import WebElement

from Core.Config.DriverFactory import DriverFactory
from Core.Exceptions.TestContextException import TestContextException
from Core.Utils.Constant import Constant

__author__ = 'hnminh@outlook.com'


class Find(object):
	def __init__(self, by, locator, element_cls, parent_element=WebElement):
		self.__by = by
		self.__locator = locator
		self.__element_cls = element_cls
		self.__parent_element = parent_element
		self.__validate_params()

	@property
	def __driver(self):
		return DriverFactory.get_driver()

	def __get__(self, obj, *args):
		element = self._search_element()
		self.__target_element = self.__element_cls(element)
		return self.__target_element

	def __validate_params(self):
		if self.__by is None:
			raise TestContextException("By value cannot be None type")
		if self.__locator is None:
			raise TestContextException("locator value cannot be None type")
		if self.__element_cls not in Constant.WEB_ELEMENT_CLASS:
			raise TestContextException(
				"Element Class is invalid, please using list classes below " + str(Constant.WEB_ELEMENT_CLASS))

	def _search_element(self):
		if self.__parent_element is not None:
			return 1
		else:
			return 2


class Finds(Find):
	pass


class FindUntil(Find):
	pass

__author__ = 'hnminh@outlook.com'
from selenium.webdriver.common.by import By

from Core.Config.SeleniumDriver.Chrome import Chrome
from Core.Config.SeleniumDriver.Firefox import Firefox
from Core.Config.SeleniumDriver.InternetExplorer import InternetExplorer
from Core.Config.SeleniumElement.Element import BaseElement
from Core.Exceptions.TestContextException import TestContextException


class ConstantMeta(type):
	def __call__(cls, *args, **kwargs):
		return cls

	def __getattr__(cls, key):
		return cls[key]

	'''
	not allow set attribute in constant class in case
	access directly to class 
	'''

	def __setattr__(cls, key, value):
		raise TestContextException("Cannot set value to Constant variable")


class Constant(metaclass=ConstantMeta):
	DRIVER_CREATOR_KEY = "driver_creator"
	WEB_DRIVER_KEY = "WEB_DRIVER"
	WEB_ELEMENT_CLASS = (BaseElement,)
	WEB_DRIVER_CLASS = (Chrome, Firefox, InternetExplorer)
	FINDER_OPTIONS = (
		By.ID, By.NAME, By.CSS_SELECTOR, By.CLASS_NAME, By.XPATH, By.LINK_TEXT, By.PARTIAL_LINK_TEXT, By.TAG_NAME)

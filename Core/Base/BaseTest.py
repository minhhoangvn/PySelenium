import os
import unittest

from Core.Config.DriverFactory import DriverFactory

__author__ = 'hnminh@outlook.com'


class BaseTest(unittest.TestCase):
	def __init__(self, *args, **kwargs):
		super(BaseTest, self).__init__(*args, **kwargs)
		self.__browser = os.environ.get('browser', 'chrome')
		self.__api_test = os.environ.get('api', False)

	def setUp(self):
		if not self.__api_test:
			DriverFactory.create_driver()

	def tearDown(self):
		if not self.__api_test:
			DriverFactory.dispose_driver()

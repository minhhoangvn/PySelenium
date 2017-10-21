__author__ = 'hnminh@outlook.com'
import os
from Core.Utils.Singleton import Singleton
from Core.Utils.Constant import Constant


class DriverFactory(metaclass=Singleton):
	__driver_creator = None

	@staticmethod
	def set_driver_options(options):
		DriverFactory.__driver_creator.set_driver_options(options)

	@staticmethod
	def set_driver_capabilities(capabilities):
		DriverFactory.__driver_creator.set_driver_desired_capabilities(capabilities)

	@staticmethod
	def create_driver():
		if DriverFactory.__driver_creator is None:
			for driver_creator in Constant.WEB_DRIVER_CLASS:
				if DriverFactory.get_browser_running() in driver_creator.__module__:
					DriverFactory.__driver_creator = driver_creator()
		DriverFactory.__driver_creator.create_driver()

	@staticmethod
	def get_driver():
		return DriverFactory.__driver_creator.driver

	@staticmethod
	def dispose_driver():
		DriverFactory.__driver_creator.dispose_driver()
		DriverFactory.__driver_creator = None

	@staticmethod
	def get_browser_running():
		return os.environ.get('browser', 'chrome')

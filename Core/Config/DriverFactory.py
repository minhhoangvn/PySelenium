__author__ = 'hnminh@outlook.com'
from Core.Config.SeleniumDriver.Chrome import Chrome
from Core.InternalAPI.Singleton import Singleton


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
			DriverFactory.__driver_creator = Chrome()
		DriverFactory.__driver_creator.create_driver()

	@staticmethod
	def get_driver():
		return DriverFactory.__driver_creator.driver

	@staticmethod
	def dispose_driver():
		DriverFactory.__driver_creator.dispose_driver()

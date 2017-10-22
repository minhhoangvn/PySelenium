__author__ = 'hnminh@outlook.com'
import os

from Core.Config.Settings import Settings
from Core.Utils.Constant import Constant
from Core.Utils.Singleton import Singleton


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
		if getattr(Settings.THREAD_LOCAL, Constant.DRIVER_CREATOR_KEY, None) is None:
			for driver_creator in Constant.WEB_DRIVER_CLASS:
				if DriverFactory.get_browser_running() in driver_creator.__module__:
					Settings.THREAD_LOCAL.driver_creator = driver_creator()
		Settings.THREAD_LOCAL.driver_creator.create_driver()
		Settings.THREAD_LOCAL.web_driver = Settings.THREAD_LOCAL.driver_creator.driver

	@staticmethod
	def get_driver():
		return Settings.THREAD_LOCAL.web_driiver

	@staticmethod
	def dispose_driver():
		if getattr(Settings.THREAD_LOCAL, Constant.DRIVER_CREATOR_KEY, None) is not None:
			Settings.THREAD_LOCAL.driver_creator.dispose_driver()

	@staticmethod
	def get_browser_running():
		return os.environ.get('browser', 'chrome')

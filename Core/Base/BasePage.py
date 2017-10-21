from Core.Config.DriverFactory import DriverFactory

__author__ = 'hnminh@outlook.com'


class BasePage(object):
	@property
	def driver(self):
		return DriverFactory.get_driver()

	def open_page(self):
		pass

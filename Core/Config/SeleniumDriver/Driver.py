__author__ = 'hnminh@outlook.com'


class SeleniumDriver(object):
	def __init__(self):
		self.__options = None
		self.__capabilities = None
		self._driver = None

	def create_driver(self):
		raise NotImplementedError

	@property
	def options(self):
		return self.__options

	@options.setter
	def options(self, options):
		self.__options = options

	@property
	def capabilities(self):
		return self.__capabilities

	@capabilities.setter
	def capabilities(self, capabilities):
		self.__capabilities = capabilities

	@property
	def driver(self):
		if self._driver is None:
			raise RuntimeError("Please call create driver before get")
		return self._driver

	def dispose_driver(self):
		if self._driver is not None:
			self.driver.quit()
			self._driver = None

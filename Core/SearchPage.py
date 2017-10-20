__author__ = 'hnminh@outlook.com'


class SearchPage(object):
	def print_log(self):
		print("log function")


class Run(object):
	__data = None

	def init_search_page(self):
		if self.__data is None:
			self.__data = SearchPage()

	def get_search_page(self):
		return self.__data

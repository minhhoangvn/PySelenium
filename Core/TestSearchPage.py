import sys
from Core.SearchPage import Run
__author__ = 'hnminh@outlook.com'

class TestSearchPage(object):

	def run(self):
		Run.get_search_page().print_log()
__author__ = 'hnminh@outlook.com'
from selenium.webdriver.common.by import By

from Core.Config.Service.ElementFinder import Find


class SearchPage(object):
	txt_search = Find(by=By.ID, locator="lst-ib")

	def input_search(self, input_value):
		self.txt_search.send_key(input_value)

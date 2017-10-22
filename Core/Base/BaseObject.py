__author__ = 'hnminh@outlook.com'
from Core.Config.Service.ElementFinder import Find


class BaseObject(object):
	@property
	def find_by(self):
		return Find

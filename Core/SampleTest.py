from Core.Config.DriverFactory import DriverFactory
from .BaseTest import BaseTest

__author__ = 'hnminh@outlook.com'


class TestSample(BaseTest):
	def __init__(self, *args, **kwargs):
		super(TestSample, self).__init__(*args, **kwargs)

	def test_sample_google(self):
		driver = DriverFactory.get_driver()
		driver.get('http://www.google.com')

	def test_sample_vtc(self):
		driver = DriverFactory.get_driver()
		driver.get('http://vtc.vn')

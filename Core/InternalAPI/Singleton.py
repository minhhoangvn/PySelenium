__author__ = 'hnminh@outlook.com'


class Singleton(type):

	def __init__(cls, name, bases, attr, **kwargs):
		return super().__init__(name, bases, attr, **kwargs)

	def __new__(mcs, name, bases, attr, **kwargs):
		mcs.__instance = {}
		return type.__new__(mcs, name, bases, attr, **kwargs)

	def __call__(cls, *args, **kwargs):
		if cls not in cls.__instance:
			cls.__instance[cls] = super(Singleton, cls).__call__(*args, **kwargs)
		return cls.__instance[cls]

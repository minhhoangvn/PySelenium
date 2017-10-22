import threading

from Core.Utils.Constant import ConstantMeta

__author__ = 'hnminh@outlook.com'


class Settings(metaclass=ConstantMeta):
	THREAD_LOCAL = threading.local()
	THREAD_LOCK = threading.Lock()

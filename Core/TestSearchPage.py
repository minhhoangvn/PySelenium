class ValueA(object):
	def click(self):
		print("click action A")


class ValueB(object):
	def click(self):
		print("click action B")


class Find(object):
	value = None

	def __init__(self, value):
		self.value = value

	def __get__(self, obj, *args):
		print(obj)
		print(*args)
		return self.value

	def __getattribute__(self, item):
		if hasattr(Find, item):
			return object.__getattribute__(self, item)
		return self.value.__getattribute__(item)

	def __getitem__(self, key):
		return self.value.__getitem__(key)


class StubPage:
	numbera = Find(ValueA())
	numberb = Find(ValueB())

	def action_stub_page(self):
		self.numbera.click()
		self.numberb.click()

a = ValueA()
b = ValueB()
numbera = Find(a)
numberb = Find(b)
numbera.click()
numberb.click()
s = StubPage()
s.action_stub_page()
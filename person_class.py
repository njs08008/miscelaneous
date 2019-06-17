class Person():
	def __init__(self, first_name, last_name, *args, **kwargs):
		self.name_attrs = ['first_name', 'middle_name', 'last_name', 'suffix']
		self.first_name = first_name
		self.last_name = last_name
		self.__dict__.update(kwargs)

	def has_suffix(self):
		if hasattr(self, 'suffix'):
			return bool(self.suffix)
		else:
			return False

	def print_legal_name(self):
		names_parts = [getattr(self, x) for x in self.name_attrs if hasattr(self, x) and getattr(self, x)]
		full_name = ' '.join(names_parts)
		print('Legal name: %s' % full_name)

	def print_age(self):
		try:
			print(self.age)
		except AttributeError as err:
			print(err)

def run_example_person():
	me = Person('Nicholas', 'Stanford', middle_name='John', age=28, title='The Awesome')
	me.name_attrs = ['title'] + me.name_attrs
	me.print_legal_name()
	print('Has suffix: %s' % me.has_suffix())
	me.print_age()

if __name__ == '__main__':
	run_example_person()

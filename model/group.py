class Group:

	def __init__(self, number_class = None, name_class = None, subject_list = None, class_code = None):
		self.number_class = number_class
		self.name_class = name_class
		self.subject_list = subject_list
		self.class_code = class_code


	def __repr__(self):
		return "%s:%s" % (self.class_code, self.name_class)
		

	def __eq__(self, other):
		return self.class_code == other.class_code and self.name_class == other.name_class
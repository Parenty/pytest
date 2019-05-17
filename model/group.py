class Group:

	def __init__(self, number_class = None, name_class = None, subject_list = None, id = None):
		self.number_class = number_class
		self.name_class = name_class
		self.subject_list = subject_list
		self.id = id


	def __repr__(self):
		return "%s:%s" % (self.id, self.name_class)
		

	def __eq__(self, other):
		return self.id == other.id and self.name_class == other.name_class
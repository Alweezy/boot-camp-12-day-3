class BinarySearch(list):

	def __init__(self, a, b):
		self.a = a
		self.b = b

		"""
			poulate the list b with valid content with it's lenght determined
			by a.
	
		"""
		for number in range(self.a):
			list.append(self, self.b)
			self.b += b

		self.length = self.a
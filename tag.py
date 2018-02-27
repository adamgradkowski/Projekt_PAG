class Tag(object):
	''' Tag klasa abstrakcyjna przedstawiajaca pojedynczy znacznik w pliku html

	Atrybuty:
		tag_start (str): poczatek znacznika
		tag_end (str): koniec znacznika
		content (str): zawartosc pomiedzy poczatkiem i koncem znacznika
	'''

	def __init__(self, name, contents='' , id_tag = None, class_tag = None):
		'''Tag init method

		Args:
			name (str): nazwa znacznika 
			content (str): wybrana zawartosc znacznika
		'''
		if id_tag and class_tag:
			self.start_tag = '<{} id="{}" class="{}">'.format(name, id_tag, class_tag)
		elif class_tag:
			self.start_tag = '<{} class="{}">'.format(name, class_tag)
		elif id_tag:
			 self.start_tag = '<{} id="{}">'.format(name, id_tag)
		else:
			self.start_tag = '<{}>'.format(name)

		self.id = id_tag
		self.clas = class_tag
		self.end_tag = '</{}>'.format(name)
		self.contents = contents
		self.elem_content = []
		self.tag_style = {}

	def add_elem(self, elem):

		self.elem_content.append(elem)

	def add_style(self, name, value):
		self.tag_style.update({name:value}) 
	
	def __str__(self):
		''' metoda __str__ zwraca wszystkie atrybuty Tag'a
		'''

		return "{0.start_tag}{0.contents}{0.end_tag}".format(self)
	
	def display(self, file=None):
		''' wyswietla obiekt - siebie
		'''
		self.contents = ''
		if self.elem_content:
			for elem in self.elem_content: #h2 #h5
				self.contents += '\n'
				self.contents += '\t'
				self.contents += elem.start_tag
				self.contents += '\n'
				self.contents += '\t\t'
				self.contents += elem.contents
				if elem.elem_content:
					for ele in elem.elem_content: #h3
						self.contents += '\n'
						self.contents += '\t\t'
						self.contents += ele.start_tag
						self.contents += '\n'
						self.contents += '\t\t\t'
						self.contents += ele.contents
						if ele.elem_content:
							for el in ele.elem_content: #h4
								self.contents += '\n'
								self.contents += '\t\t\t'
								self.contents += el.start_tag
								self.contents += '\n'
								self.contents += '\t\t\t\t'
								self.contents += el.contents
								self.contents += '\n'
								self.contents += '\t\t\t'
								self.contents += el.end_tag
						self.contents += '\n'
						self.contents += '\t\t'
						self.contents += ele.end_tag

				self.contents += '\n'
				self.contents += '\t'
				self.contents += elem.end_tag

		self.contents += '\n'
		print(self, file=file)

	
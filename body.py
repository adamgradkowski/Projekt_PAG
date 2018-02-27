from tag import Tag

class Body(Tag):
	'''Klasa Body reprezentujaca reprezentujaca cala czesc 'fizyczna' pliku html

	Atrybuty:
	dziedziczone:
		name (str): nazwa 'body'
		content (str): zawartosc czesc body
	nowe:
		body_content([]): tablicza przechowyjaca znaczniki
 	'''

	def __init__(self):
		''' Body init method

		Args:
		name (str) : body
		content(str) : wpowadzana zawartosc
		content_body([]) : dodawane elementy
		'''
		super().__init__('body', '')
		self._body_contents = []

	def add_tag(self, elem):
		''' Dodawanie nowego tagu do tablicy , tworzony jest nowy tag

		Args:
			name (str): nazwa tagu
			content (str): zawartosc tagu
		
		'''
		self.elem_content.append(elem)


	def display(self, file=None):
		'''
		dziedziczy metode display() po Tag'u, ponadto do atrybuty content dodawany sa zawartosc wszystkich Tag'ow z tablicy body_content
		'''

		#for tag in self._body_contents:
		#	self.contents += str(tag)

		super().display(file=file)
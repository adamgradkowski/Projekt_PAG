from tag import Tag

class DocType(Tag):
	'''
	Klasa dziedziczaca po Tag'u, sluzy do stworzenia obiektu jakim jest DOCTYPE
	'''
	def __init__(self):
		super().__init__('!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" http://www.w3.org/TR/html4/strict.dtd','')
		self.end_tag = ''
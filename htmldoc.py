class HtmlDoc(object):
	'''klasa reprezentujaca caly plik html 

	Atrybuty:
	_doc_type (DocType) : info o pliku html
	_head (Head): czesc head pliku html
	_body (Body): czesc body pliku html

	'''

	def __init__(self, doc_type, head, body):
		'''Method __init__

		'''
		self._doc_type = doc_type
		self._head = head
		self._body = body

	def add_tag(self, name, contents):
		''' do czesc Body() uzywana jest metoda ktora dodaje elementy Tag() do tablicy
		'''
		self._body.add_tag(name, contents)

	def display(self, file=None):
		'''Wykorzystanie metody display() kazdego z agregatu
		'''
		self._doc_type.display(file=file)
		print('<html>', file=file)
		self._head.display(file=file)
		self._body.display(file=file)
		print('</html>', file=file)
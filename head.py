from tag import Tag

class Head(Tag):
	'''
	Klasa Head() reprezentuje sekcje head strony html

	Atrybuty:
		title_tag(Tag): tytul stroony tytuowej

	Metody:
		add_style(): uzywana w celu dodania do pliku html style css
		display(): sluzy do nadpisania czesci head do pliku html 
	'''
	def __init__(self, title=None):
		super().__init__('head', '')
		if title:
			self._title_tag = Tag('title', title)



	def add_style(self, name):
		style = '<link rel="stylesheet" href="' + name + '">'
		self.elem_content.append(style)

	def display(self, file=None):
		self.contents += str(self._title_tag)
		for elem in self.elem_content:
			self.contents +=str(elem)

		print(self, file=file)
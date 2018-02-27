from tag import Tag

class Style(object):
	''' Klasa do POPRAWY
	klasa sluzaca do stworzenia pliku .css i dolaczenie go do pliku .html

	Atrybuty:
		name(str): nazwa pliku .css
		elements(List): kontener do umieszania stylow css poszczegolnych elementow strony .html

	Metody:
		add_elem(): dodawanie elementow do zmiennej elements
		display(): sluzy do nadpisania stylow do pliku .css 
	'''
	def __init__(self, name):
		self.name = name
		self.elements = []
		self.content = ''

	#def __str__(self):
	#	return "{0.name}".format(self)

	def add_elem(self, name):
		self.elements.append(name)
		print(len(self.elements))

	def display(self, file=None):
		for element in self.elements:
			if type(element) is Tag:
				if element.id and element.clas:
					self.content = self.content + '#' + element.id + '.' + element.clas + ' {' + '\n'
					for keys,values in element.tag_style.items():
						self.content = self.content + keys + ' : ' + values +';' + '\n'
					self.content += '}'
				if element.clas and element.id == '':
					self.content = self.content + '.' + element.clas + ' {' + '\n'
					for keys,values in element.tag_style.items():
						self.content = self.content + keys + ' : ' + values +';' + '\n'
					self.content += '}'
				
				if element.id and element.clas == '':
					self.content = self.content + '#' + element.id + ' {' + '\n'
					for keys,values in element.tag_style.items():
						self.content = self.content + keys + ' : ' + values  +';' + '\n'
					self.content += '}'
				
			self.content += '\n'
			
					#print('#'+element.id + '{' + '\n' + str(element.tag_style) + '}')
		#print(content)
			#el = str(element) + ' {\n}\n'
			#self.content += el 

		print(self.content)
		print(self.content, file=file)
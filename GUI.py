from tkinter import *
from tag import Tag
from htmldoc import HtmlDoc
from head import Head
from body import Body 
from doctype import DocType
from style import Style
import webbrowser as wb

from tkinter import filedialog as fd

def browsefunc():
    filename = fd.askopenfilename()
    print(filename)



def cretePage():
	'''
	Fukcja twrozaca pliki index.html oraz mystyle.css w docelowym folderze gdzie znajduja sie pliki .py
	wykonyje funcje display() w istniejacych klasach HtmlDoc() oraz Style(). 
	Wykonywana używając przycisku pageButton klasy Button(). 
	'''
	with open('index.html', 'w') as page:
		my_page.display(file=page)

	with open('mystyle.css', 'w') as style_:
		style.display(file=style_)

	print("Wykonano funkcje createPage")

def showPage():
	'''
	Funckja wyswietlająca w przeglądarce internetowej ostatnio utworzona wersje strony 
	'''
	wb.open('index.html')


'''
Zmienne globalne, ktore sluza do umieszczania w nich poszczegolnych czesci strony .html oraz .css
'''
body = Body()
new_docType = DocType()
new_header = Head('Aggregat title')
new_header.add_style('mystyle.css')
my_page = HtmlDoc(new_docType, new_header, body)
style = Style('mystyle.css')


class mainGUI(Tk):
	'''
	Klasa reprezentujaca poweirzchnie graficzna aplikacji, dziedziczaca po klasie Tk

	Atrybuty:
	geometry: odziedziczona po tkinter
	frame: odziedziczona po tkinter
	
	dodatkowymi czesciami sa:
	conteiner: przestrzen sluzaca przechowywania zawartosci
	quitButton: przycisk wyjscia
	menubar: Menu przypiete z gornej czesci aplikacji
	
	Metody:
		showFrame: sluzy do przelaczania widoku, automactzynie ustawiona jest strona startowa, wykonywana przy przelaczaniu widokow
	'''


	def __init__(self, *args, **kwargs):
		Tk.__init__(self, *args, **kwargs)
		self.geometry("640x540+300+100")
		self.frames = {}

		container = Frame(self)
		container.pack(side="top", fill="both", expand = True)
		container.grid_rowconfigure(0, weight=1)
		container.grid_columnconfigure(0, weight=1)

		quitButton = Button(self, text="Quit", command=self.quit).pack(anchor = SE)

		menubar = Menu(container)
		filemenu = Menu(menubar, tearoff=0)
		filemenu.add_command(label="Dodaj Diva", command = lambda: self.show_frame(DivPage))
		menubar.add_cascade(label="Edycja", menu=filemenu)

		Tk.config(self, menu=menubar)

		for F in (StartPage, DivPage):
			frame = F(container,self)
			self.frames[F] = frame 
			frame.grid(row=0, column=0, sticky="nsew")

		
		self.show_frame(StartPage)

	def show_frame(self, cont):
		frame = self.frames[cont]
		frame.tkraise()

class StartPage(Frame):
	'''
	Klasa reprezentujaca pierwsza strone startowa, dziedziczy po klasie Frame

	sklada sie z napisow oraz przyciskow
	'''

	def __init__(self, patern, controller):
		Frame.__init__(self, patern)

		conteiner = Frame(self, bg = 'yellow')
		conteiner.pack(expand=YES, fill=BOTH)

		label = Label(conteiner, text="Probuj stworzyc swoja strone, przejdz do edycji i wybierz opcje ktora chcesz umiescic", padx=10, pady=10)
		label.pack()
		label = Label(conteiner, text="Nastepnie wybierz element, nadaj mu stylow css", padx=10, pady=10)
		label.pack()
		label = Label(conteiner, text="Wróc do poprzedniej opcji i najpierw uzyj przycisku stwórz strone a następnie zobacz ją w przeglądarce", padx=10, pady=10)
		label.pack()

		pageButton = Button(conteiner, text="Stwórz strone", command=cretePage).pack(anchor = CENTER)

		showPageButton = Button(conteiner, text="Zobacz strone", command=showPage).pack(anchor = CENTER)


class DivPage(Frame):
	'''
	Klasa reprezentujaca wybor opcji jaki daje menu do tworzenia konkretnej czesci strony jaka jest div. 

	Atrubuty:



	Metody:
		createDiv:

		pochylona:
		pogrubiona:
		podkreslona:
	'''

	def __init__(self, patern, controller):
		Frame.__init__(self, patern)

		self.mvar = IntVar()
		self.nvar = IntVar()
		self.ovar = IntVar()
		self.div = Tag('div')
		self.val_B = 0
		self.val_U = 0
		self.val_I = 0


		conteiner = Frame(self, bg = 'yellow')
		conteiner.pack(expand=YES, fill=BOTH)

		top_frame = Frame(conteiner, bg = 'red',)
		top_frame.pack(side=TOP, expand=NO,  padx=10, pady=5, ipadx=5, ipady=5, fill = X) 

		bottom_frame = Frame(conteiner, bg = 'blue', height = 400)
		bottom_frame.pack(side=BOTTOM, expand=YES, padx=10, pady=5, fill=BOTH)

		text_frame = Frame(top_frame, bg = 'green', height = 150, width=600)
		text_frame.pack(side=LEFT, expand=NO, padx=10, pady=5, ipadx=5, ipady=5, fill = BOTH)  

		id_frame = Frame(top_frame, bg = 'black', height = 150, width=105)
		id_frame.pack(side=RIGHT, expand=NO, fill=Y, ipadx=5, ipady=5, ) 

		label_text = Label(text_frame, text="Miejsce przeznaczone na wprowadzenie tekstu")
		label_text.pack(side = TOP) 

		T_content = Text(text_frame,height=10, width=53)
		T_content.pack(side = BOTTOM)

		label_id = Label(id_frame, text="wprowadz id dla diva")
		label_id.pack()
		T_id = Text(id_frame,height=1, width=8)
		T_id.pack()
		label_class = Label(id_frame, text="wprowadz class'e dla diva")
		label_class.pack()
		T_class = Text(id_frame,height=1, width=8)
		T_class.pack()
		label_div = Label(id_frame, text="Chcesz umiescic diva w divie ?")
		label_div.pack()
		T_div_id = Text(id_frame,height=1, width=8)
		T_div_id.pack()
		backButton = Button(id_frame, text="Wróc",command=lambda: controller.show_frame(StartPage)).pack()
		createButton = Button(id_frame, text="Stwórz", command=lambda: self.createDiv(T_content, T_id, T_class, self.val_B, self.val_U, self.val_I, T_div_id)).pack()

		label_menu = Label(bottom_frame, text="Ustawienie tekstu")
		label_menu.grid(row=0, column=0)

		check = Frame(bottom_frame)
		checkB = Checkbutton(check, text='Tekst pogrubiony',state=ACTIVE, variable=self.mvar, command= self.pogrubiona).grid()
		checkL = Checkbutton(check, text='Tekst kursywa',state=ACTIVE, variable=self.nvar, command= self.pochylona).grid()
		checkP = Checkbutton(check, text='Tekst podkreslony',state=ACTIVE, variable=self.ovar, command= self.podkreslony).grid()
		check.grid(row = 1, column = 0)
		label_menu = Label(bottom_frame, text="Ustawienie rozmiaru tekstu")
		label_menu.grid(row=2, column=0)

		sizeList = ['5px','6px','7px','8px','10px','12px','14px','16px','18px','20px','24px','28px','30px']
		self.selectedSize = StringVar()
		self.selectedSize.set(sizeList[3])
		sizeMenu = OptionMenu(bottom_frame, self.selectedSize, *sizeList).grid(row=3, column=0)

		label_menu = Label(bottom_frame, text="Ustawienie koloru tekstu")
		label_menu.grid(row=4, column=0)

		colorList = ['black', 'white', 'red', 'blue', 'green', 'yellow']
		self.selectedColor = StringVar()
		self.selectedColor.set(colorList[0])
		colorMenu = OptionMenu(bottom_frame, self.selectedColor, *colorList).grid(row=5, column=0)

		label_menu = Label(bottom_frame, text="Ustawienie czcionki tekstu")
		label_menu.grid(row=6, column=0)

		familyList = ['Serif', 'Sans-serif', 'Monospace', 'Times New Roman', 'Times']
		self.selectedFamily = StringVar()
		self.selectedFamily.set(familyList[0])
		familyMenu = OptionMenu(bottom_frame, self.selectedFamily, *familyList).grid(row=7, column=0)



		label_menu = Label(bottom_frame, text="Wybierz umieszczenie wnętrza")
		label_menu.grid(row=0, column=1)

		alignList = ['center', 'left', 'right', 'justify', 'initial', 'inherit']
		self.selectedAlign = StringVar()
		self.selectedAlign.set(alignList[1])

		alignMenu = OptionMenu(bottom_frame, self.selectedAlign, *alignList).grid(row=1, column=1)

		label_menu = Label(bottom_frame, text="Ustaw padding strony")
		label_menu.grid(row=2, column=1)

		padding_frame = Frame(bottom_frame, bg = 'red', height = 70, width = 70)
		padding_frame.grid(row=3, column=1)

		Top_PList = ['0px', '1px', '2px', '2.5px', '3px', '3.5px', '4px', '5px', '6px', '7px', '8px', '9px', '10px']
		self.selectedTop_P = StringVar()
		self.selectedTop_P.set(Top_PList[0])

		Right_PList = ['0px', '1px', '2px', '2.5px', '3px', '3.5px', '4px', '5px', '6px', '7px', '8px', '9px', '10px']
		self.selectedRight_P = StringVar()
		self.selectedRight_P.set(Right_PList[0])

		Left_PList = ['0px', '1px', '2px', '2.5px', '3px', '3.5px', '4px', '5px', '6px', '7px', '8px', '9px', '10px']
		self.selectedLeft_P = StringVar()
		self.selectedLeft_P.set(Left_PList[0])

		Bottom_PList = ['0px', '1px', '2px', '2.5px', '3px', '3.5px', '4px', '5px', '6px', '7px', '8px', '9px', '10px']
		self.selectedBottom_P = StringVar()
		self.selectedBottom_P.set(Bottom_PList[0])

		Top_PMenu = OptionMenu(padding_frame, self.selectedTop_P, *Top_PList).pack()
		Right_PMenu = OptionMenu(padding_frame, self.selectedRight_P, *Right_PList).pack(side = RIGHT)
		Left_PMenu = OptionMenu(padding_frame, self.selectedLeft_P, *Left_PList).pack(side = LEFT)
		Bottom_PMenu = OptionMenu(padding_frame,self.selectedBottom_P, *Bottom_PList).pack(side = BOTTOM)


		label_menu = Label(bottom_frame, text="Ustaw tło")
		label_menu.grid(row=0, column=2)

		color_backgroundList = ['white', 'red', 'yellow']
		self.selectedBackground_color = StringVar()
		self.selectedBackground_color.set(color_backgroundList[0])
		Background_color_PMenu = OptionMenu(bottom_frame, self.selectedBackground_color, *color_backgroundList).grid(row=1, column=2)

		#label_menu = Label(bottom_frame, text="Wstaw zdjecie")
		#label_menu.grid(row=0, column=3)

		#browsebutton = Button(bottom_frame, text="Wybierz", command=browsefunc)
		#browsebutton.grid(row=1, column=3)

		bottom_frame.columnconfigure(0, weight=1)
		bottom_frame.columnconfigure(1, weight=1)
		bottom_frame.columnconfigure(2, weight=1)
		#bottom_frame.columnconfigure(3, weight=1)


		'''
		label = Label(self, text="Stworz i dodaj element do swojej strony ")
		#label.grid(row=0, column=0, columnspan=3)
		
		label2 = Label(self, text="Wprowadz tekst")
		T_content = Text(self,height=5, width=50)
		T_content.pack()
		T_id = Text(self,height=1, width=8)
		T_id.pack()
		T_class = Text(self,height=1, width=8)
		T_class.pack()
		T_div_id = Text(self,height=1, width=8)
		T_div_id.pack()

		self.mvar = IntVar()
		self.nvar = IntVar()
		self.ovar = IntVar()
		self.div = Tag('div')
		self.val_B = 0
		self.val_U = 0
		self.val_I = 0

		sizeList = ['5px','6px','7px','8px','10px','12px','14px','16px','18px','20px','24px','28px','30px']
		self.selectedSize = StringVar()
		self.selectedSize.set(sizeList[3])

		colorList = ['black', 'white', 'red', 'blue', 'green', 'yellow']
		self.selectedColor = StringVar()
		self.selectedColor.set(colorList[0])

		familyList = ['Serif', 'Sans-serif', 'Monospace', 'Times New Roman', 'Times']
		self.selectedFamily = StringVar()
		self.selectedFamily.set(familyList[0])

		alignList = ['center', 'left', 'right', 'justify', 'initial', 'inherit']
		self.selectedAlign = StringVar()
		self.selectedAlign.set(alignList[1])

		Top_PList = ['0px', '1px', '2px', '2.5px', '3px', '3.5px', '4px', '5px', '6px', '7px', '8px', '9px', '10px']
		self.selectedTop_P = StringVar()
		self.selectedTop_P.set(Top_PList[0])

		Right_PList = ['0px', '1px', '2px', '2.5px', '3px', '3.5px', '4px', '5px', '6px', '7px', '8px', '9px', '10px']
		self.selectedRight_P = StringVar()
		self.selectedRight_P.set(Right_PList[0])

		Left_PList = ['0px', '1px', '2px', '2.5px', '3px', '3.5px', '4px', '5px', '6px', '7px', '8px', '9px', '10px']
		self.selectedLeft_P = StringVar()
		self.selectedLeft_P.set(Left_PList[0])

		Bottom_PList = ['0px', '1px', '2px', '2.5px', '3px', '3.5px', '4px', '5px', '6px', '7px', '8px', '9px', '10px']
		self.selectedBottom_P = StringVar()
		self.selectedBottom_P.set(Bottom_PList[0])

		color_backgroundList = ['white', 'red', 'yellow']
		self.selectedBackground_color = StringVar()
		self.selectedBackground_color.set(color_backgroundList[0])

		backButton = Button(self, text="Back", command=lambda: controller.show_frame(StartPage)).pack(anchor = CENTER)
		createButton = Button(self, text="Create", command=lambda: self.createDiv(T_content, T_id, T_class, self.val_B, self.val_U, self.val_I, T_div_id)).pack(anchor = CENTER)

		check = Frame(self)
		checkB = Checkbutton(check, text='Tekst pogrubiony',state=ACTIVE, variable=self.mvar, command= self.pogrubiona).grid()
		checkL = Checkbutton(check, text='Tekst kursywa',state=ACTIVE, variable=self.nvar, command= self.pochylona).grid()
		checkP = Checkbutton(check, text='Tekst podkreslony',state=ACTIVE, variable=self.ovar, command= self.podkreslony).grid()
		check.pack()

		sizeMenu = OptionMenu(self, self.selectedSize, *sizeList).pack()
		colorMenu = OptionMenu(self, self.selectedColor, *colorList).pack()
		familyMenu = OptionMenu(self, self.selectedFamily, *familyList).pack()
		alignMenu = OptionMenu(self, self.selectedAlign, *alignList).pack()

		labelp = Label(self, text="Padding")
		labelp.pack(pady=10,padx=10)
		Top_PMenu = OptionMenu(self, self.selectedTop_P, *Top_PList).pack()
		Right_PMenu = OptionMenu(self, self.selectedRight_P, *Right_PList).pack()
		Left_PMenu = OptionMenu(self, self.selectedLeft_P, *Left_PList).pack()
		Bottom_PMenu = OptionMenu(self, self.selectedBottom_P, *Bottom_PList).pack()

		Background_color_PMenu = OptionMenu(self, self.selectedBackground_color, *color_backgroundList).pack()

		'''
	def createDiv(self,T_content, T_id, T_class, val_B, val_U, val_I, T_div_id):
		zag_div = T_div_id.get("1.0",'end-1c')
		value = T_content.get("1.0",'end-1c')
		new_id = T_id.get("1.0",'end-1c')
		new_class = T_class.get("1.0",'end-1c')
		self.div = Tag('div',value, id_tag = new_id, class_tag = new_class)
		self.div.contents = value
		self.div.id = new_id
		self.div.clas = new_class

		if zag_div == '':
			body.add_tag(self.div)
			print("brak zagniezdzenia")
		else:
			for elem in body.elem_content:
				if elem.id == zag_div:
					elem.add_elem(self.div)
				
			

		if self.val_B == 0:
			self.div.add_style('font-weight','normal')
		elif self.val_B == 1:
			self.div.add_style('font-weight','bold')

		if self.val_U == 0:
			self.div.add_style('font-style','normal')
		elif self.val_U == 1:
			self.div.add_style('font-style','italic')

		if self.val_I == 0:
			self.div.add_style('text-decoration','none')
		elif self.val_I == 1:
			self.div.add_style('text-decoration','underline')

		self.div.add_style('font-size', self.selectedSize.get())
		self.div.add_style('color', self.selectedColor.get())
		self.div.add_style('font-family', self.selectedFamily.get())
		self.div.add_style('text-align', self.selectedAlign.get())
		self.div.add_style('padding-top', self.selectedTop_P.get())
		self.div.add_style('padding-right', self.selectedRight_P.get())
		self.div.add_style('padding-left', self.selectedLeft_P.get())
		self.div.add_style('padding-bottom', self.selectedBottom_P.get())
		style.add_elem(self.div)
		print("Wykonano funkcje createDiv")


	def pogrubiona(self):
		self.val_B = self.mvar.get() 

	def pochylona(self):
		self.val_U = self.nvar.get()

	def podkreslony(self):
		self.val_I = self.ovar.get()

		

app = mainGUI()
app.mainloop()
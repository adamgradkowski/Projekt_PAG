from tkinter import * 
from tkinter import filedialog as fd

def browsefunc():
    filename = fd.askopenfilename()
    print(filename)
	


mainWindow = Tk()
mainWindow.title("Hello World")
mainWindow.geometry("640x520+300+100")

conteiner = Frame(mainWindow, bg = 'yellow')
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
backButton = Button(id_frame, text="Back", command='').pack()
createButton = Button(id_frame, text="Create", command='').pack()

label_menu = Label(bottom_frame, text="Ustawienie tekstu")
label_menu.grid(row=0, column=0)

check = Frame(bottom_frame)
checkB = Checkbutton(check, text='Tekst pogrubiony',state=ACTIVE, command= '').grid()
checkL = Checkbutton(check, text='Tekst kursywa',state=ACTIVE, command= '').grid()
checkP = Checkbutton(check, text='Tekst podkreslony',state=ACTIVE, command= '').grid()
check.grid(row = 1, column = 0)
label_menu = Label(bottom_frame, text="Ustawienie rozmiaru tekstu")
label_menu.grid(row=2, column=0)

sizeList = ['5px','6px','7px','8px','10px','12px','14px','16px','18px','20px','24px','28px','30px']
selectedSize = StringVar()
selectedSize.set(sizeList[3])
sizeMenu = OptionMenu(bottom_frame, selectedSize, *sizeList).grid(row=3, column=0)

label_menu = Label(bottom_frame, text="Ustawienie koloru tekstu")
label_menu.grid(row=4, column=0)

colorList = ['black', 'white', 'red', 'blue', 'green', 'yellow']
selectedColor = StringVar()
selectedColor.set(colorList[0])
colorMenu = OptionMenu(bottom_frame, selectedColor, *colorList).grid(row=5, column=0)

label_menu = Label(bottom_frame, text="Ustawienie czcionki tekstu")
label_menu.grid(row=6, column=0)

familyList = ['Serif', 'Sans-serif', 'Monospace', 'Times New Roman', 'Times']
selectedFamily = StringVar()
selectedFamily.set(familyList[0])
familyMenu = OptionMenu(bottom_frame, selectedFamily, *familyList).grid(row=7, column=0)



label_menu = Label(bottom_frame, text="Wybierz umieszczenie wnętrza")
label_menu.grid(row=0, column=1)

alignList = ['center', 'left', 'right', 'justify', 'initial', 'inherit']
selectedAlign = StringVar()
selectedAlign.set(alignList[1])
alignMenu = OptionMenu(bottom_frame, selectedAlign, *alignList).grid(row=1, column=1)

label_menu = Label(bottom_frame, text="Ustaw padding strony")
label_menu.grid(row=2, column=1)

padding_frame = Frame(bottom_frame, bg = 'red', height = 70, width = 70)
padding_frame.grid(row=3, column=1)

Top_PList = ['0px', '1px', '2px', '2.5px', '3px', '3.5px', '4px', '5px', '6px', '7px', '8px', '9px', '10px']
selectedTop_P = StringVar()
selectedTop_P.set(Top_PList[0])

Right_PList = ['0px', '1px', '2px', '2.5px', '3px', '3.5px', '4px', '5px', '6px', '7px', '8px', '9px', '10px']
selectedRight_P = StringVar()
selectedRight_P.set(Right_PList[0])

Left_PList = ['0px', '1px', '2px', '2.5px', '3px', '3.5px', '4px', '5px', '6px', '7px', '8px', '9px', '10px']
selectedLeft_P = StringVar()
selectedLeft_P.set(Left_PList[0])

Bottom_PList = ['0px', '1px', '2px', '2.5px', '3px', '3.5px', '4px', '5px', '6px', '7px', '8px', '9px', '10px']
selectedBottom_P = StringVar()
selectedBottom_P.set(Bottom_PList[0])

Top_PMenu = OptionMenu(padding_frame, selectedTop_P, *Top_PList).pack()
Right_PMenu = OptionMenu(padding_frame, selectedRight_P, *Right_PList).pack(side = RIGHT)
Left_PMenu = OptionMenu(padding_frame, selectedLeft_P, *Left_PList).pack(side = LEFT)
Bottom_PMenu = OptionMenu(padding_frame,selectedBottom_P, *Bottom_PList).pack(side = BOTTOM)


label_menu = Label(bottom_frame, text="Ustaw tło")
label_menu.grid(row=0, column=2)

color_backgroundList = ['white', 'red', 'yellow']
selectedBackground_color = StringVar()
selectedBackground_color.set(color_backgroundList[0])
Background_color_PMenu = OptionMenu(bottom_frame, selectedBackground_color, *color_backgroundList).grid(row=1, column=2)

label_menu = Label(bottom_frame, text="Wstaw zdjecie")
label_menu.grid(row=0, column=3)

browsebutton = Button(bottom_frame, text="Wybierz", command=browsefunc)
browsebutton.grid(row=1, column=3)

bottom_frame.columnconfigure(0, weight=1)
bottom_frame.columnconfigure(1, weight=1)
bottom_frame.columnconfigure(2, weight=1)
bottom_frame.columnconfigure(3, weight=1)


mainWindow.mainloop()

from tkinter import *
'''

    self.myParent = parent 
    self.myParent.geometry("640x400")

    self.myContainer1 = Frame(parent) 
    self.myContainer1.pack(expand=YES, fill=BOTH)


    self.control_frame = Frame(self.myContainer1) 
    self.control_frame.pack(side=LEFT, expand=NO,  padx=10, pady=5, ipadx=5, ipady=5)    
    
    myMessage="Demo"
    Label(self.control_frame, text=myMessage, justify=LEFT).pack(side=TOP, anchor=W)
    
    self.buttons_frame = Frame(self.control_frame)
    self.buttons_frame.pack(side=TOP, expand=NO, fill=Y, ipadx=5, ipady=5)    

    self.demo_frame = Frame(self.myContainer1) 
    self.demo_frame.pack(side=RIGHT, expand=YES, fill=BOTH)        


    self.top_frame = Frame(self.demo_frame) 
    self.top_frame.pack(side=TOP, expand=YES, fill=BOTH)      

    self.bottom_frame = Frame(self.demo_frame,
      borderwidth=5,   relief=RIDGE,
      height=50, 
      bg="cyan",
      )
    self.bottom_frame.pack(side=TOP, fill=X)    


    self.left_frame = Frame(self.top_frame,  
                            background="red",
                          borderwidth=5,   
                          relief=RIDGE,
                          width=50, 
                          ) 
    self.left_frame.pack(side=LEFT, expand=NO, fill=Y)    

    self.right_frame = Frame(self.top_frame, 
                             background="tan",
                           borderwidth=5,   
                           relief=RIDGE,
                           width=250
                          )
    self.right_frame.pack(side=RIGHT, expand=YES, fill=BOTH)   


    button_names = ["A", "B", "C"]  
    side_options = [LEFT, TOP, RIGHT, BOTTOM]  
    fill_options = [X, Y, BOTH, NONE]
    expand_options = [YES, NO]
    anchor_options = [NW, N, NE, E, SE, S, SW, W, CENTER]
    
  
    self.buttonA = Button(self.bottom_frame, text="A")
    self.buttonA.pack()
    self.buttonB = Button(self.left_frame, text="B")
    self.buttonB.pack()
    self.buttonC = Button(self.right_frame, text="C")
    self.buttonC.pack()  
    self.button_with_name = {"A":self.buttonA, "B":self.buttonB, "C":self.buttonC}  

    self.button_names_frame   = Frame(self.buttons_frame, borderwidth=5)
    self.side_options_frame   = Frame(self.buttons_frame, borderwidth=5)
    self.fill_options_frame   = Frame(self.buttons_frame, borderwidth=5)
    self.expand_options_frame = Frame(self.buttons_frame, borderwidth=5)
    self.anchor_options_frame = Frame(self.buttons_frame, borderwidth=5)

    self.button_names_frame.pack(  side=LEFT, expand=YES, fill=Y, anchor=N)
    self.side_options_frame.pack(  side=LEFT, expand=YES, anchor=N)    
    self.fill_options_frame.pack(  side=LEFT, expand=YES, anchor=N)
    self.expand_options_frame.pack(side=LEFT, expand=YES, anchor=N)
    self.anchor_options_frame.pack(side=LEFT, expand=YES, anchor=N)
          
    Label(self.button_names_frame, text="\nButton").pack()
    Label(self.side_options_frame, text="Side\nOption").pack()
    Label(self.fill_options_frame, text="Fill\nOption").pack()
    Label(self.expand_options_frame, text="Expand\nOption").pack()
    Label(self.anchor_options_frame, text="Anchor\nOption").pack()    
    
    for option in button_names:
      button = Radiobutton(self.button_names_frame, text=str(option), indicatoron=1, 
        value=option, command=self.button_refresh, variable=self.button_name)
      button["width"] = button_width
      button.pack(side=TOP)

    for option in side_options:
      button = Radiobutton(self.side_options_frame, text=str(option), indicatoron=0, 
        value=option, command=self.demo_update, variable=self.side_option)
      button["width"] = button_width
      button.pack(side=TOP)
                
    for option in fill_options:
      button = Radiobutton(self.fill_options_frame, text=str(option), indicatoron=0, 
        value=option, command=self.demo_update, variable=self.fill_option)
      button["width"] = button_width
      button.pack(side=TOP)

    for option in expand_options:
      button = Radiobutton(self.expand_options_frame, text=str(option), indicatoron=0, 
        value=option, command=self.demo_update, variable=self.expand_option)
      button["width"] = button_width 
      button.pack(side=TOP)
  
    for option in anchor_options:
      button = Radiobutton(self.anchor_options_frame, text=str(option), indicatoron=0, 
        value=option, command=self.demo_update, variable=self.anchor_option)
      button["width"] = button_width
      button.pack(side=TOP)

    self.cancelButtonFrame = Frame(self.button_names_frame)
    self.cancelButtonFrame.pack(side=BOTTOM, expand=YES, anchor=SW)
    
    self.cancelButton = Button(self.cancelButtonFrame,
      text="Cancel", background="red", 
      width=button_width,   
      padx=button_padx,     
      pady=button_pady      
      )        
    self.cancelButton.pack(side=BOTTOM, anchor=S)
    self.cancelButton.bind("<Button-1>", self.cancelButtonClick)   
    self.cancelButton.bind("<Return>", self.cancelButtonClick) 
    
    self.demo_update()


  def button_refresh(self):
    button = self.button_with_name[self.button_name.get()]
    properties = button.pack_info()
    self.fill_option.set  (  properties["fill"] )
    self.side_option.set  (  properties["side"] )
    self.expand_option.set(  properties["expand"] )
    self.anchor_option.set(  properties["anchor"] )


  def demo_update(self):
    button = self.button_with_name[self.button_name.get()]
    button.pack(fill=self.fill_option.get()
      , side=self.side_option.get()
      , expand=self.expand_option.get()
      , anchor=self.anchor_option.get()
      )
    
  def cancelButtonClick(self, event): 
    self.myParent.destroy()      

root = Tk()
myapp = MyApp(root)
root.mainloop()
'''
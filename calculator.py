from tkinter import *
from tkinter import ttk
import math

def darkTheme(*args):
  styles.configure('mainframe.TFrame', background='black')
  
  style_input_label1.configure('Label1.TLabel', background ='black', foreground='white')
  style_input_label2.configure('Label2.TLabel', background ='black', foreground='white')
  
  number_button_styles.configure('Numbers_buttons.TButton', background='black', foreground='white')
  number_button_styles.map('Numbers_buttons.TButton', background=[('active', '#333333')])
  
  style_delete_buttons.configure('Delete_buttons.TButton', background='#FF8C00', foreground='white')
  style_delete_buttons.map('Delete_buttons.TButton' , background=[('active', '#DAA520')])
  
  remaining_button_styles.configure('Remaining_buttons.TButton', background='#333333', foreground='white')
  remaining_button_styles.map('Remaining_buttons.TButton', background=[('active', 'black')])
  
  dark_button.grid_forget()
  
  style_clear_button =ttk.Style()
  style_clear_button.configure('Clear_button.TButton',font='arial 18', width=3, relief='flat', background="black", foreground='orange')
  style_clear_button.map('Clear_button.TButton', background=[('active', '#333333')], font=[('active', 'arial 19')], width=[('active', '4')])
  
  clear_button.grid(column=0, row=0, columnspan=1, sticky=(E, N))
   
def clearTheme(*args):
  
  styles.configure('mainframe.TFrame', background='white', foreground='black')
  
  style_input_label1.configure('Label1.TLabel', background ='white', foreground='black')
  style_input_label2.configure('Label2.TLabel', background ='white', foreground='black')
  
  number_button_styles.configure('Numbers_buttons.TButton', background='#FFFFFF', foreground='black')
  number_button_styles.map('Numbers_buttons.TButton', background=[('active', '#D3D3D3')])
  
  style_delete_buttons.configure('Delete_buttons.TButton', font="arial 22", width=5, relief="flat", foreground='black' ,background="#008B8B")
  style_delete_buttons.map('Delete_buttons.TButton' ,background=[('active', '#5F9EA0')])
  
  remaining_button_styles.configure('Remaining_buttons.TButton', background='#B0C4DE', foreground='black')
  remaining_button_styles.map('Remaining_buttons.TButton', background=[('active', 'white')])
  
  clear_button.grid_forget()
  
  dark_button.grid(column=0, row=0, columnspan=1, sticky=(E, N))
  
def enterValues(key):
  if key >= '0' and key <= '9' or key == '(' or key == ')' or key == '.':
    input2.set(input2.get() + key)
  
  if key == '*' or key == '/' or key == '+' or key == '-':
    if key == '*':
      input1.set(input2.get() + '*')
    elif key == '/':
      input1.set(input2.get() + '/')
    elif key == '+':
      input1.set(input2.get() + '+')
    elif key == '-':
      input1.set(input2.get() + '-')
      
    input2.set('')            
  
  if key == '=':
    input1.set(input1.get() + input2.get())
    result = eval(input1.get())
    input2.set(result)    

def enterValuesKeyboard (event):
  print(event)
  key = event.char
  if key >= '0' and key <= '9' or key == '(' or key == ')' or key == '.':
    input2.set(input2.get() + key)
  
  if key == '*' or key == '/' or key == '+' or key == '-':
    if key == '*':
      input1.set(input2.get() + '*')
    elif key == '/':
      input1.set(input2.get() + '/')
    elif key == '+':
      input1.set(input2.get() + '+')
    elif key == '-':
      input1.set(input2.get() + '-')
      
    input2.set('')            
  
  if key == '=' or key == '\r':
    input1.set(input1.get() + input2.get())
    result = eval(input1.get())
    input2.set(result)

def squareRoot():
  input1.set('')
  result = math.sqrt(float(input2.get()))
  input2.set(result)

def delete(event):
  start = 0
  final = len(input2.get()) 
  
  input2.set(input2.get()[start:final-1]) 
  
def deleteAll(event):
  input1.set('')
  input2.set('')  
    
root = Tk()
root.title('Calculator')
root.geometry('+500+80') #Indicates the coordinate where it will start / indica la coordenada donde empezara
# Hacemos que la calculadora se adapte / make the calculator adaptable
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# le damos estilos a los widgets / we style the widgets
styles = ttk.Style()
styles.theme_use('clam')
styles.configure('mainframe.TFrame', background='#DBDBDB')

#creamos un frame en el cual van a estar todos los demas widgets / create a frame in which the other widgets will be placed
mainframe = ttk.Frame(root, style="mainframe.TFrame") 
mainframe.grid(column=0, row=0, sticky=(W, N, E, S)) #position
mainframe.columnconfigure(0, weight=1)
mainframe.columnconfigure(1, weight=1)
mainframe.columnconfigure(2, weight=1)
mainframe.columnconfigure(3, weight=1)

mainframe.rowconfigure(0, weight=1)
mainframe.rowconfigure(1, weight=1)
mainframe.rowconfigure(2, weight=1)
mainframe.rowconfigure(3, weight=1)
mainframe.rowconfigure(4, weight=1)
mainframe.rowconfigure(5, weight=1)
mainframe.rowconfigure(6, weight=1)
mainframe.rowconfigure(7, weight=1)
mainframe.rowconfigure(8, weight=1)

style_input_label1 = ttk.Style()
style_input_label1.configure('Label1.TLabel', font="arial 15", anchor="e")

# Labels Styles
input1 = StringVar()
input_label1 = ttk.Label(mainframe, textvariable=input1, style="Label1.TLabel")
input_label1.grid(column=0, row=1, columnspan=4, sticky=(W, N, E, S))

style_input_label2 = ttk.Style()
style_input_label2.configure('Label2.TLabel', font="arial 40", anchor="e")

input2 = StringVar()
input_label2 = ttk.Label(mainframe, textvariable=input2, style="Label2.TLabel")
input_label2.grid(column=0, row=2, columnspan=4, sticky=(W, N, E, S))

# Estilos para los botones / Styles for buttons
number_button_styles = ttk.Style()
number_button_styles.configure('Numbers_buttons.TButton', font="arial 22", width=5, background="#FFFFFF", relief= "flat")
number_button_styles.map('Numbers_buttons.TButton', background=[('active', '#ADD8E6')])

style_delete_buttons = ttk.Style()
style_delete_buttons.configure('Delete_buttons.TButton', font="arial 22", width=5, relief="flat", background="#008B8B")
style_delete_buttons.map('Delete_buttons.TButton', background=[('active', '#5F9EA0')])

remaining_button_styles = ttk.Style()
remaining_button_styles.configure('Remaining_buttons.TButton', font="arial 22", width=5, relief="flat", background="#CECECE")
remaining_button_styles.map('Remaining_buttons.TButton', background=[('active', '#858585')])

style_dark_button = ttk.Style()
style_dark_button.configure('Dark_button.TButton', font='arial 18', width=3, relief='flat', background='white', foreground='gray')
style_dark_button.map('Dark_button.TButton', background=[('active', 'white')], font=[('active', 'arial 19')], width=[('active', '4')]) 

# Creacion de botones / Button creation
button0 = ttk.Button(mainframe, text='0', style="Numbers_buttons.TButton", command=lambda: enterValues('0'))
button1 = ttk.Button(mainframe, text='1', style="Numbers_buttons.TButton", command=lambda: enterValues('1'))
button2 = ttk.Button(mainframe, text='2', style="Numbers_buttons.TButton", command=lambda: enterValues('2'))
button3 = ttk.Button(mainframe, text='3', style="Numbers_buttons.TButton", command=lambda: enterValues('3'))
button4 = ttk.Button(mainframe, text='4', style="Numbers_buttons.TButton", command=lambda: enterValues('4'))
button5 = ttk.Button(mainframe, text='5', style="Numbers_buttons.TButton", command=lambda: enterValues('5'))
button6 = ttk.Button(mainframe, text='6', style="Numbers_buttons.TButton", command=lambda: enterValues('6'))
button7 = ttk.Button(mainframe, text='7', style="Numbers_buttons.TButton", command=lambda: enterValues('7'))
button8 = ttk.Button(mainframe, text='8', style="Numbers_buttons.TButton", command=lambda: enterValues('8'))
button9 = ttk.Button(mainframe, text='9', style="Numbers_buttons.TButton", command=lambda: enterValues('9'))

delete_button = ttk.Button(mainframe, text=chr(9003), style="Delete_buttons.TButton", command=lambda: delete(chr(9003)))
delete_all_button = ttk.Button(mainframe, text='C', style="Delete_buttons.TButton", command=lambda: deleteAll('C'))
parenthesis_button1 = ttk.Button(mainframe, text='(', style="Remaining_buttons.TButton", command=lambda: enterValues('('))
parenthesis_button2 = ttk.Button(mainframe, text=')', style="Remaining_buttons.TButton", command=lambda: enterValues(')'))
point_button = ttk.Button(mainframe, text='.', style="Remaining_buttons.TButton", command=lambda: enterValues('.'))

division_button = ttk.Button(mainframe, text=chr(247), style="Remaining_buttons.TButton", command=lambda: enterValues('/'))
multiplication_button = ttk.Button(mainframe, text='x', style="Remaining_buttons.TButton", command=lambda: enterValues('*'))
substract_button = ttk.Button(mainframe, text='-', style="Remaining_buttons.TButton", command=lambda: enterValues('-'))
sum_button = ttk.Button(mainframe, text='+', style="Remaining_buttons.TButton", command=lambda: enterValues('+'))

same_button = ttk.Button(mainframe, text='=', style="Remaining_buttons.TButton", command=lambda: enterValues('='))
square_root_button = ttk.Button(mainframe, text='√', style="Remaining_buttons.TButton", command=lambda: squareRoot('√'))

dark_button = ttk.Button(mainframe, text="🌙", style='Dark_button.TButton', command=lambda: darkTheme('🌙'))
clear_button = ttk.Button(mainframe, text='🌞', style='Clear_button.TButton', command=lambda: clearTheme('🌞'))

# Colocar botones en pantalla / placing buttons on the screen
parenthesis_button1.grid(column=0, row=3, sticky=(W, N, E, S))
parenthesis_button2.grid(column=1, row=3, sticky=(W, N, E, S))
delete_all_button.grid(column=2, row=3, sticky=(W, N, E, S))
delete_button.grid(column=3, row=3, sticky=(W, N, E, S))

button7.grid(column=0,row=4, sticky=(W, N, E, S))
button8.grid(column=1,row=4, sticky=(W, N, E, S))
button9.grid(column=2,row=4, sticky=(W, N, E, S))
division_button.grid(column=3, row=4, sticky=(W, N, E, S))

button4.grid(column=0, row=5, sticky=(W, N, E, S))
button5.grid(column=1, row=5, sticky=(W, N, E, S))
button6.grid(column=2, row=5, sticky=(W, N, E, S))
multiplication_button.grid(column=3, row=5, sticky=(W, N, E, S))

button1.grid(column=0, row=6, sticky=(W, N, E, S))
button2.grid(column=1, row=6, sticky=(W, N, E, S))
button3.grid(column=2, row=6, sticky=(W, N, E, S))
sum_button.grid(column=3, row=6, sticky=(W, N, E, S))

button0.grid(column=0, row=7, columnspan=2, sticky=(W, E))
point_button.grid(column=2, row=7, sticky=(W, N, E, S))
substract_button.grid(column=3, row=7, sticky=(W, N, E, S))

same_button.grid(column=0, row=8, columnspan=3, sticky=(W, N, E, S))
square_root_button.grid(column=3, row=8, sticky=(W, N, E, S))

dark_button.grid(column=0, row=0, columnspan=1, sticky=(E, N))

for child in mainframe.winfo_children():
  child.grid_configure(ipady=10, padx=1, pady=1)

root.bind('<KeyPress-d>', darkTheme)  
root.bind('<KeyPress-c>', clearTheme)
root.bind('<Key>', enterValuesKeyboard)
root.bind('<KeyPress-BackSpace>', delete)
root.bind('<KeyPress-a>', deleteAll)
root.mainloop()
import tkinter as tk
import math
window =tk.Tk()
window.title('Calculator')
window.geometry('500x650')
window.resizable(False, False)
window.configure(bg = 'black')
#do buttons
buttons = ['C','<-', '+', '=','1','2','3',
           '/','4','5','6','*','7','8','9',
           'cos','0','sin','tan','ctg',
           'Bin','log','ln','%']
x = 18
y = 140
for button in buttons:
    get_lbl = lambda x=button: calculate(x)
    tk.Button(text= button, bg = 'white', font=('black', 20), command = get_lbl).place(x =x , y=y, width = 115, height = 79)
    x += 117
    if x > 400:
        x = 18
        y += 81
#create function for buttons
def calculate(operation):

    global mathform

    if operation == 'C':
        mathform = '0'
    elif operation == '<-':
        mathform = mathform[0:-1]
    elif operation == '=':
        mathform = str(eval(mathform))
    elif operation == 'sin':
        mathform = str(math.sin(float(mathform)))
    elif operation == 'cos':
        mathform = str(math.cos(float(mathform)))
    elif operation == 'tg':
        mathform = str(math.tan(float(mathform)))
    elif operation == 'ctg':
        mathform = str(math.cos(float(mathform))/math.sin(float(mathform)))
    elif operation == 'log':
        mathform = str(math.log10(float(mathform)))
    elif operation == 'ln':
        mathform = str(math.log(float(mathform)))
    elif operation == 'Bin':
        mathform = str(bin(int(mathform)))
    else:
        if mathform == '0':
            mathform = ''
        mathform += operation
    label_text.configure(text=mathform)

mathform = '0'
label_text = tk.Label(text= mathform, font = ('black',30, 'bold'), bg = 'black',fg = 'white')
label_text.place(x = 11, y = 50)

window.mainloop()
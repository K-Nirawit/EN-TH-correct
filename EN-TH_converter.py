import tkinter as tk
from tkinter import ttk


win = tk.Tk()
win.title('EN-TH-EN converter')
win.geometry('500x800')
win.configure(bg='gray')
font = ('apple symbol',30, 'bold')

La1 = tk.Label(win, text = 'EN-TH-EN converter',font=font,fg='blue',bg = 'white')
La1.place(x=100,y=30)


#function
def EtoT():
    La3.config(text= 'your selection is : EN to TH')
    ETval = 1 # english to Thai
    return ETval

def TtoE():
    La3.config(text= 'your selection is : TH to EN')
    ETval = 0 # Thai to English
    return ETval

def runtraslate(msg,ETval):
    pass
#mode select
La2 = tk.Label(win, text = 'select mode')
La2.place(x=150,y=100)
B1 = ttk.Button(win, text= 'EN to TH', command = EtoT)
B1.place(x=100,y=130)

B2 = ttk.Button(win,text = 'TH to EN', command= TtoE)
B2.place(x=200,y=130)

La3 = tk.Label(win,text = 'your selection is : _________')
La3.place(x=150,y=160)

#1 entry + 1 output
font2 = ('apple symbol',20)
En1 = tk.Entry(win,width=10, font=font2, bg = 'white')
En1.place(x=100,y=200)
msg = En1.get()
out1 = tk.Label(win, width= 20, text = '            ', bg ='white')
out1.place(x=100,y=250)

#command to run
run = ttk.Button(win,text='RUN',command = runtraslate(msg,ETval))
run.place(x=250, y= 200)




win.mainloop()
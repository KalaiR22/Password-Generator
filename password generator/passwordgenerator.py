from tkinter import *   
import string
import random
import pyperclip

window = Tk()

def generate():
    
    small_letter= string.ascii_lowercase
    caps_letter=string.ascii_uppercase
    num = string.digits
    special_character=string.punctuation
    all=small_letter+caps_letter+num+special_character
    pw_lenght=int(password_lenght.get())
    if choice.get()==1:
        password_output.insert(0, random.sample(small_letter,pw_lenght))
    elif choice.get()==2:
        password_output.insert(0, random.sample(small_letter+caps_letter,pw_lenght))
    elif choice.get()==3:
        password_output.insert(0, random.sample(all,pw_lenght))

def copy():
    password_cp = password_output.get()
    pyperclip.copy(password_cp)

window.title('password generator')
window.geometry('400x400')
window.config(bg='#191717')
window.resizable(False,False)
choice = IntVar()
title_topic = Label(window,text='PASSWORD GENERATOR', font=('arial', 20, 'bold'), fg='white', bg='#191717',)
title_topic.place(x=25,y=20)
Radiobutton(window, text = 'Weak', font=('arial', 13, 'bold'),value=1, variable=choice,width=6 ).place(x=155,y=70)
Radiobutton(window, text = 'Medium', font=('arial', 13, 'bold'),value=2, variable=choice, width=6 ).place(x=155,y=100)
Radiobutton(window, text = 'Strong', font=('arial', 13, 'bold'),value=3, variable=choice,width=6   ).place(x=155,y=130)

Label(window, text='Password Lenght:', font=('arial', 13, 'bold'),fg='white', bg='#191717').place(x=55,y=180)
password_lenght=Spinbox(window, from_=5, to=18,font=('arial', 13, 'bold'),width=10)
password_lenght.place(x=220, y=180)
Button(window, text='Generate',font=('arial', 13, 'bold'), bg='#96B6C5',pady=5, padx=3, command=generate).place(x=160,y=230)

password_output=Entry(window,text='',font=('arial', 13, 'bold'))
password_output.place(x=65,y=308)
copy_btn=Button(window, text='Copy',font=('arial', 13, 'bold'), bg='#96B6C5',pady=5, padx=3,command=copy)
copy_btn.place(x=265,y=300)
window.mainloop()
import tkinter as tk
from tkinter import Tk

root = tk.Tk()

root.geometry("400x600+500+50")
root.title("AGIO Login")
root.configure(bg = 'black')

from tkinter import Label
Titulo = Label(root, text = "AGIO", bg = 'black', fg = 'white', font = ("HoloLens", 20, 'bold'), bd = 0, highlightthickness = 0)
Titulo.pack(pady = (50,10))

user_var = tk.StringVar()
senha_var = tk.StringVar()


def submit():
    
    user = user_entrada.get()
    senha = senha_entrada.get()
    
    print("Username: " + user)
    print("Password: " + senha)
    
    user_var.set("")
    senha_var.set("")
    
    user_entrada.delete(0, tk.END)
    senha_entrada.delete(0, tk.END)


from tkinter import Entry
U = Label(root, text = "Username", pady = 10, font = ("Arial", 12), bg = 'black', fg = 'white', height = 1, width = 8)
U.pack()
user_entrada = Entry(root, width = 30, bg = 'black', fg = 'white', highlightthickness = 1)
user_entrada.pack(pady = 10)
    
S = Label(root, text = "Password", pady = 10, font = ("Arial", 12), bg = 'black', fg = 'white', height = 1, width = 8)
S.pack()
senha_entrada = Entry(root, width = 30, show = "*", bg = 'black', fg = 'white', highlightthickness = 1)
senha_entrada.pack(pady = 20)

sub_titulo = Label(root, text = "Don’t have an account yet? Sign in", bg = 'black', fg = 'light gray', font = ("HoloLens", 10), bd = 0, highlightthickness = 0)
sub_titulo.pack(pady = 20)

from tkinter import Button
sub_btn = tk.Button(root, text = 'LOGIN', command = submit, bg = 'black', fg = 'white', font = ("HoloLens", 16, 'bold'), highlightthickness = 1)
sub_btn.pack(pady = 10)

bottom_text = Label(root, text = "2025 AGIO from SLAS", bg = 'black', fg = 'light gray', font = ("HoloLens", 10), bd = 0, highlightthickness = 0)
bottom_text.pack(side = "bottom", pady = 20)

root.mainloop()
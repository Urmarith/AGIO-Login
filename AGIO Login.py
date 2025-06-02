import tkinter as tk
from tkinter import Tk

root = tk.Tk()

root.geometry("400x600+500+50")
root.title("AGIO Login")
root.configure(bg = 'black')

from tkinter import Label
titulo = Label(root, text = "AGIO", bg = 'black', fg = 'white', font = ("HoloLens", 20, 'bold'), bd = 0, highlightthickness = 0)
titulo.pack(pady = (50,10))

user_var = tk.StringVar()
senha_var = tk.StringVar()


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


def abrir_loading():
    titulo.pack_forget()
    U.pack_forget()
    user_entrada.pack_forget()
    S.pack_forget()
    senha_entrada.pack_forget()
    sub_titulo.pack_forget()
    sub_btn.pack_forget()
    bottom_text.pack_forget()
    
    loading_frame.pack(expand = True)
    animate_loading()
    
    root.after(5000, carregar_concluido)

def carregar_concluido():
    loading_frame.pack_forget()
    Label(root, text = "Login Successfull", font = ("HoloLens", 14), fg = 'white', bg = 'black').pack(pady = 200)
    
def submit():
    
    user = user_entrada.get()
    senha = senha_entrada.get()
    
    print("Username: " + user)
    print("Password: " + senha)
    
    user_var.set("")
    senha_var.set("")
    
    user_entrada.delete(0, tk.END)
    senha_entrada.delete(0, tk.END)
    
    abrir_loading()


from tkinter import Button
sub_btn = tk.Button(root, text = 'LOGIN', command = submit, bg = 'black', fg = 'white', font = ("HoloLens", 16, 'bold'), highlightthickness = 1)
sub_btn.pack(pady = 10)

bottom_text = Label(root, text = "2025 AGIO from SLAS", bg = 'black', fg = 'light gray', font = ("HoloLens", 10), bd = 0, highlightthickness = 0)
bottom_text.pack(side = "bottom", pady = 20)

loading_frame = tk.Frame(root, bg = 'black')
canvas = tk.Canvas(loading_frame, width = 300, height = 150, bg = 'black', highlightthickness = 0)
canvas.pack(pady = 60, padx = 70)

dots = []
spacing = 60
for i in range(3):
    dot = canvas.create_oval(60 + i * spacing, 75, 80 + i * spacing, 95, fill = 'white')
    dots.append(dot)
    
current_frame = [0]

def animate_loading():
    for i in range(3):
        offset = -15 if i == current_frame[0] else 0
        canvas.coords(dots[i],
                      60 + i * 60, 75 + offset,
                      80 + i * 60, 95 + offset)
            
    current_frame[0] = (current_frame[0] + 1) % 3
    root.after(200, animate_loading)
        
root.mainloop()

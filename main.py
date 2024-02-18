from tkinter import *
import tkinter as tk
import subprocess
import ttkbootstrap as tb
from tkinter import IntVar
from PIL import Image, ImageTk
from tkinter import messagebox,simpledialog
def auth(file):
    pswd =  "admin123"
    admin_password = simpledialog.askstring("Enter Password","Enter admin password", show='*')
    if admin_password == pswd:
        root.destroy()
        subprocess.run(["python", file])
    else:
        messagebox.showwarning("Invalid Password", "Incorrect admin password.")

def move1():
    # root.destroy()
    # subprocess.run(["python", "candidate_reg.py"])
    auth("candidate_reg.py")

def move2():
    root.destroy()
    subprocess.run(["python", "log.py"])

def move3():
    # root.destroy()
    # subprocess.run(["python", "results.py"])
    auth("results.py")

root = tb.Window(themename="litera", iconphoto=None)
root.configure(bg="#f5f5f5")
root.attributes('-fullscreen', True)
root.title("Log In ")

registration_label = tb.Label(root, text="Select the option", font=("Roboto", 40, "bold"))
registration_label.pack(pady=(50, 0))
registration_label.configure(style="Primary.TLabel")

my_frame = LabelFrame(root, font=("Roboto", 16, "bold"), background="#00FFFF", padx=100, pady=100)
my_frame.place(relx=0.5, rely=0.5, anchor='center')

my_style = tb.Style()
my_style.configure('success.Outline.TButton', font=("Helvetica", 25))
my_button1 = tb.Button(my_frame, text="Candidate Registration", bootstyle="success", style="success.Outline.TButton", width=30, command=move1)
my_button1.pack(pady=(20, 0), padx=20)

my_button2 = tb.Button(my_frame, text="Voting Interface", bootstyle="success", style="success.Outline.TButton", width=30, command=move2)
my_button2.pack(pady=(60, 0), padx=20)

my_button3 = tb.Button(my_frame, text="Results", bootstyle="success", style="success.Outline.TButton", width=30, command=move3)
my_button3.pack(pady=(60, 0), padx=20)

original_image = Image.open("./emblem.png")
resized_image = original_image.resize((90, 90))
logo_image = ImageTk.PhotoImage(resized_image)

logo_label = tb.Label(root, image=logo_image, anchor='s')
logo_label.place(relx=0.5, rely=1.0, anchor='s', y=-30)

root.option_add("*Font", "Roboto")
root.option_add("*Entry.highlightcolor", "#54a0ff")

root.mainloop()

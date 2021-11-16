#Importando Bibliotecas
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

#=====Criar Nossa Janela
jan = Tk()
jan.title("Code System")
jan.geometry("600x300")
jan.configure(background="black")
jan.resizable(width=False, height=False)
jan.attributes("-alpha", 0.9)
jan.iconbitmap(default="icons/LogoIcon.ico")

#======== Carregando Imagens 
logo = PhotoImage(file="icons/logo.png")


#======= Widgets =========
LeftFrame = Frame(jan,width=200, height=300, bg="MIDNIGHTBLUE",relief="raise")
LeftFrame.pack(side=LEFT)

RightFrame =Frame(jan,width=395, height=300, bg="MIDNIGHTBLUE",relief="raise")
RightFrame.pack(side=RIGHT)

LogoLabel = Label(LeftFrame, image=logo, bg="MIDNIGHTBLUE")
LogoLabel.place(x=50,y=100)


UserLabel = Label(RightFrame, text="Username:", font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="white")
UserLabel.place(x=5,y=100)

UserEntry = ttk.Entry(RightFrame,width=30)
UserEntry.place(x=150,y=110)

PassLabel= Label(RightFrame, text="Password:", font=("Century Gothic",20), bg="MIDNIGHTBLUE", fg="white")
PassLabel.place(x=5,y=150)

PassEntry =ttk.Entry(RightFrame,width=30, show="*")
PassEntry.place(x=150,y=160)


#Botoes
LoginButton = ttk.Button(RightFrame,text="Login",width=20,)
LoginButton.place(x=105,y=210)

RegisterButton = ttk.Button(RightFrame,text="Register",width=20)
RegisterButton.place(x=105,y=240)

jan.mainloop()
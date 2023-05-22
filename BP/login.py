from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image


def fun_login():
    global login
    login = Tk()
    login.title("Ingresar al Sistema")
    login.resizable(0,0)
    login.geometry("500x200") #ancho, alto
    login.configure()
    
    img_login = Image.open("Imágenes/logoxd.png")
    
    login.configure(bg='black')
    
    resized = img_login.resize((300,200))
    img_login = ImageTk.PhotoImage(resized)
    
    label_imagen = Label(login, image = img_login, bg='black')
    label_imagen.pack()
    label_imagen.place(x=10, y=1)
    
    
    
    
    lbl_usuario = Label(login, text= "Usuario", bg='black', fg='white')
    lbl_usuario.pack()
    lbl_usuario.place(x=250, y=30)
    
    lbl_usuario = Label(login, text= "Contraseña", bg='black', fg='white')
    lbl_usuario.pack()
    lbl_usuario.place(x=250, y=60)
    
    usuario_1=  StringVar()
    entry_usuario = Entry(login, textvariable= usuario_1)
    entry_usuario.pack
    entry_usuario.place(x=325, y=30)
    
    contraseña_1=  StringVar()
    entry_contraseña = Entry(login, textvariable= contraseña_1)
    entry_contraseña.pack
    entry_contraseña.place(x=325, y=60)
    
    
    btn_entrar= Button(login, text= "      ENTRAR      ", bg='blue',bd=0, command = ir_l_f)
    btn_entrar.pack()
    btn_entrar.place(x=300,y=153)
    
    btn_salir= Button(login, text= "       VOLVER       ", bg='#800080',bd=0, command = ir_l_m)
    btn_salir.pack()
    btn_salir.place(x=10,y=10)
    
    btn_salir= Button(login, text= "       SALIR       ", bg='green',bd=0, command = ir_l_e)
    btn_salir.pack()
    btn_salir.place(x=400,y=153)
    
    
    mainloop()
    

def ir_l_m():
    login.destroy()
    import menu

def ir_l_e():
    login.destroy()
    

def ir_l_f():
    login.destroy()
    import categorias 

fun_login()

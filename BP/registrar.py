from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import tkinter as tk
import re
import sqlite3


conn = sqlite3.connect('registros.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS registros
             (ID INTEGER PRIMARY KEY AUTOINCREMENT,
             NOMBRE TEXT NOT NULL,
             EMAIL TEXT NOT NULL,
             CONTRASENA TEXT NOT NULL);''')



def fun_registrar():
    global registrar
    registrar = Tk()
    registrar.title("Ingresar al Sistema")
    registrar.resizable(0,0)
    registrar.geometry("500x350") #ancho, alto
    registrar.configure()
    
    img_registrar = Image.open("Imágenes/logoxd.png")
    
    registrar.configure(bg='black')
    
    resized = img_registrar.resize((250,150))
    img_registrar = ImageTk.PhotoImage(resized)
    
    label_imagen = Label(registrar, image = img_registrar, bg='black')
    label_imagen.pack()
    label_imagen.place(x=100, y=1)
    
    
    
    
    lbl_CE = Label(registrar, text= "Correo Electronico", bg='black', fg='white')
    lbl_CE.pack()
    lbl_CE.place(x=100, y=180)
    
    lbl_N = Label(registrar, text= "Nombre", bg='black', fg='white')
    lbl_N.pack()
    lbl_N.place(x=100, y=210)
    
    lbl_U = Label(registrar, text= "Usuario", bg='black', fg='white')
    lbl_U.pack()
    lbl_U.place(x=100, y=240)
    
    lbl_C = Label(registrar, text= "Contraseña", bg='black', fg='white')
    lbl_C.pack()
    lbl_C.place(x=100, y=270)
    
    CE_1=  StringVar()
    entry_CE = Entry(registrar, textvariable= CE_1)
    entry_CE.pack
    entry_CE.place(x=225, y=180)
    
    N_1=  StringVar()
    entry_N = Entry(registrar, textvariable= N_1)
    entry_N.pack
    entry_N.place(x=225, y=210)
    
    U_1=  StringVar()
    entry_U = Entry(registrar, textvariable= U_1)
    entry_U.pack
    entry_U.place(x=225, y=240)
    
    C_1=  StringVar()
    entry_C = Entry(registrar, textvariable= C_1, show="*")
    entry_C.pack
    entry_C.place(x=225, y=270)
    
    def verificar_contrasena():
        contrasena = C_1.get()
        if len(contrasena) < 8:
            messagebox.showwarning("Contraseña inválida", "La contraseña debe tener al menos 8 caracteres.")
        elif not any(char.isdigit() for char in contrasena):
            messagebox.showwarning("Contraseña inválida", "La contraseña debe contener al menos un número.")
        elif not any(char.isupper() for char in contrasena):
            messagebox.showwarning("Contraseña inválida", "La contraseña debe contener al menos una letra mayúscula.")
        elif not any(char.islower() for char in contrasena):
            messagebox.showwarning("Contraseña inválida", "La contraseña debe contener al menos una letra minúscula.")
        else:
            messagebox.showinfo("Contraseña válida", "Sus datos son correctos, puede volver para iniciar sesion")
        correo = CE_1.get()
        if CE_1.get() =="":
            messagebox.showinfo("Falta dato","Ingrese su correo electronico")
            entry_CE.focus()
            return
        if len(correo) < 8:
            messagebox.showwarning("datos inválidos", "el correo electronico debe tener al menos mas caracteres.")
            
        if not re.search(r"@gmail.com", correo):
            messagebox.showwarning("Error en la información", "La dirección de correo electrónico debe ser de Gmail")
            return
            
        usuario = U_1.get()
        if U_1.get() =="":
            messagebox.showinfo("Falta dato","Ingrese su usuario")
            entry_U.focus()
            return
        elif not usuario.isalpha():
            messagebox.showwarning("Error en la información", "El nombre de usuario debe contener solo letras")
            entry_U.focus()
            return
            
        nombre = N_1.get()
        if N_1.get() =="":
            messagebox.showinfo("Falta dato","Ingrese su usuario")
            entry_N.focus()
            return
            
        if nombre == "":
            messagebox.showwarning("Falta dato", "Ingrese su nombre")
            entry_N.focus()
            return
        if re.search(r"\d", nombre):
            messagebox.showwarning("Error en la información", "El nombre no puede contener números")
            entry_N.focus()
            return
            
    # Insertar registro en la base de datos
        cursor.execute("INSERT INTO registros (NOMBRE, EMAIL, CONTRASENA) VALUES (?, ?, ?)",
                       (nombre, correo, contrasena))
        conn.commit()
        messagebox.showinfo("Registro exitoso", "Se ha registrado correctamente en la base de datos.")

        # Limpiar las entradas de texto
        CE_1.set("")
        N_1.set("")
        U_1.set("")
        C_1.set("")

                        
    btn_entrar= Button(registrar, text= "      VERIFICAR DATOS      ", bg='#1E90FF',bd=0, command = verificar_contrasena)
    btn_entrar.pack()
    btn_entrar.place(x=215,y=320)
    
    btn_salir= Button(registrar, text= "       VOLVER       ", bg='#800080',bd=0, command = ir_l_d)
    btn_salir.pack()
    btn_salir.place(x=10,y=10)
    
    btn_salir= Button(registrar, text= "       SALIR       ", bg='#09E509',bd=0, command = ir_l_m)
    btn_salir.pack()
    btn_salir.place(x=400,y=10)
    
    
    
    
    mainloop()
    

def ir_l_m():
    registrar.destroy()
    
    
def ir_l_f():
    registrar.destroy()
    import menuBP
    
def ir_l_d():
	registrar.destroy()
	import menuBP
	

fun_registrar()

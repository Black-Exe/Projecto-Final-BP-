from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import tkinter as tk
from PIL import Image, ImageTk


def fun_menu():
    global menu
    menu = Tk()
    menu.title("Bienvenidos")
    menu.resizable(0,0)
    #menu.geometry("1400x700") #ancho, alto
    menu.configure()
    menu.iconbitmap("Imágenes/LogoProA.ico")
    menu.attributes('-fullscreen', True)
    
    img_net = Image.open("Imágenes/logoxd.png")
   
    resized = img_net.resize((700,700))
    img_net = ImageTk.PhotoImage(resized)
   
    label_imagen = Label(menu, image = img_net, bg='black')
    label_imagen.pack()
    label_imagen.place(x=10, y=10)
   
   
    menu.configure(bg='black')

    
    
    
    
    lbl_b = Label(menu, text= "𝑩𝑰𝑬𝑵𝑽𝑬𝑵𝑰𝑫𝑶𝑺", fg='white', bg='black')
    lbl_b.config(font=("Black Italic", 50))
    lbl_b.pack()
    lbl_b.place(x=700, y=12)
    
    btn_iniciar_sesion= Button(menu, text= "      INICIAR SESION      ", bg='blue', command = ir_m_l, width=13, height=2,bd=0, font=("Helvetica", 14, "bold"))
    btn_iniciar_sesion.pack()
    btn_iniciar_sesion.place(x=1000,y=350)
     
    btn_salir= Button(menu, text= "       SALIR       ", bg='#800080',bd=0, command = ir_l_e)
    btn_salir.pack()
    btn_salir.place(x=10,y=10)
    
    btn_iniciar_sesion= Button(menu, text= "      REGISTRAR      ", bg='green', command = ir_l_m,width=10, height=2, bd=0,  font=("Helvetica", 14, "bold"))
    btn_iniciar_sesion.pack()
    btn_iniciar_sesion.place(x=750,y=350)
    
    
    
    mainloop()

def ir_m_l():
    menu.destroy()
    import login
    
def ir_l_e():
    menu.destroy()
     
    
def ir_l_m():
    menu.destroy()
    import registrar 

fun_menu()

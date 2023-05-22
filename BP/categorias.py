from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import tkinter as tk
from PIL import Image, ImageTk


def fun_menu():
    global menu
    menu = Tk()
    menu.title("Seleccione la categoria")
    menu.resizable(0,0)
    menu.geometry("1400x700") #ancho, alto
    menu.configure()
    menu.iconbitmap("Imágenes/LogoProA.ico")
    menu.attributes('-fullscreen', True)
    
    img_net = Image.open("Imágenes/amd.png")
    img_net = img_net.resize((300, 300))  # Ajustar el tamaño de la imagen
    img_net = ImageTk.PhotoImage(img_net)
    
    img_int = Image.open("Imágenes/intel--600.png")
    img_int = img_int.resize((300, 300))  # Ajustar el tamaño de la imagen
    img_int = ImageTk.PhotoImage(img_int)
    
    imagen = Image.open("Imágenes/fondod.png")
    imagen = imagen.resize((menu.winfo_screenwidth(), menu.winfo_screenheight()))  # Ajustar el tamaño de la imagen al tamaño de la pantalla
    imagen = ImageTk.PhotoImage(imagen)

# Crear un label con la imagen
    fondo = Label(menu, image=imagen)
    fondo.place(x=0, y=0, relwidth=1, relheight=1)

# Establecer la opacidad de la ventana a 0.5
    menu.wm_attributes("-alpha", 1)
   
    
   
   
    menu.configure(bg='black')

    
    
    
    
    #lbl_b = Label(menu, text= "𝑩𝑰𝑬𝑵𝑽𝑬𝑵𝑰𝑫𝑶𝑺",fg='white')
    #lbl_b.config(font=("Black Italic", 50), bg='#%02x%02x%02x' % (0, 0, 0))
    #lbl_b.pack()
    #lbl_b.place(x=400, y=12)
    
    btn_iniciar_sesion= Button(menu, image= img_net, bg='red', command = ir_m_l, width=290, height=290,bd=0, font=("Helvetica", 14, "bold"))
    btn_iniciar_sesion.pack()
    btn_iniciar_sesion.place(x=300,y=250)
    
    btn_salir= Button(menu, text= "       SALIR       ", bg='#800080',bd=0, command = ir_l_e)
    btn_salir.pack()
    btn_salir.place(x=10,y=10)
    
    btn_iniciar_sesion= Button(menu, image= img_int , bg='blue', command = ir_l_m,width=290, height=290,bd=0, font=("Helvetica", 14, "bold"))
    btn_iniciar_sesion.pack()
    btn_iniciar_sesion.place(x=800,y=250)
    
    
    
    mainloop()

def ir_m_l():
    menu.destroy()
    import amd_1
    
def ir_l_e():
    menu.destroy()
     
    
def ir_l_m():
    menu.destroy()
    import registrar 

fun_menu()





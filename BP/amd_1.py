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
    
    img_net = Image.open("Imágenes/amd34100.png")
    img_net = img_net.resize((300, 300))  # Ajustar el tamaño de la imagen
    img_net = ImageTk.PhotoImage(img_net)
    
    img_int = Image.open("Imágenes/amd53600.png")
    img_int = img_int.resize((300, 300))  # Ajustar el tamaño de la imagen
    img_int = ImageTk.PhotoImage(img_int)
    
    img_inte = Image.open("Imágenes/ryzen758000x.png")
    img_inte = img_inte.resize((700, 300))  # Ajustar el tamaño de la imagen
    img_inte = ImageTk.PhotoImage(img_inte)
    
    imagen = Image.open("Imágenes/fondod.png")
    imagen = imagen.resize((menu.winfo_screenwidth(), menu.winfo_screenheight()))  # Ajustar el tamaño de la imagen al tamaño de la pantalla
    imagen = ImageTk.PhotoImage(imagen)

# Crear un label con la imagen
    fondo = Label(menu, image=imagen)
    fondo.place(x=0, y=0, relwidth=1, relheight=1)

# Establecer la opacidad de la ventana a 0.5
    menu.wm_attributes("-alpha", 1)
   
    
   
   
    menu.configure(bg='black')

    
    
        
    
    
    
    btn_entrar= Button(menu, text= "      INFORMACION ↓↓↓↓      ", bg='#1E90FF',bd=0, command = mostrar_mensaje1)
    btn_entrar.pack()
    btn_entrar.place(x=270,y=220)
    
    btn_entrar= Button(menu, text= "      INFORMACION ↓↓↓↓      ", bg='#1E90FF',bd=0, command = mostrar_mensaje2)
    btn_entrar.pack()
    btn_entrar.place(x=620,y=220)
    
    btn_entrar= Button(menu, text= "      INFORMACION ↓↓↓↓      ", bg='#1E90FF',bd=0, command = mostrar_mensaje3)
    btn_entrar.pack()
    btn_entrar.place(x=970,y=220)
    
    btn_iniciar_sesion= Button(menu, image= img_net, bg='red', command = ir_m_l, width=290, height=290,bd=0, font=("Helvetica", 14, "bold"))
    btn_iniciar_sesion.pack()
    btn_iniciar_sesion.place(x=200,y=250)
    
    btn_salir= Button(menu, text= "       SALIR       ", bg='#800080',bd=0, command = ir_l_e)
    btn_salir.pack()
    btn_salir.place(x=10,y=10)
    
    btn_iniciar_sesion1= Button(menu, image= img_int , bg='red', command = ir_l_m,width=290, height=290,bd=0, font=("Helvetica", 14, "bold"))
    btn_iniciar_sesion1.pack()
    btn_iniciar_sesion1.place(x=550,y=250)
    
    btn_iniciar_sesion2= Button(menu, image= img_inte , bg='red', command = ir_l_m,width=290, height=290,bd=0, font=("Helvetica", 14, "bold"))
    btn_iniciar_sesion2.pack()
    btn_iniciar_sesion2.place(x=900,y=250)
    
    
    
    mainloop()

def ir_m_l():
    menu.destroy()
    import login
    
def ir_l_e():
    menu.destroy()
     
    
def ir_l_m():
    menu.destroy()
    import registrar 

def mostrar_mensaje1():
	
    texto = """ 
_______________________________________
	
	RYZEN 3 4100x
_______________________________________
	
	
    
Modelo: 			4100
Socket:			AM4 Ryzen 4th Gen
Núcleos: 			4
Frecuencia: 		3800.00 MHz
Proceso De Fabricación: 	7 nm
Chipset GPU: 		NO Posee Gráficos Integrados
Hilos: 			8
Frecuencia Turbo: 		4000 MHz
Familia: 			AMD RYZEN 3"""
    messagebox.showinfo("INFORMACION", texto)
    
def mostrar_mensaje2():
	
    texto = """ 
_______________________________________
	
	RYZEN 5 3600x
_______________________________________
	
	
    
Modelo: 			Ryzen 5 3600
Socket:			AM4 Ryzen 3th Gen
Núcleos: 			6
Frecuencia: 		3600.00 MHz
Proceso De Fabricación: 	7 nm
Chipset GPU: 		NO Posee Gráficos Integrados
Hilos: 			12
Frecuencia Turbo: 		4200 MHz
Familia: 			AMD RYZEN 5"""
    messagebox.showinfo("INFORMACION", texto)
    
def mostrar_mensaje3():
	
    texto = """ 
_______________________________________
	
	RYZEN 7 5800x
_______________________________________
	
	
    
Modelo: 			Ryzen 7 5800
Socket:			AM4 Ryzen 4th Gen
Núcleos: 			8
Frecuencia: 		3800.00 MHz
Proceso De Fabricación: 	7 nm
Chipset GPU: 		NO Posee Gráficos Integrados
Hilos: 			16
Frecuencia Turbo: 		4700 MHz
Familia: 			AMD RYZEN 7"""
    messagebox.showinfo("INFORMACION", texto)


fun_menu()

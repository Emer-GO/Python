from tkinter import Menu,Tk,ttk,Label,Button,Entry,messagebox

def Salir():
    ventana.destroy()
def calculadora():


    #CREAMOS LAS FUNCIONES:
    def Sumar():
        n1= float(txtNumero1.get())
        n2= float(txtNumero2.get())
        suma = n1 + n2
        
        #Mostramos el resultado
        lblResultado["text"] = suma
        
    def Restar():
        n1= float(txtNumero1.get())
        n2= float(txtNumero2.get())
        resta = n1 - n2 
        
        #Mostramos el resultado
        lblResultado["text"] = resta
        
    def Multiplicar():
        n1= float(txtNumero1.get())
        n2= float(txtNumero2.get())
        multi = n1 * n2 
        
        #Mostramos el resultado
        lblResultado["text"] = multi
        
    def Dividir():
        n1= float(txtNumero1.get())
        n2= float(txtNumero2.get())
        divi = n1 / n2 
        
        #Mostramos el resultado
        lblResultado["text"] = divi
        
    

    #PASO #2 (Obligatrorio): Creamos un OBJETO o VARIABLE de
    # tipo TK.
    ventana= Tk()
    #PASO #3: Agregamos un titulo
    ventana.title("CALCULADORA TKINTER")

    #PASO #4: Agregamos las Dimensiones de la ventana
    ventana.geometry("300x200")

    #PASO #5: Creamos las etiquetas, cajas de texto y botones
    Label(ventana,text="CALCULADORA SENATI").pack()
    Label(ventana,text="Número 1: ").place(x=20, y=50)
    txtNumero1=Entry(ventana)
    txtNumero1.place(x= 90, y= 50)

    Label(ventana,text="Número 2: ").place(x=20, y=80)
    txtNumero2=Entry(ventana)
    txtNumero2.place(x= 90, y= 80)

    #Botones
    Button(ventana, text="+",width=6, command=Sumar).place(x=40, y=120)
    Button(ventana, text="-",width=6, command=Restar).place(x=100, y=120)
    Button(ventana, text="*",width=6, command=Multiplicar).place(x=160, y=120)
    Button(ventana, text="/",width=6, command=Dividir ).place(x=220, y=120)
    #PASO #6: Mostramos el resultado
    Label(ventana, text="Resultado: ").place(x=10, y= 160)
    lblResultado= Label(ventana, text=" ")
    lblResultado.place(x= 70, y=160 )
    #PASO FINAL (Obligatrorio): Mostramos o ejecutamos la ventana
    ventana.mainloop()

def cajero():


    ventana_cajero = Tk()
    ventana_cajero.title("Cajero Tkinter")
    ventana_cajero.geometry("300x200")

    def agregar():
        Name = txtUser.get()
        password=txtContra1.get()
        Npassword=txtContra2.get()

        if password ==  "":
            messagebox.showinfo(title="REGISTRO",message="El campo de contraseña no debe estar vacio")

        else:
            if password == Npassword:
                messagebox.showinfo(title="REGISTRO",message="Usuario "+Name+" Ingresado correctamente")
            
                ventana_cajero_interfaz = Tk()
                ventana_cajero_interfaz.title("Menu cajero")
                ventana_cajero_interfaz.geometry("300x200")

                Label(ventana_cajero_interfaz,text="Bienvenido al menu de Banco Pichicha").pack()
                Button(ventana_cajero_interfaz,text="Deposito").place(x=50,y=25)
                Button(ventana_cajero_interfaz,text="Retiro").place(x=50,y=25)
                Button(ventana_cajero_interfaz,text="Consulta").place(x=50,y=25)
                Button(ventana_cajero_interfaz,text="Cambiar").place(x=50,y=25)


            else:
                messagebox.showinfo(title="REGISTRO",message="La contraseña es erronea")

    def salir_cajero():
        ventana_cajero.destroy()
        
    Label(ventana_cajero,text="Bienvenido a BANCO PICHINCHA").pack()
    Label(ventana_cajero,text="Ingrese su Usuario").place(x=10,y=20)
    txtUser=Entry(ventana_cajero)
    txtUser.place(x=10,y=45)

    Label(ventana_cajero,text="Ingrese su contraseña").place(x=10,y=70)
    txtContra1=Entry(ventana_cajero)
    txtContra1.place(x=10,y=95)

    Label(ventana_cajero,text="Repita su contraseña").place(x=10,y=120)
    txtContra2=Entry(ventana_cajero)
    txtContra2.place(x=10,y=145)

    Button(ventana_cajero,text="  Ingresar  ",command=agregar).place(x=170,y=45)
    Button(ventana_cajero,text="   Salir    ",command=salir_cajero).place(x=170,y=95)



ventana=Tk()
ventana.geometry("400x400")

barra_menu = Menu()
ventana.config(menu=barra_menu)

opciones_menu =Menu(barra_menu)
opciones_menu.add_command(label="Salir",command=Salir)
barra_menu.add_cascade(label="Archivo",menu=opciones_menu)

opciones_menu =Menu(barra_menu)
opciones_menu.add_command(label="Calculadora",command=calculadora)
opciones_menu.add_command(label="Cajero",command=cajero)

barra_menu.add_cascade(label="Calculo",menu=opciones_menu)
ventana.mainloop()
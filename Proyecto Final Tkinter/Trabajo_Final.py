from tkinter import Button, Entry, Label, Tk, messagebox, ttk,Toplevel

import pymysql

#empresa
def nuevo():
    txtId.delete(0,"end")
    txtNaEmp.delete(0,"end")
    cboTipo.delete(0,"end")
    
    #La propiedad focus permite que el cursor este parpadeandp en la caja que le indiquemos
    txtId.focus()
    listado()

def eliminar():
    try :
        query="delete from EMPRESA where IDEMPRESA=%s"
        IDEMPRESA=txtId.get()

        c.execute(query, (IDEMPRESA))
        db.commit()
        messagebox.showinfo(message="Empresa eliminada correctamente")
        listado()

    except Exception as ex:
        messagebox.showerror(message=ex)

def modificar():
    try:
        query="update EMPRESA set NOMBREEMPRESA= %s,TIPOEMPRESA=%s where IDEMPRESA=%s"
        IDEMPRESA=txtId.get()
        NOMBREEMPRESA=txtNaEmp.get()
        TIPOEMPRESA=cboTipo.get()

        #ejecutamos la consulta de actualizacion
        c.execute(query, (NOMBREEMPRESA,TIPOEMPRESA,IDEMPRESA))
        db.commit()
        messagebox.showinfo(message="Empresa correctamente modificado")
        listado()
        txtId.focus()

    except Exception as ex:
        messagebox.showerror(message=ex)

def registrar():
    listado()
    try:
        query="insert into EMPRESA values(%s,%s,%s)"
        IDEMPRESA=txtId.get()
        NOMBREEMPRESA=txtNaEmp.get()
        TIPOEMPRESA=cboTipo.get()

        c.execute(query,(IDEMPRESA,NOMBREEMPRESA,TIPOEMPRESA))
        db.commit()

        messagebox.showinfo(message="Empresa {} correctamente registrada".format(NOMBREEMPRESA))
        txtId.focus()
        listado()
    except Exception as ex:
        messagebox.showerror(message=ex)

def listado():
    #Creamos un método para mostrar los datos en el TreeView de la tabla curso
    query="select * from EMPRESA"
    #A continuación ejecutamos la consulta
    c.execute(query)
    #Recuperamos todos los datos de la consulta
    datos=c.fetchall()
    #Finalmente, borramos todos los elementos que ya existen en el TreeView
    for item in tvEmp.get_children():
        tvEmp.delete(item)
    #Mostramos cada uno de lso datos en el TreeWiev
    for reg in datos:
        tvEmp.insert("", "end", text=reg[0], values=(reg[1], reg[2]))
    #Ahora registramos o actualizamos los registros
    total= c.rowcount
    lblTotal.config(text="Cant. Empresa: {}".format(total))


def empresas():
    global txtId, txtNaEmp, cboTipo, tvEmp, lblTotal
    ventana_empresa=Toplevel()
    ventana_empresa.geometry ("500x300")

    ventana_empresa.title("empresa")
    Label(ventana_empresa,text="Tabla empresa", font=("Arial", 15, "bold")).pack()
#id empresa
    Label(ventana_empresa,text="Id Empresa: ").place(x=10,y=35)
    txtId= Entry(ventana_empresa)
    txtId.place(x=10, y=60)

#label
    Label(ventana_empresa,text="Nombre de Empresa: ").place(x=10,y=85)
    txtNaEmp=Entry(ventana_empresa,width=25)
    txtNaEmp.place(x=10,y=110)

    #tipo de empresa label
    tipo=["Aerea","Terrestre"]
    Label(ventana_empresa,text="Tipo de Empresa").place(x=10,y=135)
    cboTipo=ttk.Combobox(ventana_empresa,width=31,values=tipo,state="readonly")
    cboTipo.place(x=10,y=160)

    #lista de la empresa
    #TREEVIEW
    tvEmp=ttk.Treeview(ventana_empresa,columns=("col1", "col2"))
    tvEmp.column("#0", width=60)
    tvEmp.column("col1", width=90)
    tvEmp.column("col2", width=90)
   

    #ENCABEZADOS - HEADINGS
    tvEmp.heading("#0", text="ID Empresa")
    tvEmp.heading("col1", text="Nombres")
    tvEmp.heading("col2", text="Tipo de empresa")

    tvEmp.place(x=240, y=35)


    
    lblTotal= Label(ventana_empresa,text="Cant. Estudiantes. ")
    Button(ventana_empresa,text="Registrar",width=7,command=registrar).place(x=10,y=250)
    Button(ventana_empresa,text="Modificar",width=7,command=modificar).place(x=85,y=250)
    Button(ventana_empresa,text="Nuevo",width=7,command=nuevo).place(x=160,y=250)
    Button(ventana_empresa, text="Eliminar",command=eliminar).place(x=165, y=55)
    
#Empleado
def empleado():
    global txtID, txtNombre, txtApellido, txtCelular, txtDistrito, txtCargo, tvIdCli, lblTotal_emp
    ventana_empleado=Toplevel()
    ventana_empleado.geometry ("910x400")
    ventana_empleado.title("SISTEMA DE CONTROL DE EMPLEADOS")
    Label(ventana_empleado, text="CONTROL DE EMPLEADOS", font=("Arial", 15, "bold")).pack()
    #CAJA IDEMPLEADO
    Label(ventana_empleado, text="ID Empleado:").place(x=10, y=45)
    txtID= Entry(ventana_empleado,width=18)
    txtID.place(x=10, y=65)
    #BOTÓN ELIMINAR
    Button(ventana_empleado, text="Eliminar", width=10, command=eliminar_empleado).place(x=165, y=65)
    #CAJA NOMBRES
    Label(ventana_empleado, text="Nombres:").place(x=10, y=95)
    txtNombre= Entry(ventana_empleado,width=39)
    txtNombre.place(x=10, y=114)
    #CAJA APELLIDOS
    Label(ventana_empleado, text="Apellidos:").place(x=10, y=140)
    txtApellido= Entry(ventana_empleado,width=39)
    txtApellido.place(x=10, y=160)
    #CAJA CELULAR
    Label(ventana_empleado, text="Celular:").place(x=10, y=186)
    txtCelular= Entry(ventana_empleado,width=39)
    txtCelular.place(x=10, y=210)
    #CAJA DISTRITO
    Label(ventana_empleado, text="Distrito:").place(x=10, y=234)
    txtDistrito= Entry(ventana_empleado,width=39)
    txtDistrito.place(x=10, y=258)
    #CAJA CARGO
    Label(ventana_empleado, text="Cargo:").place(x=10, y=284)
    txtCargo= Entry(ventana_empleado,width=39)
    txtCargo.place(x=10, y=305)
    #BOTONES
    Button(ventana_empleado, text="Registrar", width=10, command=registrar_empleado).place(x=10, y=360)
    Button(ventana_empleado, text="Modificar", width=10, command=modificar_empleado).place(x=93, y=360)
    Button(ventana_empleado, text="Nuevo", width=10, command=nuevo_empleado).place(x=175, y=360)
    #TREEVIEW
    tvIdCli=ttk.Treeview(ventana_empleado,columns=("col1", "col2", "col3", "col4", "col5"))
    tvIdCli.column("#0", width=80)
    tvIdCli.column("col1", width=135)
    tvIdCli.column("col2", width=135)
    tvIdCli.column("col3", width=80)
    tvIdCli.column("col4", width=85)
    tvIdCli.column("col5", width=100)
    #ENCABEZADOS - HEADINGS
    tvIdCli.heading("#0", text="ID Empleado")
    tvIdCli.heading("col1", text="Nombres")
    tvIdCli.heading("col2", text="Apellidos")
    tvIdCli.heading("col3", text="Celular")
    tvIdCli.heading("col4", text="Distrito")
    tvIdCli.heading("col5", text="Cargo")
    tvIdCli.place(x=280, y=50)
    #LABEL DE TOTAL EMPLEADO
    lblTotal_emp=Label(ventana_empleado, text=("Total de empleados: 0"))
    lblTotal_emp.place(x=750, y=290) 
    
def modificar_empleado():
    try:
        query="update empleado set NOMBREEMPLEADO= %s, APELLIDOEMPLEADO= %s, CELULAR= %s, DISTRITO= %s, CARGO=%s where idempleado= %s"
        idempleado=txtID.get()
        nombre=txtNombre.get()
        apellido=txtApellido.get()
        celular= int(txtCelular.get())
        distrito= txtDistrito.get()
        cargo=txtCargo.get()
        c.execute(query, (nombre, apellido, celular, distrito, cargo, idempleado))
        db.commit()
        messagebox.showinfo(message="Empleado modificado satisfactoria.")
        listado_empleado()
        nuevo_empleado()
    except Exception as ex:
        messagebox.showerror(message=ex)

def listado_empleado():
    query="select * from empleado"
    c.execute(query)
    datos=c.fetchall()
    for item in tvIdCli.get_children():
        tvIdCli.delete(item)
    for reg in datos:
        tvIdCli.insert("", "end", text=reg[0], values=(reg[1], reg[2], reg[3], reg[4], reg[5]))
    total= c.rowcount
    lblTotal_emp.config(text="Total de empleados: {}".format(total))

def registrar_empleado():
    try:
        query= "insert into empleado values(%s, %s, %s, %s, %s, %s)"
        idempleado=txtID.get()
        nombre=txtNombre.get()
        apellido=txtApellido.get()
        celular= int(txtCelular.get())
        distrito= txtDistrito.get()
        cargo=txtCargo.get()
        c.execute(query, (idempleado, nombre, apellido, celular, distrito, cargo))
        db.commit()
        messagebox.showinfo(message="Empleado {} registrado satisfactoriamente.".format(nombre))
        listado_empleado()
        nuevo_empleado()
    except Exception as ex:
        messagebox.showerror(message=ex)

def eliminar_empleado():
    try:
        query= "delete from empleado where idempleado= %s"
        codigo= txtID.get()
        c.execute(query, (codigo))
        db.commit()
        messagebox.showinfo(message="Empleado eliminado satisfactoriamente")
        listado_empleado()
    except Exception as ex:
        messagebox.showerror(message=ex)

def nuevo_empleado():
    txtID.delete(0, "end")
    txtNombre.delete(0, "end")
    txtApellido.delete(0, "end")
    txtCelular.delete(0, "end")
    txtDistrito.delete(0, "end")
    txtCargo.delete(0, "end")
    txtID.focus()


#Cliente
def Cliente():
    global txtID_CLIENTE, txtNombre_CLIENTE, txtApellido_CLIENTE, txtCelular_CLIENTE, txtDistrito_CLIENTE,txtEmail_CLIENTE,lblTotal_CLIENTE,tvIdCli
    ventana_cliente=Toplevel()
    ventana_cliente.geometry ("950x400")
    ventana_cliente.title("SISTEMA DE CONTROL DE CLIENTES")
    Label(ventana_cliente, text="CONTROL DE CLIENTES", font=("Arial", 15, "bold")).pack()
    #CAJA IDCLIENTE
    Label(ventana_cliente, text="ID Cliente:").place(x=10, y=45)
    txtID_CLIENTE= Entry(ventana_cliente,width=18)
    txtID_CLIENTE.place(x=10, y=65)
    #BOTÓN ELIMINAR
    Button(ventana_cliente, text="Eliminar", width=10, command=eliminar_CLIENTE).place(x=165, y=65)
    #CAJA NOMBRES
    Label(ventana_cliente, text="Nombres:").place(x=10, y=95)
    txtNombre_CLIENTE= Entry(ventana_cliente,width=39)
    txtNombre_CLIENTE.place(x=10, y=114)
    #CAJA APELLIDOS
    Label(ventana_cliente, text="Apellidos:").place(x=10, y=140)
    txtApellido_CLIENTE= Entry(ventana_cliente,width=39)
    txtApellido_CLIENTE.place(x=10, y=160)
    #CAJA CELULAR
    Label(ventana_cliente, text="Celular:").place(x=10, y=186)
    txtCelular_CLIENTE= Entry(ventana_cliente,width=39)
    txtCelular_CLIENTE.place(x=10, y=210)
    #CAJA DISTRITO
    Label(ventana_cliente, text="Distrito:").place(x=10, y=234)
    txtDistrito_CLIENTE= Entry(ventana_cliente,width=39)
    txtDistrito_CLIENTE.place(x=10, y=258)
    #CAJA EDAD
    Label(ventana_cliente, text="Email:").place(x=10, y=284)
    txtEmail_CLIENTE= Entry(ventana_cliente,width=39)
    txtEmail_CLIENTE.place(x=10, y=305)
    #BOTONES
    Button(ventana_cliente, text="Registrar", width=10, command=registrar_CLIENTE).place(x=10, y=360)
    Button(ventana_cliente, text="Modificar", width=10, command=modificar_CLIENTE).place(x=93, y=360)
    Button(ventana_cliente, text="Nuevo", width=10, command=nuevo_CLIENTE).place(x=175, y=360)
    #TREEVIEW
    tvIdCli=ttk.Treeview(ventana_cliente,columns=("col1", "col2", "col3", "col4", "col5"))
    tvIdCli.column("#0", width=60)
    tvIdCli.column("col1", width=135)
    tvIdCli.column("col2", width=135)
    tvIdCli.column("col3", width=80)
    tvIdCli.column("col4", width=85)
    tvIdCli.column("col5", width=160)
    #ENCABEZADOS - HEADINGS
    tvIdCli.heading("#0", text="ID Cliente")
    tvIdCli.heading("col1", text="Nombres")
    tvIdCli.heading("col2", text="Apellidos")
    tvIdCli.heading("col3", text="Celular")
    tvIdCli.heading("col4", text="Distrito")
    tvIdCli.heading("col5", text="Email")
    tvIdCli.place(x=280, y=50)
    #LABEL DE TOTAL CLIENTES
    lblTotal_CLIENTE=Label(ventana_cliente, text=("Total de clientes: 0"))
    lblTotal_CLIENTE.place(x=780, y=290)

def modificar_CLIENTE():
    
    try:
        query="update cliente set NOMBRECLIENTE= %s, APELLIDOCLIENTE= %s, CELULARCLIENTE= %s, DISTRITO= %s, EMAIL=%s where IDCLIENTE= %s"
        idcliente=txtID_CLIENTE.get()
        nombre_cli=txtNombre_CLIENTE.get()
        apellido_cli=txtApellido_CLIENTE.get()
        celular_cli= int(txtCelular_CLIENTE.get())
        distrito_cli= txtDistrito_CLIENTE.get()
        email_cli=txtEmail_CLIENTE.get()
        c.execute(query, (nombre_cli, apellido_cli, celular_cli, distrito_cli, email_cli, idcliente))
        db.commit()
        messagebox.showinfo(message="cliente modificado satisfactoria.")
        listado_CLIENTE()
        nuevo_CLIENTE()
    except Exception as ex:
        messagebox.showerror(message=ex)

def listado_CLIENTE():
    query="select * from cliente"
    c.execute(query)
    datos=c.fetchall()
    for item in tvIdCli.get_children():
        tvIdCli.delete(item)
    for reg in datos:
        tvIdCli.insert("", "end", text=reg[0], values=(reg[1], reg[2], reg[3], reg[4], reg[5]))
    total= c.rowcount
    lblTotal_CLIENTE.config(text="Total de clientes: {}".format(total))

def registrar_CLIENTE():
    try:
        query= "insert into cliente values(%s, %s, %s, %s, %s,%s)"
        idcliente=txtID_CLIENTE.get()
        nombre_cli=txtNombre_CLIENTE.get()
        apellido_cli=txtApellido_CLIENTE.get()
        celular_cli= int(txtCelular_CLIENTE.get())
        distrito_cli= txtDistrito_CLIENTE.get()
        email_cli=txtEmail_CLIENTE.get()
        c.execute(query(idcliente,nombre_cli, apellido_cli, celular_cli, distrito_cli, email_cli))
        db.commit()
        messagebox.showinfo(message="Cliente {} registrado satisfactoriamente.".format(nombre_cli))
        listado_CLIENTE()
        nuevo_CLIENTE()
    except Exception as ex:
        messagebox.showerror(message=ex)

def eliminar_CLIENTE():
    try:
        query= "delete from cliente where idcliente= %s"
        codigo= txtID_CLIENTE.get()
        c.execute(query, (codigo))
        db.commit()
        messagebox.showinfo(message="Cliente eliminado satisfactoriamente")
        listado_CLIENTE()
    except Exception as ex:
        messagebox.showerror(message=ex)

def nuevo_CLIENTE():
    txtID_CLIENTE.delete(0, "end")
    txtNombre_CLIENTE.delete(0, "end")
    txtApellido_CLIENTE.delete(0, "end")
    txtCelular_CLIENTE.delete(0, "end")
    txtDistrito_CLIENTE.delete(0, "end")
    txtEmail_CLIENTE.delete(0, "end")
    txtID_CLIENTE.focus()

#VENTA
def venta():
    global txtID_venta, cboDestino, txtCantidad_venta,tvCursos,txtHora_venta,lblTotal_venta
    ventana_venta=Toplevel()
    ventana_venta.geometry ("940x410")
    ventana_venta.title("Venta de viajes")
    Label(ventana_venta, text="Venta De Viajes", font=("Arial", 16, "bold")).pack()
    #CAJA ID
    Label(ventana_venta, text="ID:").place(x=10, y=45)
    txtID_venta=Entry(ventana_venta,width=50)
    txtID_venta.place(x=10, y=65)

    Destino_List=["Lima", "Ucayali", "Tarapoto", "La libertad", "Senati", "2asa de delegado"]


    Label(ventana_venta, text="Destino:").place(x=10, y=90)
    cboDestino=ttk.Combobox(ventana_venta,state="readonly", values=Destino_List)
    cboDestino.place(x=10, y=120)





    #CAJA CURSO
    Label(ventana_venta, text="Precio:").place(x=10, y=170)
    txtCantidad_venta=Entry(ventana_venta,width=50)
    txtCantidad_venta.place(x=10, y=190)
    #CAJA CICLO
    Label(ventana_venta, text="Hora del Viaje:").place(x=10, y=225)
    txtHora_venta=Entry(ventana_venta,width=50)
    txtHora_venta.place(x=10, y=245)
    #CAJA HORAS

    Button(ventana_venta, text="Registrar", width=10, command=registrar_venta).place(x=10, y=350)
    Button(ventana_venta, text="Modificar", width=10, command=Modificar_venta).place(x=93, y=350)
    Button(ventana_venta, text="Nuevo", width=10,command=Nuevo_venta).place(x=175, y=350)
    Button(ventana_venta, text="Eliminar", width=10, command=eliminar_venta).place(x=257, y=350)
    #TREEVIEW
    tvCursos=ttk.Treeview(ventana_venta,columns=("col1", "col2", "col3"))
    tvCursos.column("#0", width=120)
    tvCursos.column("col1", width=150)
    tvCursos.column("col2", width=150)
    tvCursos.column("col3", width=150)

    #ENCABEZADOS - HEADINGS
    tvCursos.heading("#0", text="ID Viaje3")
    tvCursos.heading("col1", text="Destino")
    tvCursos.heading("col2", text="Precio")
    tvCursos.heading("col3", text="Hora del viaje")

    tvCursos.place(x=350, y=60)
    #LABEL DE TOTAL CURSOS
    lblTotal_venta=Label(ventana, text=("Total Viajes: 0"))
    lblTotal_venta.place(x=800, y=400)

def eliminar_venta():
    try:
        query="delete from VENTA where IDVENTA= %s"
        idventa=txtID_venta.get()
        #Ejecutamos la consulta
        c.execute(query,(idventa))
        db.commit()
        messagebox.showinfo(message="viaje Eliminado Sactisfactoriamente")
        listado_venta()
        

    except Exception as ex:
        messagebox.showerror(message="Seleccione una opcion")
def Nuevo_venta():
    txtID_venta.delete(0,"end")
    txtCantidad_venta.delete(0,"end")
   
    txtHora_venta.delete(0,"end")
    #La propiedad focus permite que el cursos este parpadeando en la caja que le indiquemos
    txtID_venta.focus()

def Modificar_venta():
    
    try:
        query="update venta set DESTINO=%s ,PRECIO=%s, TIEMPOMIN=%s where IDVENTA=%s"
        
        idventa=txtID_venta.get()
        destino=cboDestino.get()
        precio=txtCantidad_venta.get()
        tiempomin=txtHora_venta.get()
        

        #Ahora ejecutamos la QUERY
        c.execute(query, ( destino, precio, tiempomin, idventa))
        db.commit()
        messagebox.showinfo(message="Viaje Modificado satisfactoriamente")
        listado_venta()
        Nuevo_venta()

    except Exception as ex:
        messagebox.showerror(message=ex)

def listado_venta():

    #Creamos un método para mostrar los datos en el TreeView de la tabla curso
    query="select * from VENTA"
    #A continuación ejecutamos la consulta
    c.execute(query)
    #Recuperamos todos los datos de la consulta
    datos=c.fetchall()
    #Finalmente, borramos todos los elementos que ya existen en el TreeView
    for item in tvCursos.get_children():
        tvCursos.delete(item)
    #Mostramos cada uno de lso datos en el TreeWiev
    for reg in datos:
        tvCursos.insert("", "end", text=reg[0], values=(reg[1], reg[2], reg[3]))
    #Ahora registramos o actualizamos los registros
    total=c.rowcount
    lblTotal_venta.config(text="Total Viajes: {}".format(total))

def registrar_venta():
    global idventa,destino,precio,tiempomin
    try:
        #Creamos un QUERY (Consulta) para poder registrar cursos y
        #sus valores en la BD
        query= "insert into venta values(%s, %s, %s, %s)"
        #Ahora obtenemos cada uno de los campos de la BD
        idventa=txtID_venta.get()
        destino=cboDestino.get()
        precio=txtCantidad_venta.get()
        tiempomin=txtHora_venta.get()
        

        #Ahora ejecutamos la QUERY
        c.execute(query, (idventa, destino, precio, tiempomin))
        #Utilizamos el ingreso en el TreeView y en la BD
        db.commit()
        #Mostramos un mensaje en caso se registró
        messagebox.showinfo(message="Curso de registrado satisfactoriamente el viaje.")
        listado_venta()
        Nuevo_venta()
    except Exception as ex:
        messagebox.showerror(message=ex)
#Ventana Principal
ventana=Tk()
ventana.geometry ("280x230")
ventana.title("Venta de boletos")
Label(ventana, text="VENTA DE BOLETOS DE VIAJE", font=("Arial", 12, "bold")).pack()

Button(ventana, text="Empresa", width=11, command=empresas, font=("Arial", 11, "bold"), bg="#2271B3", fg="#FFFFFF").place(x=85, y=30)
Button(ventana, text="Empleado", width=11, command=empleado, font=("Arial", 11, "bold"), bg="#BA0000", fg="#FFFFFF").place(x=85, y=70)
Button(ventana, text="Cliente", width=11, command=Cliente, font=("Arial", 11, "bold"), bg="#1e8529", fg="#FFFFFF").place(x=85, y=110)
Button(ventana, text="Venta", width=11, command=venta, font=("Arial", 11, "bold"), bg="#ee4a00", fg="#FFFFFF").place(x=85, y=150)

try:
    db = pymysql.connect(host="localhost", user="root", password="", db="VENTA_BOLETOS")
    c=db.cursor()
except Exception as ex:
    messagebox.showerror(message=ex)
    
    ventana.destroy()

db.close 
ventana.mainloop()

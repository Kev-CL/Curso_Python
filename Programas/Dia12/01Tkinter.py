from tkinter import *

# Iniciando tkinter
aplicacion = Tk()

# Tamaño de la ventana
aplicacion.geometry('1020x630+0+0') # (largo x ancho + x + y)

# Evitar maximizar
aplicacion.resizable(False,False)

# Titulo de la ventana
aplicacion.title('Mi restaurante - Sistema de facturación')

# Color de fondo
aplicacion.config(bg='burlywood')

# *********************************************************************************
# Panel superior
# FLAT - RAISED - SUNKEN - GROOVE - RIDGE
panel_superior = Frame(aplicacion, bd=1, relief=FLAT)
panel_superior.pack(side=TOP)

# etiqueta titulo
etiqueta_titulo = Label(panel_superior, text='Sistema de facturación', fg='azure4',
                        font=('Dosis', 58), bg='burlywood', width=22)
etiqueta_titulo.grid(row=0, column=0)

# *********************************************************************************
# Panel izquierdo
panel_izquierdo = Frame(aplicacion, bd=1, relief=FLAT)
panel_izquierdo.pack(side=LEFT)

# Panel costos
panel_costos = Frame(panel_izquierdo, bd=1, relief=FLAT, bg='azure4', padx=90)
panel_costos.pack(side=BOTTOM)

# Panel comidas
panel_comidas = LabelFrame(panel_izquierdo, text='Comidas', font=('Dosis', 19, 'bold'),
                           bd=1, relief=FLAT, fg='azure4')
panel_comidas.pack(side=LEFT)

# Panel bebidas
panel_bebidas = LabelFrame(panel_izquierdo, text='Bebidas', font=('Dosis', 19, 'bold'),
                           bd=1, relief=FLAT, fg='azure4')
panel_bebidas.pack(side=LEFT)

# Panel postres
panel_postres = LabelFrame(panel_izquierdo, text='Postres', font=('Dosis', 19, 'bold'),
                           bd=1, relief=FLAT, fg='azure4')
panel_postres.pack(side=LEFT)

# *********************************************************************************
# Panel derecho
panel_derecho = Frame(aplicacion, bd=1, relief=FLAT)
panel_izquierdo.pack(side=RIGHT)

# Panel calculadora
panel_calculadora = Frame(panel_derecho, bd=1, relief=FLAT, bg='burlywood')
panel_calculadora.pack()

# Panel recibo
panel_recibo = Frame(panel_derecho, bd=1, relief=FLAT, bg='burlywood')
panel_recibo.pack()

# Panel botones
panel_botones = Frame(panel_derecho, bd=1, relief=FLAT, bg='burlywood')
panel_botones.pack()

# *********************************************************************************
# En panel izquierdo

# Lista de productos
lista_comidas = ['pollo', 'costillas', 'Cordon Blue', 'Pizza']
lista_bebidas = ['Coca-cola', 'Vino', 'Agua natural']
lista_postres = ['helado', 'pastel']

# Items comida
variables_comida = []
cuadros_comida = []
texto_comida = []
contador = 0
for comida in lista_comidas:
    # Crear checkbutton
    variables_comida.append('')
    variables_comida[contador] = IntVar()
    comida = Checkbutton(panel_comidas,
                         text=comida.title(),
                         font=('Dosis', 19, 'bold'),
                         onvalue=1,
                         offvalue=0,
                         variable=variables_comida[contador])
    comida.grid(row=contador,
                column=0,
                sticky=W)

    # Crear los cuadros de entrada
    cuadros_comida.append('')
    texto_comida.append('')
    texto_comida[contador] = StringVar()
    texto_comida[contador].set('0')
    cuadros_comida[contador] = Entry(panel_comidas,
                                     font=('Dosis', 18, 'bold'),
                                     bd=1,
                                     width=6,
                                     state=DISABLED,
                                     textvariable=texto_comida[contador])
    cuadros_comida[contador].grid(row=contador,
                                  column=1)
    contador += 1

# Items bebida
variables_bebida = []
cuadros_bebida = []
texto_bebida = []
contador = 0
for bebida in lista_bebidas:
    # Crear checkbutton
    variables_bebida.append('')
    variables_bebida[contador] = IntVar()
    bebida = Checkbutton(panel_bebidas, text=bebida.title(), font=('Dosis', 19, 'bold'),
                         onvalue=1, offvalue=0, variable=variables_bebida[contador])
    bebida.grid(row=contador, column=0, sticky=W)
    # Crear los cuadros de entrada
    cuadros_bebida.append('')
    texto_bebida.append('')
    texto_bebida[contador] = StringVar()
    texto_bebida[contador].set('0')
    cuadros_bebida[contador] = Entry(panel_bebidas,
                                     font=('Dosis', 18, 'bold'),
                                     bd=1,
                                     width=6,
                                     state=DISABLED,
                                     textvariable=texto_bebida[contador])
    cuadros_bebida[contador].grid(row=contador,
                                  column=1)
    contador += 1
# Items postre
variables_postre = []
cuadros_postre = []
texto_postre = []
contador = 0
for postre in lista_postres:
    # Crear checkbutton
    variables_postre.append('')
    variables_postre[contador] = IntVar()
    postre = Checkbutton(panel_postres, text=postre.title(), font=('Dosis', 19, 'bold'),
                         onvalue=1, offvalue=0, variable=variables_postre[contador])
    postre.grid(row=contador, column=0, sticky=W)
    # Crear los cuadros de entrada
    cuadros_postre.append('')
    texto_postre.append('')
    texto_postre[contador] = StringVar()
    texto_postre[contador].set('0')
    cuadros_postre[contador] = Entry(panel_postres,
                                     font=('Dosis', 18, 'bold'),
                                     bd=1,
                                     width=6,
                                     state=DISABLED,
                                     textvariable=texto_postre[contador])
    cuadros_postre[contador].grid(row=contador,
                                  column=1)
    contador += 1

# *******************************************************************************
# En panel de costos
# Variables
var_costo_comida = StringVar()
var_costo_bebida = StringVar()
var_costo_postres = StringVar()
var_subtotal = StringVar()
var_impuesto = StringVar()
var_total = StringVar()

# Etiqueta de costos y campos de entrada
#Comida
etiqueta_costo_comida = Label(panel_costos,
                        text='Costo Comida',
                        font=('Dosis', 12, 'bold'),
                        bg='azure4',
                        fg='white')
etiqueta_costo_comida.grid(row=0, column=0)
texto_costo_comida = Entry(panel_costos,
                           font='Dosis',
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_costo_comida)
texto_costo_comida.grid(row=0, column=1, padx=41)

#bebida
etiqueta_costo_bebida = Label(panel_costos,
                        text='Costo bebida',
                        font=('Dosis', 12, 'bold'),
                        bg='azure4',
                        fg='white')
etiqueta_costo_bebida.grid(row=1, column=0)
texto_costo_bebida = Entry(panel_costos,
                           font='Dosis',
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_costo_bebida)
texto_costo_bebida.grid(row=1, column=1, padx=41)

#postres
etiqueta_costo_postres = Label(panel_costos,
                        text='Costo Postres',
                        font=('Dosis', 12, 'bold'),
                        bg='azure4',
                        fg='white')
etiqueta_costo_postres.grid(row=2, column=0)
texto_costo_postres = Entry(panel_costos,
                           font='Dosis',
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_costo_postres)
texto_costo_postres.grid(row=2, column=1, padx=41)

#subtotal
etiqueta_subtotal = Label(panel_costos,
                        text='Subtotal',
                        font=('Dosis', 12, 'bold'),
                        bg='azure4',
                        fg='white')
etiqueta_subtotal.grid(row=0, column=2)
texto_subtotal = Entry(panel_costos,
                           font='Dosis',
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_subtotal)
texto_subtotal.grid(row=0, column=3, padx=41)

#Impuesto
etiqueta_impuesto = Label(panel_costos,
                        text='Impuesto',
                        font=('Dosis', 12, 'bold'),
                        bg='azure4',
                        fg='white')
etiqueta_impuesto.grid(row=1, column=2)
texto_impuesto = Entry(panel_costos,
                           font='Dosis',
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_impuesto)
texto_impuesto.grid(row=1, column=3, padx=41)

#Total
etiqueta_total = Label(panel_costos,
                        text='Total',
                        font=('Dosis', 12, 'bold'),
                        bg='azure4',
                        fg='white')
etiqueta_total.grid(row=0, column=0)
texto_total = Entry(panel_costos,
                           font='Dosis',
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_total)
texto_total.grid(row=0, column=1, padx=41)

# Evtiar que app se cierre
aplicacion.mainloop()
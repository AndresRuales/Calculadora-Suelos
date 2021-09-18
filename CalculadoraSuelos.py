from tkinter import *
from tkinter import messagebox

ventana = Tk()

ventana.title("Cálculo Propiedades del suelo")
ventana.geometry("517x600")
ventana.configure(bg="#38383A")
#Metodo --> set --> para asignar un valor, Ej: dato.set(23)
#Metodo --> get --> para obtener un valor, Ej: dato.get()

#Funciones

textopantallapesoAgua=DoubleVar()
textopantallaDensidadReal=DoubleVar()
textopantallaHumedadGravimetrica=DoubleVar()
textopantallaPorosidad=DoubleVar()
textopantallaHumedadVolumetrica=DoubleVar()

pesohumedo=DoubleVar()
pesoseco=DoubleVar()
volumentotal=DoubleVar()
densidadreal=DoubleVar()



def pesoAgua():
    resultado = pesohumedo.get()-pesoseco.get()
    textopantallapesoAgua.set(resultado)

def densidadaparente():
    resultado=pesoseco.get()/volumentotal.get()
    textopantallaDensidadReal.set(resultado)

def porosidad():
    resultado=(1-(textopantallaDensidadReal.get()/densidadreal.get()))*100
    textopantallaPorosidad.set(resultado)

def humedadgravimetrica():
    resultado=(textopantallapesoAgua.get()/pesoseco.get())*100
    textopantallaHumedadGravimetrica.set(resultado)

def humedadvolumetrica():
    resultado=textopantallaHumedadGravimetrica.get()*textopantallaDensidadReal.get()
    textopantallaHumedadVolumetrica.set(resultado)


def calcular():
    if pesohumedo.get() ==0.0:
        messagebox.showerror("Error","Peso total de suelo húmedo sin digitar.")
    elif pesoseco.get() ==0.0:
        messagebox.showerror("Error","Peso suelo seco sin digitar.",)
    elif volumentotal.get()==0.0:
        messagebox.showerror("Error","Volumen total sin digitar.")
    elif densidadreal.get()==0.0:
        messagebox.showerror("Error", "Densidad real sin digitar.")
    else:
        pesoAgua()
        densidadaparente()
        porosidad()
        humedadgravimetrica()
        humedadvolumetrica()

def clear():
    textopantallapesoAgua.set(0.0)
    textopantallaDensidadReal.set(0.0)
    textopantallaHumedadGravimetrica.set(0.0)
    textopantallaPorosidad.set(0.0)
    textopantallaHumedadVolumetrica.set(0.0)
    pesohumedo.set(0.0)
    pesoseco.set(0.0)
    volumentotal.set(0.0)
    densidadreal.set(0.0)

    #Segunda parte

profundidadSuelo = DoubleVar()
CC=DoubleVar()
PMP=DoubleVar()
DPM=DoubleVar()
eficienciaderiego=DoubleVar()

textopantallaLamina=DoubleVar()
textopantallaAA=DoubleVar()
textopantallaLAA=DoubleVar()
textopantallaLARA=DoubleVar()
textopantallaLARANETA=DoubleVar()

def lamina():
    resultado=(textopantallaHumedadGravimetrica.get()/100)*textopantallaDensidadReal.get()*profundidadSuelo.get()
    textopantallaLamina.set(resultado)

def aguaAprovechable():
    resultado=CC.get()-PMP.get()
    textopantallaAA.set(resultado)

def LaminadeAguaAprovechable():
    resultado=(((CC.get()-PMP.get())/100)*textopantallaDensidadReal.get()*profundidadSuelo.get())*10
    textopantallaLAA.set(resultado)

def laminadeAguaRapidamenteAprovechable():
    resultado=((textopantallaLAA.get()*DPM.get())/100)
    textopantallaLARA.set(resultado)

def laminaAguaRapidamenteAprovechableNeta():
    resultado=textopantallaLARA.get()/(eficienciaderiego.get()/100)
    textopantallaLARANETA.set(resultado)

def calcular2():

    if profundidadSuelo.get() ==0.0:
        messagebox.showerror("Error","Profundidad del suelo sin digitar.")
    elif CC.get() ==0.0:
        messagebox.showerror("Error","CC sin digitar.",)
    elif PMP.get()==0.0:
        messagebox.showerror("Error","PMP digitar.")
    elif DPM.get()==0.0:
        messagebox.showerror("Error", "DPM sin digitar.")
    elif eficienciaderiego.get()==0.0:
        messagebox.showerror("Error", "Eficiencia de riego sin digitar.")
    elif textopantallaHumedadGravimetrica.get()==0.0 or textopantallaDensidadReal.get()==0.0:
        messagebox.showerror("Error", "Para el calculo de la lamina es necesario W(%) y Da (gr/cm³")

    else:
        lamina()
        aguaAprovechable()
        LaminadeAguaAprovechable()
        laminadeAguaRapidamenteAprovechable()
        laminaAguaRapidamenteAprovechableNeta()

def clear2():
    CC.set(0.0)
    PMP.set(0.0)
    DPM.set(0.0)
    eficienciaderiego.set(0.0)
    textopantallaLamina.set(0.0)
    textopantallaAA.set(0.0)
    textopantallaLAA.set(0.0)
    textopantallaLARA.set(0.0)
    textopantallaLARANETA.set(0.0)
    profundidadSuelo.set(0.0)

def informacion():
    global Imagen1
    global Imagen2
    global Imagen3
    global Imagen4
    global Imagen5
    global Imagen6
    global Imagen7
    global Imagen8
    global Imagen9

    ventana1 = Toplevel()
    ventana1.title("Información")
    ventana1.geometry("600x600")
    ventana1.configure(bg="#38383A")
    titulo2 = Label(ventana1, text="Información", font=('Calibri', 20, "bold"),  fg = "#FFFFFF",bg="#38383A").place(
        relx=0.5, y=30, anchor=CENTER)
    explicacion=Label(ventana1,text="Ingrese los datos en los cuadros de color verde.", font = ('Calibri',15,"italic",),fg = "#FFFFFF",bg="#38383A").place(x=15,y=55)
    Cuadroverde = Entry(ventana1, font=('Calibri', 15), justify=CENTER, bg="#76EA3D",
                               ).place(x=410, y=55, width=40, height=25)
    explicacion2=Label(ventana1,text="Los cuadros de color naranja se llenarán automaticamente\ncon la información suministrada en los cuadros verdes.",justify=LEFT, font = ('Calibri',15,"italic"),fg = "#FFFFFF",bg="#38383A").place(x=15,y=85)
    CuadroNaranja = Entry(ventana1, font=('Calibri', 15), justify=CENTER, bg="#F08C2D",
                        ).place(x=510, y=100, width=40, height=25)
    explicacion3=Label(ventana1,text="Da=Densidad aparente.\nDr=Densidad real.\nW=Humedad gravimétrica.\nθ=Humedad volumétrica.\nn=Porosidad.\nCC=Capacidad de campo.\nPMP=Punto de marchitez permanente.\nDPM=Deficit permisible de manejo.\nLam=Lamina de agua.\nAA=Agua aprovechable.\nLAA=Lamina de agua aprovechable.\nLARA=Lamina de agua rapidamente\naprovechable.",justify=LEFT, font = ('Calibri',14,"italic"),fg = "#FFFFFF",bg="#38383A").place(x=15,y=140)

    #Imagenes

    imagenDa=PhotoImage(file="Da.png")
    Imagen1=Label(ventana1,image=imagenDa).place(x=250,y=150)

    W = PhotoImage(file="W.png")
    Imagen2 = Label(ventana1, image=W).place(x=380, y=150)

    Tetta = PhotoImage(file="Tetta.png")
    Imagen3 = Label(ventana1, image=Tetta).place(x=250, y=220)

    Porosidad = PhotoImage(file="Porosidad.png")
    Imagen4 = Label(ventana1, image=Porosidad).place(x=405, y=220)

    Lamina = PhotoImage(file="Lamina.png")
    Imagen5 = Label(ventana1, image=Lamina).place(x=15, y=450)

    AA = PhotoImage(file="AA.png")
    Imagen6 = Label(ventana1, image=AA).place(x=340, y=290)

    LAA = PhotoImage(file="LAA.png")
    Imagen7 = Label(ventana1, image=LAA).place(x=15, y=520)

    LARA = PhotoImage(file="LARA.png")
    Imagen8 = Label(ventana1, image=LARA).place(x=340, y=340)

    LARANeta = PhotoImage(file="LARANeta.png")
    Imagen9 = Label(ventana1, image=LARANeta).place(x=370, y=410)

    ventana1.mainloop()


def is_valid_char(char):
    return char in "0123456789."

validatecommand = ventana.register(is_valid_char)


#Labels:

                                        #font --> (Fuente, tamaño)
                                        #fg --> Color del texto
                                        #justify --> Alineacion de texto, LEFT, RIGHT, CENTER
                                        #bg --> Color del fondo del texto

titulo=Label(ventana, text ="Soil Properties", font = ('Calibri',20,"bold"), fg = "#FFFFFF",bg="#38383A").place(relx=0.5, y=30, anchor=CENTER)

PesoTotalHumedo=Label(ventana, text ="Peso total suelo húmedo (gr):", font = ('Calibri',15,"italic"), fg = "#FFFFFF",bg="#38383A").place(x=15,y=55)
PesoSeco=Label(ventana,text ="Peso suelo seco (gr):", font = ('Calibri',15,"italic"), fg = "#FFFFFF",bg="#38383A").place(x=15,y=85)
PesoAgua = Label(ventana, text ="Peso agua (gr):", font = ('Calibri',15,"italic"), fg = "#FFFFFF",bg="#38383A").place(x=15,y=115)
VolumenTotal=Label(ventana, text ="Volumen total (cm³):", font = ('Calibri',15,"italic"), fg = "#FFFFFF",bg="#38383A").place(x=15,y=145)
VolumenPorosidad=Label(ventana, text ="n (%):", font = ('Calibri',15,"italic"), fg = "#FFFFFF",bg="#38383A").place(x=15,y=175)


Da=Label(ventana, text ="Da (gr/cm³):", font = ('Calibri',15,"italic"), fg = "#FFFFFF",bg="#38383A").place(x=350,y=55)
Dr=Label(ventana, text ="Dr (gr/cm³):", font = ('Calibri',15,"italic"), fg = "#FFFFFF",bg="#38383A").place(x=350,y=85)
wLabel=Label(ventana, text ="W (%):", font = ('Calibri',15,"italic"), fg = "#FFFFFF",bg="#38383A").place(x=350,y=115)
TettaLabel=Label(ventana, text ="θ (%):", font = ('Calibri',15,"italic"), fg = "#FFFFFF",bg="#38383A").place(x=350,y=145)

    #Segunda parte
profundidad=Label(ventana, text ="Profundidad suelo (cm):", font = ('Calibri',15,"italic"), fg = "#FFFFFF",bg="#38383A").place(x=15,y=220)
capacidadCampo=Label(ventana, text ="CC (%):", font = ('Calibri',15,"italic"), fg = "#FFFFFF",bg="#38383A").place(x=15,y=250)
PMPLabel=Label(ventana, text ="PMP (%):", font = ('Calibri',15,"italic"), fg = "#FFFFFF",bg="#38383A").place(x=15,y=280)
DPMLabel=Label(ventana, text ="DPM (%):", font = ('Calibri',15,"italic"), fg = "#FFFFFF",bg="#38383A").place(x=15,y=310)
EficienciaRiego=Label(ventana, text ="Eficiencia de riego (%):", font = ('Calibri',15,"italic"), fg = "#FFFFFF",bg="#38383A").place(x=15,y=340)
LaraNeta=Label(ventana, text ="LARA Neta (mm):", font = ('Calibri',15,"italic"), fg = "#FFFFFF",bg="#38383A").place(x=15,y=370)

Lamina=Label(ventana, text ="Lam (mm):", font = ('Calibri',15,"italic"), fg = "#FFFFFF",bg="#38383A").place(x=350,y=220)
aguaaprovechable=Label(ventana, text ="AA (%):", font = ('Calibri',15,"italic"), fg = "#FFFFFF",bg="#38383A").place(x=350,y=250)
Laa=Label(ventana, text ="LAA (mm):", font = ('Calibri',15,"italic"), fg = "#FFFFFF",bg="#38383A").place(x=350,y=280)
Lara=Label(ventana, text ="LARA (mm):", font = ('Calibri',15,"italic"), fg = "#FFFFFF",bg="#38383A").place(x=350,y=310)

#Entrada de variables
                                                    #width-> ancho, height->Altura, justify=comience a la derecha
EntradaPesoTotalHumedo=Entry(ventana,validate="key", validatecommand=(validatecommand, "%S"),font = ('Times New Roman',15),justify=CENTER,bg="#76EA3D",textvariable=pesohumedo).place(x=260, y=55, width=40, height=25)
EntradaPesoSeco=Entry(ventana,validate="key", validatecommand=(validatecommand, "%S"),font=('Times New Roman',15),justify=CENTER,bg="#76EA3D",textvariable=pesoseco).place(x=260, y=85, width=40, height=25)
EntradaPesoAgua=Entry(ventana,validate="key", validatecommand=(validatecommand, "%S"), font=('Times New Roman',15),justify=CENTER,bg="#F08C2D",textvariable=textopantallapesoAgua).place(x=260, y=115, width=40, height=25)
EntradaVolumenTotal=Entry(ventana,validate="key", validatecommand=(validatecommand, "%S"),font=('Times New Roman',15),justify=CENTER,bg="#76EA3D",textvariable=volumentotal).place(x=260, y=145, width=40, height=25)
EntradaPorosidad=Entry(ventana,validate="key", validatecommand=(validatecommand, "%S"),font=('Times New Roman',15),justify=CENTER,bg="#F08C2D",textvariable=textopantallaPorosidad).place(x=260, y=175, width=40, height=25)


EntradaDa=Entry(ventana,validate="key", validatecommand=(validatecommand, "%S"),font=('Times New Roman',15),justify=CENTER,bg="#F08C2D",textvariable=textopantallaDensidadReal).place(x=460, y=55, width=40, height=25)
EntradaDr=Entry(ventana,validate="key", validatecommand=(validatecommand, "%S"),font=('Times New Roman',15),justify=CENTER,bg="#76EA3D",textvariable=densidadreal).place(x=460, y=85, width=40, height=25)
Entradaw=Entry(ventana,validate="key", validatecommand=(validatecommand, "%S"), font=('Times New Roman',15),justify=CENTER,bg="#F08C2D",textvariable=textopantallaHumedadGravimetrica).place(x=460, y=115, width=40, height=25)
EntradaTetta=Entry(ventana,validate="key", validatecommand=(validatecommand, "%S"),font=('Times New Roman',15,),justify=CENTER,bg="#F08C2D",textvariable=textopantallaHumedadVolumetrica).place(x=460, y=145, width=40, height=25)

    #Segunda parte Entradas

EntradaProfundidad=Entry(ventana,validate="key", validatecommand=(validatecommand, "%S"),font = ('Times New Roman',15),justify=CENTER,bg="#76EA3D",textvariable=profundidadSuelo).place(x=260, y=220, width=40, height=25)
EntradaCC=Entry(ventana,validate="key", validatecommand=(validatecommand, "%S"),font = ('Times New Roman',15),justify=CENTER,bg="#76EA3D",textvariable=CC).place(x=260, y=250, width=40, height=25)
EntradaPMP=Entry(ventana,validate="key", validatecommand=(validatecommand, "%S"),font = ('Times New Roman',15),justify=CENTER,bg="#76EA3D",textvariable=PMP).place(x=260, y=280, width=40, height=25)
EntradaDPM=Entry(ventana,validate="key", validatecommand=(validatecommand, "%S"),font = ('Times New Roman',15),justify=CENTER,bg="#76EA3D",textvariable=DPM).place(x=260, y=310, width=40, height=25)
EntradaEficiencia=Entry(ventana,validate="key", validatecommand=(validatecommand, "%S"),font = ('Times New Roman',15),justify=CENTER,bg="#76EA3D",textvariable=eficienciaderiego).place(x=260, y=340, width=40, height=25)
EntradaLARANETA=Entry(ventana,validate="key", validatecommand=(validatecommand, "%S"),font=('Times New Roman',15),justify=CENTER,bg="#F08C2D",textvariable=textopantallaLARANETA).place(x=260, y=370, width=40, height=25)


EntradaLam=Entry(ventana,validate="key", validatecommand=(validatecommand, "%S"),font=('Times New Roman',15),justify=CENTER,bg="#F08C2D",textvariable=textopantallaLamina).place(x=460, y=220, width=40, height=25)
EntradaAA=Entry(ventana,validate="key", validatecommand=(validatecommand, "%S"),font=('Times New Roman',15),justify=CENTER,bg="#F08C2D",textvariable=textopantallaAA).place(x=460, y=250, width=40, height=25)
EntradaLAA=Entry(ventana,validate="key", validatecommand=(validatecommand, "%S"),font=('Times New Roman',15),justify=CENTER,bg="#F08C2D",textvariable=textopantallaLAA).place(x=460, y=280, width=40, height=25)
EntradaLARA=Entry(ventana,validate="key", validatecommand=(validatecommand, "%S"),font=('Times New Roman',15),justify=CENTER,bg="#F08C2D",textvariable=textopantallaLARA).place(x=460, y=310, width=40, height=25)


#Botones Calcular

BotonCalcular1=Button(ventana,command=calcular,text="Calcular",font=('Times New Roman',12,"italic","bold",),bg="#FFFFFF").place(x=350, y=175)
BotonLimpiar=Button(ventana,command=clear,text="Limpiar",font=('Times New Roman',12,"italic","bold",),bg="#FFFFFF").place(x=430, y=175)

    #Segunda parte

BotonCalcular2=Button(ventana,text="Calcular",command=calcular2,font=('Times New Roman',12,"italic","bold",),bg="#FFFFFF").place(x=350, y=350)
BotonLimpiar2=Button(ventana,text="Limpiar",command=clear2,font=('Times New Roman',12,"italic","bold",),bg="#FFFFFF").place(x=430, y=350)
BotonInformacion=Button(ventana,text="Info",command=informacion,font=('Times New Roman',12,"italic","bold",),bg="#81DAE8").place(x=430, y=390)

ventana.mainloop()














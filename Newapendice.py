# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 22:59:36 2021

@author: LUISA RODRIGUEZ
"""

from tkinter import ttk
from tkinter import *
import sqlite3 

k = """  ECUACIÓN EFICIENCIA DE SECADO: \n
           W * Δ||I
   nd =  -----------
         Ic * Ac * t
         
    Donde W = Masa de humedad evaporada (kg) en el tiempo t.
    Δ||I = Liente latente de evaporación del agua (a la temperatura del secador)(kJ kg-1)
    Ic = Insolación en la superficie del colector (W m −2 )
    Ac = Área del colector (m 2 )
    t = Tiempo
    
    POR FAVOR INGRESE LOS DATOS: """
    

m = """ 
        ECUACION EFICIENCIA DE ABSORCION : \n
       
                     Mo − Mt 
       np   =   ----------------
                V * ρ * t (has−hi)
        Donde Mo = Masa del producto en el tiempo t = o (kg)
        Mt = Masa del producto en el momento t (kg)
        V = Caudal de aire (m's −1 )
        ρ = Densidad del aire (kg m −3 )
        t = Tiempo de secado (s) 
        has = Humedad de saturacion adiabática
        hi = Humedad absoluta del aire
        
        POR FAVOR INGRESE LOS DATOS:  """
        
        
class Apendice:
    
    datos = 'BaseD.db' #esta base de datos ya debera estar creada en la misma carpeta que se aloja el codigo
    def __init__(self,ventana):
        """ Este metodo es el encargado de inicializar la ventana y a su vez de darle
            forma a la ventana principal """
        
        
        self.ventana = ventana
        self.ventana.title("Apendice5")

        #Creando Frame para agregar titulo
        frame = LabelFrame(self.ventana , text = "Bienvenido\n Seleciona una opcion." )
        frame.grid(row = 0 , column = 0, columnspan = 4, pady = 25 )
        
        self.secado = ttk.Button(frame, text = "Eficiencia de secado",
                                 command = self.calculo).grid(  row = 1, 
                                                                column = 0, 
                                                                columnspan = 2, 
                                                                sticky = W+E ) 

        self.captacion = ttk.Button(frame, text = "Eficiencia de captacion", 
                                    command = self.Ventana2).grid(  row = 2, 
                                                                    column = 0, 
                                                                    columnspan = 2, 
                                                                    sticky = W+E ) 
                                                                  
                                                        
        self.mensaje = Label(text = "" , fg = 'red')
        self.mensaje.grid(row = 3 , column = 0 , columnspan = 2 , sticky = W+E )
        #Tabla para observar valores
        self.tabla = ttk.Treeview(height = 12 , columns = 2 )
        self.tabla.grid(row = 4 , column = 0 , columnspan = 3 )
        self.tabla.heading("#0", text = "Resultado eficienciaC", anchor = CENTER)
        self.tabla.heading("#1", text = "Resultado eficienciaS", anchor = CENTER)
        ttk.Button(text = "BORRAR" , command = self.borrar).grid(row = 5 ,column=0, sticky = W+E ,columnspan = 4  )
        self.obtener()
        
        
    def conectar(self, consulta, parametro = ()):
        """Este metodo es el encargado de conectar la base de datos 
            recibe la consulta de que quiere hacer el usuario y los parametros"""
        with sqlite3.connect(self.datos) as connect :
            cursor = connect.cursor()
            resultado = cursor.execute(consulta , parametro)
            connect.commit()
        return resultado
    
    def obtener(self):
        j = self.tabla.get_children()
        for i in j:
            self.tabla.delete(i)
        consulta = 'SELECT * FROM Datos ORDER BY EficienciaS DESC'
        db = self.conectar(consulta)
        for j in db:
            self.tabla.insert('',0,text = j[1], values = j[2])

    def calculo(self):
        """"Este metodo es el encargado de poner en orden todas y cada una de las casillas y label donde 
            se ingresaran lo datos"""
        
        self.Cal = Toplevel()
        self.Cal.title("Ingresar Datos")
        Label(self.Cal , text = k ).grid(row = 0 , column = 0, columnspan = 4, pady = 15 )
         
        #Frames para ingresar valores
        # Masa de humedad
        Label(self.Cal , text = "W =" ).grid(row = 1 , column = 0 )
        self.W = Entry(self.Cal)
        self.W.grid(row = 1 , column = 1,sticky = W+E ) 

        #Latente Evaporacion.
        Label(self.Cal , text = "Δ||I =" ).grid(row = 2 , column = 0 )
        self.Latente = Entry(self.Cal)
        self.Latente.grid(row = 2 , column = 1,sticky = W+E )
        
        #Insolacion de la superficie
        Label(self.Cal , text = "Ic =" ).grid(row = 3 , column = 0 )
        self.Ic = Entry(self.Cal)
        self.Ic.grid(row = 3 , column = 1,sticky = W+E )
        
        #Area del coelctor
        Label(self.Cal , text = "Ac =" ).grid(row = 4 , column = 0 )
        self.Ac = Entry(self.Cal)
        self.Ac.grid(row = 4 , column = 1,sticky = W+E )
        
        #Tiempo
        Label(self.Cal , text = "t =" ).grid(row = 5  , column = 0 )
        self.Tiempo = Entry(self.Cal)
        self.Tiempo.grid(row = 5 , column = 1,sticky = W+E )
        
        #Resultado
        Resultado =  ttk.Button(self.Cal , text = "Resultado" , command = self.Calcular).grid(  row = 7, 
                                                                                           column = 1)
    def Calcular(self):
        """Este metodo es el encargado de hacer lo calculos de la ecuacion numero 1
            hace los calculos con los valores obtenidosen de los label """
        try:
            resultado1 = float(self.W.get()) * float(self.Latente.get()) 
            resultado2 = float(self.Ic.get()) * float(self.Ac.get()) * float(self.Tiempo.get())
            
            if resultado2 != float(0):
                q = resultado1/resultado2
                Label(self.Cal, text = f"El resultado es = {q}" ).grid(row = 9 , column = 1 ,sticky = W+E)
                
            elif resultado2 == float(0):
                Label(self.Cal, text = "No se puede hacer la division por cero" ).grid(row = 9 , column = 1 ,sticky = W+E)
           
            
        except:
          Label(self.Cal, text = "Haz digitado un valor erroneo " ).grid(row = 9 , column = 1 ,sticky = W+E)
           

        try:
            self.agregar(q)
        except:
            print("Ups algo anda mal :c..\ ")

    def agregar(self,X):    
            consulta = 'INSERT INTO Datos VALUES(NULL,?,?)'
            parametro = (X,"")
            self.conectar(consulta, parametro)
            print("Datos almacenados")
            
            
            
            """--------------------------------------------------------------------------------"""
        
    

    def Ventana2(self):
        """Este metodo es el encargado de crear todas y cada una de las casillas"""
        self.Vent = Toplevel()
        self.Vent.title("Ingresar Datos")
        Label(self.Vent , text = m ).grid(row = 0 , column = 0, columnspan = 4, pady = 15 )
         
        #Frames para ingresar valores
        # Masa de humedad
        Label(self.Vent , text = "Mo =" ).grid(row = 1 , column = 0 )
        self.masa0 = Entry(self.Vent)
        self.masa0.grid(row = 1 , column = 1,sticky = W+E ) 

        #Latente Evaporacion.
        Label(self.Vent , text = "Mt =" ).grid(row = 2 , column = 0 )
        self.masa1 = Entry(self.Vent)
        self.masa1.grid(row = 2 , column = 1,sticky = W+E )
        
        #Insolacion de la superficie
        Label(self.Vent , text = "V =" ).grid(row = 3 , column = 0 )
        self.caudal = Entry(self.Vent)
        self.caudal.grid(row = 3 , column = 1,sticky = W+E )
        
        #Area del coelctor
        Label(self.Vent , text = "ρ =" ).grid(row = 4 , column = 0 )
        self.densidad_Aire = Entry(self.Vent)
        self.densidad_Aire.grid(row = 4 , column = 1,sticky = W+E )
        
        #Tiempo
        Label(self.Vent , text = "t =" ).grid(row = 5  , column = 0 )
        self.Time = Entry(self.Vent)
        self.Time.grid(row = 5 , column = 1,sticky = W+E )
        
        Label(self.Vent , text = "has =" ).grid(row = 6  , column = 0 )
        self.has = Entry(self.Vent)
        self.has.grid(row = 6 , column = 1,sticky = W+E )
        
        
        Label(self.Vent , text = "hi =" ).grid(row = 7  , column = 0 )
        self.hi = Entry(self.Vent)
        self.hi.grid(row = 7 , column = 1,sticky = W+E )
        
        #Resultado
        Outcome =  ttk.Button(self.Vent , text = "Resultado" , command = self.Calculo2).grid(  row = 8, 
                                                                                              column = 1)
    def Calculo2(self):
        """ Este metodo se encarga de calcular los resultado de la segunda formula
            este metodo obtiene los numero de las casillas ingresads y a partir de eso 
            hace los multiples calculos"""
        
        try:
            resultado1 = float(self.masa0.get()) - float(self.masa1.get()) 
            resultado2 = float(self.caudal.get()) * float(self.densidad_Aire.get()) * float(self.Time.get()) * (float(self.has.get()) - float(self.hi.get()))
            if resultado2 != float(0):
                rf = resultado1/resultado2
                Label(self.Vent, text = f"El resultado es = {rf}" ).grid(row = 10 , column = 1 ,sticky = W+E)
                
            elif resultado2 == float(0):
                Label(self.Vent, text = "No se puede hacer la division por cero" ).grid(row = 10 , column = 1 ,sticky = W+E)
        except:
            Label(self.Vent, text = "Haz digitado un valor erroneo" ).grid(row = 10 , column = 1 ,sticky = W+E)            
        
        try:
            self.save(rf)
            
        except:
            print("Ups algo anda mal :c..\ ")

    def save(self,X):    
            consulta = 'INSERT INTO Datos VALUES(NULL,?,?)'
            parametro = ("",X)
            self.conectar(consulta, parametro)
            print("Datos almacenados")


    def borrar(self):
        """Este metodo se encarga de eliminar el ultimo indice de la base de datos 
            o el elemento que se seleccione"""
        try:
            self.tabla.item(self.tabla.selection())['text']
        except IndexError:
            return 
        
        name = self.tabla.item(self.tabla.selection())['text']
        consulta = 'DELETE FROM Datos WHERE EficienciaS = ?'
        self.conectar(consulta, (name, ))
        self.obtener()
                

if __name__ == '__main__':
    ventana = Tk()
    aplicacion = Apendice(ventana)
    ventana.mainloop()
from collections import defaultdict
from collections import Counter
from tkinter import filedialog
from datetime import datetime
from graphviz import Digraph, nohtml
#import funciones_js_css as css_js_fun
#import funciones_js as js_fun
#import funciones as css_fun
import webbrowser
import tkinter
import time
import os
import re

#-----------------------------XXXXXXXXXXXXXXX------XXXXXXXXXXXXXXXXX---XXXXX--XXXXXXX----------------------------------------------------
#-----------------------------XXXXXXXXXXXXXXXX-----XXXXXXXXXXXXXXXXX---XXXXXXXXXXXXXXXX--------------------------------------------------
#-----------------------------XXXXX-----XXXXXXX----------XXXXX---------XXXXXXXX---XXXXXX-------------------------------------------------
#-----------------------------XXXXX-------XXXXXX---------XXXXX---------XXXXXXX-----XXXXX-------------------------------------------------
#-----------------------------XXXXX---------XXXX---------XXXXX---------XXXXXX------------------------------------------------------------
#-----------------------------XXXXX-------XXXXXX---------XXXXX---------XXXXX-------------------------------------------------------------
#-----------------------------XXXXX-----XXXXXXX----------XXXXX---------XXXXX-------------------------------------------------------------
#-----------------------------XXXXXXXXXXXXXXXX-----XXXXXXXXXXXXXXXXX---XXXXX-------------------------------------------------------------
#-----------------------------XXXXXXXXXXXXXXX------XXXXXXXXXXXXXXXXX---XXXXX-------------------------------------------------------------

if os.path.isdir('Desktop/LFP_Proyecto2/'):
    print()
    print('Confirmando Existencia del Directorio')
    time.sleep(0.8)
    print('...................................................')
    time.sleep(1.2)
    print('                                     Ruta Existente')
    time.sleep(0.5)
    print('...................................................')
    time.sleep(0.8)
    print('Confirmando sub Rutas y Archivos')
    print('...................................................')
    time.sleep(0.8)
else:
    print()
    print('Confirmando Existencia del Directorio')
    time.sleep(0.8)
    print('...................................................')
    time.sleep(1.2)
    print('                                 Creando Directorio')
    time.sleep(1.5)
    print('                                 ..................')
    time.sleep(0.5)
    directorio_nuevo = 'Desktop/LFP_Proyecto2'
    os.mkdir(directorio_nuevo)
    time.sleep(1.2)
    print('                                  Directorio Creado')
    time.sleep(0.5)
    print('...................................................')
    time.sleep(0.8)
#---------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------
if os.path.isdir('Desktop/LFP_Proyecto2/css'):
        time.sleep(1.2)
        print('                       Carpeta de Estilos Existente')
        print('...................................................')
        time.sleep(0.5)
        print('Confirmando archivos de la Carpeta CSS')
        print('...................................................')
        time.sleep(0.8)   
else:
    time.sleep(1.2)
    print('                      Creando Directorio de Estilos')
    time.sleep(1.5)
    print('                      .............................')
    time.sleep(0.5)
    directorio_nuevo = 'Desktop/LFP_Proyecto2/css'
    os.mkdir(directorio_nuevo)
    time.sleep(1.2)
    print('                                  Directorio Creado')
    time.sleep(0.5)
    print('...................................................')
    time.sleep(0.8)

if os.path.isfile('Desktop/LFP_Proyecto2/css/flexslider.css'): #1
    time.sleep(0.5)
    print('                               FlexSlider Existente')
else:
    time.sleep(0.2)
    print('                        Creando Archivo FlexxSlider')
    time.sleep(0.5)
    css_fun.flexsilder()
if os.path.isfile('Desktop/LFP_Proyecto2/css/index.css'): #2
    time.sleep(0.5)
    print('                                    Index Existente')
else:
    time.sleep(0.2)
    print('                              Creando Archivo Index')
    time.sleep(0.5)
    css_fun.index()
if os.path.isfile('Desktop/LFP_Proyecto2/css/reset.css'): #3
    time.sleep(0.5)
    print('                                    Reset Existente')
else:
    time.sleep(0.2)
    print('                              Creando Archivo Reset')
    time.sleep(0.5)
    css_fun.reset_css()
if os.path.isfile('Desktop/LFP_Proyecto2/css/font-awesome.css'): #4
    time.sleep(0.5)
    print('                             Font Awesome Existente')
else:
    time.sleep(0.2)
    print('                       Creando Archivo Font Awesome')
    time.sleep(0.5)
    css_fun.font_awesome()
if os.path.isfile('Desktop/LFP_Proyecto2/css/jquery-ui.css'): #5
    time.sleep(0.5)
    print('                                JQuery-UI Existente')
else:
    time.sleep(0.2)
    print('                          Creando Archivo JQuery-UI')
    time.sleep(0.5)
    css_fun.jquery_ui()
if os.path.isfile('Desktop/LFP_Proyecto2/css/fuentes.css'): #6
    time.sleep(0.5)
    print('                                  Fuentes Existente')
else:
    time.sleep(0.2)
    print('                            Creando Archivo Fuentes')
    time.sleep(0.5)
    css_fun.fuentes()
time.sleep(1.2)
print('...................................................')
#---------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------
if os.path.isdir('Desktop/LFP_Proyecto2/js'):
        time.sleep(1.2)
        print('                               Carpeta JS Existente')
        print('...................................................')
        time.sleep(0.5)
        print('Confirmando archivos de la Carpeta JS')
        print('...................................................')
        time.sleep(0.8)   
else:
    time.sleep(1.2)
    print('                              Creando Directorio JS')
    time.sleep(1.5)
    directorio_nuevo = 'Desktop/LFP_Proyecto2/js'
    os.mkdir(directorio_nuevo)
    print('...................................................')
    time.sleep(1.2)
    print('                                  Directorio Creado')
    time.sleep(0.5)
    print('...................................................')
    time.sleep(0.8)
    
if os.path.isfile('Desktop/LFP_Proyecto2/js/flexslider.css'): #1
    time.sleep(0.5)
    print('                               FlexSlider Existente')
else:
    time.sleep(0.2)
    print('                        Creando Archivo FlexxSlider')
    time.sleep(0.5)
    css_js_fun.flexslider()
if os.path.isfile('Desktop/LFP_Proyecto2/js/jquery-ui.css'): #3
    time.sleep(0.5)
    print('                                JQuery-UI Existente')
else:
    time.sleep(0.2)
    print('                          Creando Archivo JQuery-UI')
    time.sleep(0.5)
    css_js_fun.jquery_ui()
if os.path.isfile('Desktop/LFP_Proyecto2/js/jquery.flexslider.js'): #8
    time.sleep(0.5)
    print('                        JQuery Flexslider Existente')
else:
    time.sleep(0.2)
    print('                  Creando Archivo JQuery Flexslider')
    time.sleep(0.5)
    js_fun.jquery_flexslider()
if os.path.isfile('Desktop/LFP_Proyecto2/js/main.js'): #9
    time.sleep(0.5)
    print('                                     Main Existente')
else:
    time.sleep(0.2)
    print('                               Creando Archivo Main')
    time.sleep(0.5)
    js_fun.main()
if os.path.isfile('Desktop/LFP_Proyecto2/js/prueba.js'): #10
    time.sleep(0.5)
    print('                                   Prueba Existente')
else:
    time.sleep(0.2)
    print('                             Creando Archivo Prueba')
    time.sleep(0.5)
    js_fun.prueba()
time.sleep(1.2)
print('...................................................')
#---------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------
if os.path.isdir('Desktop/LFP_Proyecto2/img'):
        time.sleep(1.2)
        print('                              Carpeta IMG Existente')
        time.sleep(0.5)
        print('...................................................')
        time.sleep(0.8)   
else:
    time.sleep(1.2)
    print('                             Creando Directorio IMG')
    time.sleep(1.5)
    directorio_nuevo = 'Desktop/LFP_Proyecto2/img'
    os.mkdir(directorio_nuevo)
    print('...................................................')
    time.sleep(1.2)
    print('                                  Directorio Creado')
    time.sleep(0.5)
    print('...................................................')
    time.sleep(0.8)

#------------------------------------XXXXXXXXXXXXXXXXXXXX----XXXXXX---------------------------------------------------------------
#------------------------------------XXXXXXXXXXXXXXXXXXXX----XXXXXX---------------------------------------------------------------
#------------------------------------XXXXXXXXXXXXXXXXXXXX----XXXXXX---------------------------------------------------------------
#------------------------------------XXXXX----------XXXXX----XXXXXX---------------------------------------------------------------
#------------------------------------XXXXX-------------------XXXXXX---------------------------------------------------------------
#------------------------------------XXXXX----------XXXXX----XXXXXX---------------------------------------------------------------
#------------------------------------XXXXXXXXXXXXXXXXXXXX----XXXXXXXXXXXXXXXXXXXX-------------------------------------------------
#------------------------------------XXXXXXXXXXXXXXXXXXXX----XXXXXXXXXXXXXXXXXXXX-------------------------------------------------
#------------------------------------XXXXXXXXXXXXXXXXXXXX----XXXXXXXXXXXXXXXXXXXX-------------------------------------------------

class gramatica():
    def __init__(self, N_Gramatica, Nombre, No_Terminales, Terminales, No_Terminal_Inicial, Producciones):
        self.N_Gramatica = N_Gramatica
        self.Nombre = Nombre
        self.No_Terminales = No_Terminales
        self.Terminales = Terminales
        self.No_Terminal_Inicial = No_Terminal_Inicial
        self.Producciones = Producciones
    def __str__(self):
        return self.Nombre
    def __str__(self):
        return self.N_Gramatica
    def __repr__(self):
        return str(self.__dict__)
    

class gramatica2():
    def __init__(self, N_Gramatica, Nombre, No_Terminales, Terminales, No_Terminal_Inicial, Producciones):
        self.N_Gramatica = N_Gramatica
        self.Nombre = Nombre
        self.No_Terminales = No_Terminales
        self.Terminales = Terminales
        self.No_Terminal_Inicial = No_Terminal_Inicial
        self.Producciones = Producciones
    def __str__(self):
        return self.Nombre
    def __str__(self):
        return self.N_Gramatica
    def __repr__(self):
        return str(self.__dict__)

#--------------------------XXXXXXXXXXXXXXXXXXXX---XXXXXXXXXXXXXXXXXXXX---XXXXXXXXXXXXXXXXXXXX-------------------------------------
#--------------------------XXXXXXXXXXXXXXXXXXXX---XXXXXXXXXXXXXXXXXXXX---XXXXXXXXXXXXXXXXXXXX-------------------------------------
#--------------------------XXXXXXXXXXXXXXXXXXXX---XXXXXXXXXXXXXXXXXXXX---XXXXXXXXXXXXXXXXXXXX-------------------------------------
#--------------------------XXXXX------------------XXXXX----------XXXXX---XXXXXX---------XXXXX-------------------------------------
#--------------------------XXXXX-----XXXXXXXXXX---XXXXX----------XXXXX---XXXXXX---------XXXXX-------------------------------------
#--------------------------XXXXX----------XXXXX---XXXXXXXXXXXXXXXXXXXX---XXXXXXXXXXXXXXXXXXXX-------------------------------------
#--------------------------XXXXXXXXXXXXXXXXXXXX---XXXXXXXXXXXXXXXXXXXX---XXXXXXXXXXXXXXXXXXXX-------------------------------------
#--------------------------XXXXXXXXXXXXXXXXXXXX---XXXXX-------XXXXXX-----XXXXXX---------XXXXX-------------------------------------
#--------------------------XXXXXXXXXXXXXXXXXXXX---XXXXX--------XXXXXXX---XXXXXX---------XXXXX-------------------------------------

class Gra():
    __abc = [] #alfabeto
    __pila = [] #pila
    __terminales = [] #terminales
    __noterminales = [] #no terminales
    __inicial = [] #no terminal inicial
    __acept = [] #aceptacion
    __error = False #error
    __cont = 0 #contador
    
    def __init__(self, no, nombre, terminales, no_terminales, inicial, pila, aceptacion):
        self.__numero = no
        self.__nombre = nombre
        self.__terminales = terminales
        self.__noterminales = no_terminales
        self.__inicial = inicial
        self.__pila = pila
        self.__aceptacion = aceptacion
        
    def __pertenece(self, c):
        print()
        



        
#---------------------XXXXXXXXXXXXXX---XXXXXXXXXXXXXX---XXXXXXXXXXXXXXXXX---XXXXXXXXXXXXXXXXXXXX----------------------------------
#---------------------XXXXXXXXXXXXXX---XXXXXXXXXXXXXX---XXXXXXXXXXXXXXXXX---XXXXXXXXXXXXXXXXXXXX----------------------------------
#---------------------XXXX-------XXX---XXX--------XXX---XXX-----------XXX---XXX---------------------------------------------------
#---------------------XXXX-------XXX---XXX--------XXX---XXX-----------XXX---XXX---------------------------------------------------
#---------------------XXXXXXXXXXXXXX---XXXXXXXXXXXXXX---XXX-----------XXX---XXX----XXXXXXXXXXXXX----------------------------------
#---------------------XXXXXXXXXXXXXX---XXXXXXXXXXXXXX---XXX-----------XXX---XXX----XXXXXXXXXXXXX----------------------------------
#---------------------XXXX-------------XXX----XXX-------XXX-----------XXX---XXX----XXX-------XXX----------------------------------
#---------------------XXXX-------------XXX------XXX-----XXXXXXXXXXXXXXXXX---XXXXXXXXXXXXXXXXXXXX----------------------------------
#---------------------XXXX-------------XXX--------XXX---XXXXXXXXXXXXXXXXX---XXXXXXXXXXXXXXXXXXXX----------------------------------

class Inicio():
    
    def __init__(self):
        self.gr_as = []
        self.gramatica_semi = []
        self.esta_gramatica = False
        self.contenido_archivo = []
    
#-------------------------XXXXXXXXXXXXXXXXXXXX----------------XXXXXXXXXXXXXXXXXXXX-------------------------------------------------
#-------------------------XXXXXXXXXXXXXXXXXXXX----------------XXXXXXXXXXXXXXXXXXXX-------------------------------------------------
#-------------------------XXXXXXXXXXXXXXXXXXXX----------------XXXXXXXXXXXXXXXXXXXX-------------------------------------------------
#-------------------------XXXXX----------XXXXX----XXXXXXXXX---XXXXXX---------XXXXX-------------------------------------------------
#-------------------------XXXXX-------------------XXXXXXXXX---XXXXXX---------XXXXX-------------------------------------------------
#-------------------------XXXXX----------XXXXX----XXXXXXXXX---XXXXXXXXXXXXXXXXXXXX-------------------------------------------------
#-------------------------XXXXXXXXXXXXXXXXXXXX----------------XXXXXXXXXXXXXXXXXXXX-------------------------------------------------
#-------------------------XXXXXXXXXXXXXXXXXXXX----------------XXXXXX---------XXXXX-------------------------------------------------
#-------------------------XXXXXXXXXXXXXXXXXXXX----------------XXXXXX---------XXXXX-------------------------------------------------
    
    def cargar_archivo(self):
        print('Cargando Archivo')
        time.sleep(0.5)
        print('.  .  .  .  .  .')
        time.sleep(0.5)
        root = tkinter.Tk()
        ruta = filedialog.askopenfilename(title = "GLC: ", filetypes = (("GLC File", "*.glc"),("all files","*.*")))
        if ruta != None:
            self.esta_gramatica = True
            archivo_contenido = open(ruta, 'r', encoding='utf-8')
            #texto = archivo_contenido.read()
            texto = archivo_contenido.readlines()
            self.contenido_archivo = texto
            archivo_contenido.close()
            print('Ruta del Archivo:', ruta)
            time.sleep(1.5)
            #print(ruta)
            #print()
            #print(texto)
            root.destroy() #Cerrar ventana
            #print(texto)
            filas = 0
            kr = []
            gla = []
            numero = 0
            #print(texto)
            #------------------------ Eliminarion Espacios / Saltos de Linea ------------------------
            for i in range(len(texto)):
                texto[i] = texto[i].strip(' ')
                texto[i] = texto[i].strip('\n')
                texto[i] = texto[i].strip(' ')
                #print(texto[i]) #Muestra toda la gramatica
            #------------------- FIN **/** Eliminarion Espacios / Saltos de Linea -------------------
            #------------------------ Separar Terminales de No Terminales :v ------------------------
            #print(texto)
                if filas == 0:
                    titulo = texto[i]
                elif filas == 1:
                    kr_producciones = texto[i].split(';')
                    #print('producciones:' ,kr_producciones)
                    kr_nterminales = kr_producciones[0]
                    #print('no terminales:', kr_nterminales)
                    kr_terminales = kr_producciones[1]
                    #print('terminales:', kr_terminales)
                    kr_inicio = kr_producciones[2]
                    #print('simbolo inicial:', kr_inicio)
                elif filas > 1:
                    if texto[i] != '*':
                        kr.append(texto[i])
                    else:
                        #gramatica_nueva = gramatica(gr_nombre, gr_nterminal, gr_terminal, gr_titulo, gr_producciones, gr_gramatica)
                        gramatica_nueva = gramatica(numero, titulo, kr_nterminales, kr_terminales, kr_inicio, kr)
                        kr = []
                        self.gr_as.append(gramatica_nueva)
                        filas = -1
                        numero += 1
                filas += 1
                
            #print(self.gr_as)
            #print(self.contenido_archivo)
            print('Archivo Cargado con Exito')
            time.sleep(0.5)
            self.composicion_automata()
            #---------------------- FIN Separar Terminales de No Terminales :v ----------------------
            
            
            
            '''
            lete = texto.split('*')
            for i in lete:
                kr.append(i.split('\n'))
            #------------------------ Eliminarion Espacios / Saltos de Linea ------------------------
            posiciones = []
            can = len(kr)-1
            kr.pop(can)
            for i in range(len(kr)):
                for j in range(len(kr[i])):
                    if kr[i][j] == '':
                        posiciones.append([i,j])
            kr[0].pop(len(kr[0])-1)
            kr_in = 1
            for i in range(kr_in, len(kr)):
                kr[i].pop(0)
                kr[i].pop(-1)
            #------------------- FIN **/** Eliminarion Espacios / Saltos de Linea -------------------
            #------------------------ Separar Terminales de No Terminales :v ------------------------
            for i in range(len(kr)):
                kr[i][1] = kr[i][1].split(';')
                #kr[i][1][0] = kr[i][1][0].split(',')
                #kr[i][1][1] = kr[i][1][1].split(',')
            #---------------------- FIN Separar Terminales de No Terminales :v ----------------------
            #--------------------------------- Separar Producciones ---------------------------------
            for i in range(len(kr)):
                for k in range(2, len(kr[i])):
                    kr[i][k] = kr[i][k].split('->')
            #------------------------------- Fin Separar Producciones -------------------------------
            # Enviar a Variable Global -------------
            self.gramatica_semi = kr
        
            #print('Posiciones: ', posiciones)
            #print(kr[0][1][2]) #Posicion en donde se encuentra la No Terminal Inicial (inicia todo / se subdibide)
            #print(kr[0][1][0][0]) #Posicion en donde se encuetra una terminal gramatica 1
            #print(can) #cantidad
            #print(kr)
            '''
        else:
            self.esta_gramatica = False
            print("Gramatica no Cargada >:v")
        
        
#-------------------------XXXXXXXXXXXXXXXXXXXX----------------XXXXXXXXXXXXXXXXXXXX------------------------------------------------
#-------------------------XXXXXXXXXXXXXXXXXXXX----------------XXXXXXXXXXXXXXXXXXXX------------------------------------------------
#-------------------------XXXXXXXXXXXXXXXXXXXX----------------XXXXXXXXXXXXXXXXXXXX------------------------------------------------
#--------------------------------XXXXXX----------XXXXXXXXXX---XXXXX---------------------------------------------------------------
#--------------------------------XXXXXX----------XXXXXXXXXX---XXXXX-----XXXXXXXXXX------------------------------------------------
#--------------------------------XXXXXX----------XXXXXXXXXX---XXXXX----------XXXXX------------------------------------------------
#-------------------------XXXXXXXXXXXXXXXXXXXX----------------XXXXXXXXXXXXXXXXXXXX------------------------------------------------
#-------------------------XXXXXXXXXXXXXXXXXXXX----------------XXXXXXXXXXXXXXXXXXXX------------------------------------------------
#-------------------------XXXXXXXXXXXXXXXXXXXX----------------XXXXXXXXXXXXXXXXXXXX------------------------------------------------

    def info_gramatica(self, gramatica_seleccionada):
        contador = 0
        for i in self.gr_as:
            if i.N_Gramatica == gramatica_seleccionada:
                time.sleep(0.5)
                print('................................................................')
                print('................................................................')
                print('                  §♦§ Gramatica Seleccionada §♦§                  ')
                print('................................................................')
                print('................................................................')
                time.sleep(0.2)
                print('Nombre de la Gramatica §(T2)§: ', i.Nombre)
                time.sleep(0.2)
                print('No Terminales: {',i.No_Terminales,'}')
                time.sleep(0.2)
                print('Terminales: {',i.Terminales,'}')
                time.sleep(0.2)
                print('No Terminal Inicial: {',i.No_Terminal_Inicial,'}')
                time.sleep(0.2)
                print('Producciones:')
                con = 0
                for k in i.Producciones:
                    time.sleep(0.2)
                    print('  {§',con,'§}',k)
                    con += 1
            
    def nombre_gramatica(self):
        if self.esta_gramatica == True:
            print('Gramaticas Obtenidas')
            contador = 0
            for i in self.gr_as:
                time.sleep(0.5)
                print('{§',i.N_Gramatica,'§} '+ i.Nombre)
                #contador += 1
            gramatica_a_elegir = int(input("Ingrese el Numero de la Gramatica para ver su Informacion: "))
            #print(gramatica_a_elegir)
            gram = self.info_gramatica(gramatica_a_elegir)
        else:
            print("Opcion no Valida >:v (Gramatica no subida)")
    
#-------------------------XXXXXXXXXXXXXXXXXXXX----------------XXXXXXXXXXXXXXXXXXXX------------------------------------------------
#-------------------------XXXXXXXXXXXXXXXXXXXX----------------XXXXXXXXXXXXXXXXXXXX------------------------------------------------
#-------------------------XXXXXXXXXXXXXXXXXXXX----------------XXXXXXXXXXXXXXXXXXXX------------------------------------------------
#-------------------------XXXXX------------------XXXXXXXXXX---XXXXXX---------XXXXX------------------------------------------------
#-------------------------XXXXX-----XXXXXXXXXX---XXXXXXXXXX---XXXXXX---------XXXXX------------------------------------------------
#-------------------------XXXXX----------XXXXX---XXXXXXXXXX---XXXXXXXXXXXXXXXXXXXX------------------------------------------------
#-------------------------XXXXXXXXXXXXXXXXXXXX----------------XXXXXXXXXXXXXXXXXXXX------------------------------------------------
#-------------------------XXXXXXXXXXXXXXXXXXXX----------------XXXXXX---------XXXXX------------------------------------------------
#-------------------------XXXXXXXXXXXXXXXXXXXX----------------XXXXXX---------XXXXX------------------------------------------------  
    
    def composicion_automata(self):
        filas = 0
        kr = []
        numero = 0
        #print(texto)
        #------------------------ Eliminarion Espacios / Saltos de Linea ------------------------
        for i in range(len(self.contenido_archivo)):
            self.contenido_archivo[i] = self.contenido_archivo[i].strip(' ')
            self.contenido_archivo[i] = self.contenido_archivo[i].strip('\n')
            self.contenido_archivo[i] = self.contenido_archivo[i].strip(' ')
            #print(texto[i]) #Muestra toda la gramatica
        #------------------- FIN **/** Eliminarion Espacios / Saltos de Linea -------------------
        #------------------------ Separar Terminales de No Terminales :v ------------------------
        #print(texto)
            if filas == 0:
                titulo = self.contenido_archivo[i]
            elif filas == 1:
                kr_producciones = self.contenido_archivo[i].split(';')
                #print('producciones:' ,kr_producciones)
                kr_nterminales = kr_producciones[0].split(',')
                #print('no terminales:', kr_nterminales)
                kr_terminales = kr_producciones[1].split(',')
                #print('terminales:', kr_terminales)
                kr_inicio = kr_producciones[2]
                #print('simbolo inicial:', kr_inicio)
            elif filas > 1:
                if self.contenido_archivo[i] != '*':
                    kr.append(self.contenido_archivo[i])
                else:
                    #gramatica_nueva = gramatica(gr_nombre, gr_nterminal, gr_terminal, gr_titulo, gr_producciones, gr_gramatica)
                    gramatica_nueva = gramatica2(numero, titulo, kr_nterminales, kr_terminales, kr_inicio, kr)
                    kr = []
                    self.gramatica_semi.append(gramatica_nueva)
                    filas = -1
                    numero += 1
            filas += 1
        #print(self.gramatica_semi)
        #print(self.contenido_archivo)
        #print('Archivo Cargado con Exito')
        #time.sleep(0.5)
        #---------------------- FIN Separar Terminales de No Terminales :v ----------------------
        
    def pagina_gramatica_generada(self, gramatica_seleccionada):
        print('Generando Automata de Pila Equivalente :v')
        time.sleep(1.2)
        for i in self.gr_as:
            if i.N_Gramatica == gramatica_seleccionada:
                pa = open('Grafo_Generado.html', 'w')
                mensaje = '''<!DOCTYPE html>
<html lang="en">
<head>
<link rel="icon" href="https://es.seaicons.com/wp-content/uploads/2016/06/NFSShift-logo-2-icon.png">
	<meta charset="UTF-8">
	<link rel="stylesheet" type="text/css" href="css/index.css">
	<link rel="stylesheet" href="css/flexslider.css">
	<link rel="stylesheet" href="css/font-awesome.css">
	<link rel="stylesheet" href="js/jquery-ui.css">
	<script src="https://code.jquery.com/jquery-3.1.0.min.js"></script>
	<script src="js/jquery.flexslider.js"></script>
	<script src="js/main.js"></script>
	<script src="http://code.jquery.com/ui/1.12.1/jquery-ui.js"></script>
	<script>
		$( function() {
    	$( "#grupoTablas" ).tabs();
		} );
	</script>
	<title>Gramatica |o| '''
                mensaje += i.Nombre
                mensaje +='''</title>
</head>
<body>
		<header>
			<div id="subheader">
				<div id="logotipo"><p><a href=""><i>Reporte LFP</i></a></p></div>
				<nav>
					<ul class="menu cf">
						<li><a href="">Aplicaci&oacute;n desarrollada por: </a>
							<ul class="submenu">
								
							</ul>
						</li>
						<li><a href="">Alumno</a>
							<ul class="submenu2">
								
							</ul>
						</li>
					</ul>
				</nav>
			</div>
		</header>
		<section id="wrap">
			<section id="main">
				<section id="slideshow">
					<div class="slides_container">
						<div class="flexslider">
							<ul class="slides">
								<li>
									<img src="https://i.redd.it/tgp7noky54u61.png" alt="">
									<section class="caption">
										<h2></h2>
									</section>
								</li>
								<li>
									<img src="https://i.redd.it/a47ad3convt61.jpg" alt="">
									<section class="caption">
										<h2></h2>
									</section>
								</li>
								<li>
									<img src="https://i.pinimg.com/originals/41/75/c9/4175c9ecc33d57cb4f3404725cd441e0.jpg" alt="">
										<section class="caption">
											<h2></h2>
										</section>
								</li>
							</ul>
						</div>
					</div>
				</section>
				<section id="bienvenidos">
					<article>
						<hgroup><h3>&nbsp;&nbsp;&nbsp;Gram&aacute;tica Seleccionada</h3></hgroup>
					</article>
					<article>
						<p>
							<ul>
							  <div id="grupoTablas">
  									<ul>
   										<li><a href="#tab-1">Texto</a></li>
    									<li><a href="#tab-2">Imagen</a></li>
    									<li><a href="#tab-3">Texto + Imagen</a></li>	
  									</ul>
  									<div id="tab-1">
    									<h3>Gram&aacute;tica <strong>'''
                mensaje += i.Nombre
                mensaje +='''</strong></h3>
    								<ul>
   										<li><a href="#tab-1">Nombre: '''
                mensaje += i.Nombre
                mensaje +='''</a></li>
    									<li><a href="#tab-1">No Terminales: {  '''
                mensaje += i.No_Terminales
                mensaje +=  '''  }</a></li>
    									<li><a href="#tab-1">Terminales: {  '''
                mensaje += i.Terminales
                mensaje +=  '''  }</a></li>
    									<li><a href="#tab-1">No Terminal Inicial: {  '''
                mensaje += i.No_Terminal_Inicial
                mensaje +=  '''  }</a></li>
    									<li><a href="#tab-1">Estados: { i, p, q, F }</a></li>
                                        <li><a href="#tab-1">Estado Inicial: { i }</a></li>
                                        <li><a href="#tab-1">Estado Final: { F }</a></li></ul>
  									</div>
  									<div id="tab-2">
    									<h3>Gram&aacute;tica <strong>'''
                mensaje += i.Nombre
                mensaje +='''</strong></h3>
    								<ul>
   										<li><a href="#tab-2"></a></li>
    									<li><a href="#tab-2"></a></li>
    									<li><a href="#tab-2"></a></li>
    									<li><a href="#tab-2"></a></li>
  									</ul>
   										<img class="ima" src="Grafo_Generado.svg"/>
  									</div>
  									<div id="tab-3">
    									<h3>Gram&aacute;tica <strong>'''
                mensaje += i.Nombre
                mensaje +=''' </strong>+ Imagen</h3>
    								<ul>
   										<li><a href="#tab-3">Nombre: '''
                mensaje += i.Nombre
                mensaje +='''</a></li>
    									<li><a href="#tab-3">No Terminales: {  '''
                mensaje += i.No_Terminales
                mensaje +=  '''  }</a></li>
    									<li><a href="#tab-3">Terminales: {  '''
                mensaje += i.Terminales
                mensaje +=  '''  }</a></li>
    									<li><a href="#tab-3">No Terminal Inicial: {  '''
                mensaje += i.No_Terminal_Inicial
                mensaje +=  '''  }</a></li>
    									<li><a href="#tab-3">Estados: { i, p, q, F }</a></li>
                                        <li><a href="#tab-3">Estado Inicial: { i }</a></li>
                                        <li><a href="#tab-3">Estado Final: { F }</a></li>
                                    </ul>
                                        <img class="ima" src="Grafo_Generado.svg"/>
                                    </div>
								</div>
							</ul>
						</p>
					</article>
				</section>
            <footer>
				<section id="acerca-de">
					<article>
						<hgroup><h3>Proyecto 2 Primer Semestre 2021</h3></hgroup>
						<p> </p>
					</article>
				</section>
			</footer>
			<div id="copyright"><p>SRT CC 2021 -- Carne</p></div>
		</section>
	</body>
</html>'''
                pa.write(mensaje)
                pa.close()
                print('Automata de Pila Generado c:')
                time.sleep(1.2)
                os.startfile('Grafo_Generado.html')
        
    def generacion_automata(self, gramatica_seleccionada):
        for i in self.gramatica_semi:
            if i.N_Gramatica == gramatica_seleccionada:
                f = 'digraph Grafica{\n'
                f += 'rankdir=LR;node[shape=circle color=red fontcolor=blue fontsize=20 penwidth=1.5];q[width=.8 penwidth=1.8]\n'
                f += 'i->p[label="&lambda;,&lambda;,#" penwidth=1.5 color=gray fontcolor=blue fontsize=18]\n'
                f += 'p->q[label="&lambda;,&lambda;,'+i.No_Terminal_Inicial+'" penwidth=1.5 color=gray fontcolor=blue fontsize=18]\n'
                t = i.Terminales
                p = i.Producciones
                obtener_terminales = ''
                obtener_producciones = ''
                for k in t:
                    obtener_terminales += k+','+k+','+'&lambda;<BR/>' 
                for m in p:
                    quite = m.split('->')
                    obtener_producciones += '&lambda;,'+quite[0]+','+quite[1]+'<BR/>'
                f += 'q:n->q:n[label=<'+obtener_producciones+'>];\n'
                f += 'q:s->q:s[label=<'+obtener_terminales+'>];\n'
                f += 'q->F[label="#,#,&lambda;" penwidth=1.5 color=gray fontcolor=blue fontsize=18]\n'
                f += 'title[fontsize=20 label="Nombre:'+i.Nombre+'" shape=none fontcolor=blue color=gray]\n'
                f += '}'
                archivo = open('Grafo_Generado.gv', 'w')
                archivo.write(f)
                archivo.close()
                conversion = 'dot -Tsvg Grafo_Generado.gv -o Grafo_Generado.svg'
                os.system(conversion)
                self.pagina_gramatica_generada(gramatica_seleccionada)
                #----------------------------------------------------------------------------------------
  
    def nombre_generacion_automata(self):
        if self.esta_gramatica == True:
            print('Gramaticas Obtenidas')
            contador = 0
            for i in self.gr_as:
                time.sleep(0.5)
                print('{§',i.N_Gramatica,'§} '+ i.Nombre)
                #contador += 1
            gramatica_a_elegir = int(input("Ingrese el Numero de la Gramatica para ver su Informacion: "))
            #print(gramatica_a_elegir)
            gram = self.generacion_automata(gramatica_a_elegir)
        else:
            print("Opcion no Valida >:v (Gramatica no subida)")
        
#-------------------------XXXXX--XXXXXXXXXXX------------------XXXXX--XXXXXXXXXXX--------------------------------------------------
#-------------------------XXXXXXXXXXXXXXXXXXXX----------------XXXXXXXXXXXXXXXXXXXX------------------------------------------------
#-------------------------XXXXXXXXXXXXXXXXXXXX----------------XXXXXXXXXXXXXXXXXXXX------------------------------------------------
#-------------------------XXXXXXX--------XXXXX---XXXXXXXXXX---XXXXXXX--------XXXXX------------------------------------------------
#-------------------------XXXXXX-----------------XXXXXXXXXX---XXXXXX--------------------------------------------------------------
#-------------------------XXXXX------------------XXXXXXXXXX---XXXXX---------------------------------------------------------------
#-------------------------XXXXX-------------------------------XXXXX---------------------------------------------------------------
#-------------------------XXXXX-------------------------------XXXXX---------------------------------------------------------------
#-------------------------XXXXX-------------------------------XXXXX---------------------------------------------------------------
    
    def reporte_recorrido(self, gramatica):
        print()
        
    def nombre_gram_reporte(self):
        if self.esta_gramatica == True:
            print('Gramaticas Obtenidas')
            contador = 0
            for i in self.gr_as:
                time.sleep(0.5)
                print('{§',i.N_Gramatica,'§} '+ i.Nombre)
                #contador += 1
            gramatica_a_elegir = int(input("Ingrese el Numero de la Gramatica para ver su Informacion: "))
            #print(gramatica_a_elegir)
            gram = self.reporte_recorrido(gramatica_a_elegir)
        else:
            print("Opcion no Valida >:v (Gramatica no subida)")
        
#-------------------------XXXXX--XXXXXXXXXXX------------------XXXXXXXXXXXXXXXXXXXX------------------------------------------------
#-------------------------XXXXXXXXXXXXXXXXXXXX----------------XXXXXXXXXXXXXXXXXXXX------------------------------------------------
#-------------------------XXXXXXXXXXXXXXXXXXXX----------------XXXXXXXXXXXXXXXXXXXX------------------------------------------------
#-------------------------XXXXXXX--------XXXXX---XXXXXXXXXX----------XXXXXX-------------------------------------------------------
#-------------------------XXXXXX-----------------XXXXXXXXXX----------XXXXXX-------------------------------------------------------
#-------------------------XXXXX------------------XXXXXXXXXX----------XXXXXX-------------------------------------------------------
#-------------------------XXXXX--------------------------------------XXXXXX-------------------------------------------------------
#-------------------------XXXXX--------------------------------------XXXXXX-------------------------------------------------------
#-------------------------XXXXX--------------------------------------XXXXXX-------------------------------------------------------
    
    def reporte_en_tabla(self, gramatica):
        print()
    
    def nombre_reporte_tabla(self):
        if self.esta_gramatica == True:
            print('Gramaticas Obtenidas')
            contador = 0
            for i in self.gr_as:
                time.sleep(0.5)
                print('{§',i.N_Gramatica,'§} '+ i.Nombre)
                #contador += 1
            gramatica_a_elegir = int(input("Ingrese el Numero de la Gramatica para ver su Informacion: "))
            #print(gramatica_a_elegir)
            gram = self.reporte_en_tabla(gramatica_a_elegir)
        else:
            print("Opcion no Valida >:v (Gramatica no subida)")
    
#-------------------------XXXXXXXXXXXXXXXXX-------------------XXXXXXXXXXXXXXXXXXX-------------------------------------------------
#-------------------------XXXXXXXXXXXXXXXXXX------------------XXXXXXXXXXXXXXXXXXX-------------------------------------------------
#-------------------------XXXXXXXXXXXXXXXXXXXX----------------XXXXXX-------XXXXXX-------------------------------------------------
#-------------------------XXXXXX--------XXXXXX---XXXXXXXXXX---XXXXXX-------XXXXXX-------------------------------------------------
#-------------------------XXXXXX--------XXXXXX---XXXXXXXXXX---XXXXXXXXXXXXXXXXXXX-------------------------------------------------
#-------------------------XXXXXX--------XXXXXX---XXXXXXXXXX---XXXXXXXXXXXXXXXXXXX-------------------------------------------------
#-------------------------XXXXXXXXXXXXXXXXXXXX----------------XXXXXX--------------------------------------------------------------
#-------------------------XXXXXXXXXXXXXXXXXX------------------XXXXXX--------------------------------------------------------------
#-------------------------XXXXXXXXXXXXXXXXX-------------------XXXXXX--------------------------------------------------------------

    def datos_personales(self):
        print('------------------------------------------')
        print('------------ Datos Personales ------------')
        print('------------------------------------------')
        print()
        print("Universidad de San Carlos de Guatemala")
        print("------------------ Facultad de Ingenieria")
        print("------- Ingenieria en Ciencias & Sistemas")
        print("Lab. Lenguajes Formales & de Programacion")
        print("Seccion: --------------------------->  A-")
        print("Alumno")
        print("Carne")
        print()
        print('------------------------------------------')
    
#-------------------------XXXXXXXX-----------XXXXXXXX----------------XXXXXXXXXXXXXXXXXXX-------------------------------------------------
#-------------------------XXXXXXXXX---------XXXXXXXXX----------------XXXXXXXXXXXXXXXXXXX-------------------------------------------------
#-------------------------XXXXXXXXXX-------XXXXXXXXXX----------------XXXXXX-------XXXXXX-------------------------------------------------
#-------------------------XXXXXXXXXXXX---XXXXXXXXXXXX---XXXXXXXXXX---XXXXXX-------XXXXXX-------------------------------------------------
#-------------------------XXXXXX-----XXXXX-----XXXXXX---XXXXXXXXXX---XXXXXXXXXXXXXXXXXXX-------------------------------------------------
#-------------------------XXXXXX-----XXXXX-----XXXXXX---XXXXXXXXXX---XXXXXXXXXXXXXXXXXXX-------------------------------------------------
#-------------------------XXXXXX-----XXXXX-----XXXXXX----------------XXXXXX--------------------------------------------------------------
#-------------------------XXXXXX-----XXXXX-----XXXXXX----------------XXXXXX--------------------------------------------------------------
#-------------------------XXXXXX-----XXXXX-----XXXXXX----------------XXXXXX--------------------------------------------------------------    
    
    def menu_principal(self):
        salir = False
        while salir == False:
            print("------------------- Menu Inicial -------------------")
            print("1. Cargar Archivo")
            print("2. Mostrar Informacion de la Gramatica")
            print("3. Generar Automata de Pila Equivalente")
            print("4. Reporte Recorrido")
            print("5. Reporte en Tabla")
            print("6. Salir")
            option = int(input("Ingresar Opcion: "))
            if option == 1:
                self.cargar_archivo()
            elif option == 2:
                self.nombre_gramatica()
            elif option == 3:
                self.nombre_generacion_automata()
            elif option == 4:
                self.nombre_gram_reporte()
            elif option == 5:
                self.nombre_reporte_tabla()
            elif option == 6:
                self.datos_personales()
                salir = True
            else:
                print("Syntax Error  --  Saliendo del Programa")
                exit()

empezar = Inicio()
empezar.menu_principal()
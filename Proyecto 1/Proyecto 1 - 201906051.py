from collections import defaultdict
from collections import Counter
from tkinter import filedialog
from datetime import datetime
from graphviz import Digraph
import webbrowser
import tkinter
import time
import os
import re

Titulo = ''
lista_errores_codigo = []
lectura_texto_menu = []#Obtine la lista principal al leer el archivo de menu
lectura_texto_factura = []#obtiene la lista principal al tener el archivo de factura
lista_token_codigo = []
menu_existente = False
objeto_completo = []
objeto_menu = []
objeto_factura = []
objeto_obtener_factura = []
salida_factura = ''
lista_receta = []
lista_objeto_receta = []
lista_c = []
factura_valida = True
salida = ''
Titulo_limpio = []
Nombre_Recetas = []
Recetas_Obtenidas = []

#------XXXXXXXXXXXXXXXXX------------------XXXXXXEEEEEEEEEE---XXXXXX--XXXXXX-------XXXXXX--XXXXXX-------------------------------------------
#------XXXXXXXXXXXXXXXXX------------------XXXXXXEEEEEEEEEE---XXXXXXXXXXXXXXXX-----XXXXXXXXXXXXXXXX-----------------------------------------
#------XXXXXX------XXXXX------------------XXXXXX-------------XXXXXXXXXXXXXXXXXX---XXXXXXXXXXXXXXXXXX---------------------------------------
#------XXXXXX------XXXXX---XXXXXXXXXXXX---XXXXXXEEEEEEE------XXXXXXXX------XXXX---XXXXXXXX------XXXX---------------------------------------
#------XXXXXXXXXXXXXXXXX---XXXXXXXXXXXX---XXXXXXEEEEEEE------XXXXXX----------XX---XXXXXX----------XX---------------------------------------
#------XXXXXXXXXXXXXXXXX---XXXXXXXXXXXX---XXXXXXEEEEEEE------XXXXXX---------------XXXXXX---------------------------------------------------
#------XXXXXX-----------------------------XXXXXX-------------XXXXXX---------------XXXXXX---------------------------------------------------
#------XXXXXX-----------------------------XXXXXXEEEEEEEEEE---XXXXXX---------------XXXXXX---------------------------------------------------
#------XXXXXX-----------------------------XXXXXXEEEEEEEEEE---XXXXXX---------------XXXXXX---------------------------------------------------
def pagina_errores():
    if factura_valida == True:
        print('Creando Tabla de Errores')
        time.sleep(0.5)
        print('.    .     ..     .    .')
        time.sleep(0.5)
        f = open('Desktop\C.201906051_Proyecto1\Errores.html', 'w')
        mensaje = '''<!DOCTYPE html>
        <html lang="en"><head><title>Errores - Proyecto 1</title><link rel="icon" href="https://es.seaicons.com/wp-content/uploads/2016/06/NFSShift-logo-2-icon.png">
        <style>
        body{background-image: url("https://elandroidelibre.elespanol.com/wp-content/uploads/2020/10/Fondos-pantalla-Huawei-Mate-40-10.jpg");background-repeat:no-repeat;background-attachment: fixed;} 
        h1{text-align:center; color: white; font-weight: bold; margin:left;} h2{text-align:center; color: gray;margin:left;} h3{text-align:left; margin-left: 30%; color: #483D8B;} 
        .dates{text-align:left; margin-left: 30%; color: #2F4F4F;} h4{text-align:left; margin-left: 30%; color: #6A5ACD;} .totas{text-align:right; margin-right: 35%; margin-top: -40px; color: #008B8B;} 
        h6{color: white; text-align: right; margin-right: 5%; font-size: 15px; margin-bottom: -25px;}
        .codatos{color: white; text-align: left; font-size: 14px;}
        .coencabezado{color: #008B8B; text-align: left; font-size: 14px;}
        table{width: 50%; text-align: left; margin-left: 25%; margin:left; margin-right: 25%;}
        </style></head><body>'''
        for i in range(len(lista_errores_codigo)):
            for k in range(len(lista_errores_codigo[i])):
                mensaje += lista_errores_codigo[i][k]   
        mensaje += '''</body><h6>Alumno</h6><h6>Carne</h6></html>'''
        f.write(mensaje)
        f.close()
        os.startfile('Desktop\C.201906051_Proyecto1\Errores.html')
    else:
        print("SYNTAX ERROR")





#-----------------------------XXXXXXEEEEEEEEEE---XXXXXX--XXXXXX-------XXXXXX--XXXXXX---------------------------------------------
#-----------------------------XXXXXXEEEEEEEEEE---XXXXXXXXXXXXXXXX-----XXXXXXXXXXXXXXXX-------------------------------------------
#-----------------------------XXXXXX-------------XXXXXXXXXXXXXXXXXX---XXXXXXXXXXXXXXXXXX-----------------------------------------
#-----------------------------XXXXXXEEEEEEE------XXXXXXXX------XXXX---XXXXXXXX------XXXX-----------------------------------------
#-----------------------------XXXXXXEEEEEEE------XXXXXX----------XX---XXXXXX----------XX-----------------------------------------
#-----------------------------XXXXXXEEEEEEE------XXXXXX---------------XXXXXX-----------------------------------------------------
#-----------------------------XXXXXX-------------XXXXXX---------------XXXXXX-----------------------------------------------------
#-----------------------------XXXXXXEEEEEEEEEE---XXXXXX---------------XXXXXX-----------------------------------------------------
#-----------------------------XXXXXXEEEEEEEEEE---XXXXXX---------------XXXXXX-----------------------------------------------------
def errores():
    global lista_errores_codigo
    lista_errores_codigo = lista_errores_codigo
    error_a = re.compile(r'[a-z]+-+[a-z0-9]*')#error de guion
    error_b = re.compile(r'\?')#signo ?
    error_c = re.compile(r'\@+?')#signo @
    error_d = re.compile(r'\"+?')#signo "
    error_e = re.compile(r'^\(+?')#signo (
    error_f = re.compile(r'>+?')#signo > entre cosas
    error_g = re.compile(r'<+?')#signo < entre cosas
    error_h = re.compile(r'\)$')#signo )

    encabezado_errores = ['<table><tr><td><strong><h3 class="coencabezado">No.</h3></strong></td>', '<td><strong><h3 class="coencabezado">Fila</h3></strong></td>', '<td><strong><h3 class="coencabezado">Columna</h3></strong></td>', '<td><strong><h3 class="coencabezado">Caracter</h3></strong></td>', '<td><strong><h3 class="coencabezado">Descripcion</h3></strong></td></tr>']
    listado_errores = []
    #------------------------------------------Grupo de Menu - Errores------------------------------------
    
    contador_menu = 1
    lista_errm_a = [] 
    contador_errorm_a = 0
    for i in lectura_texto_menu:
        for x in error_a.finditer(i):
            lista_errm_a.append([0, '<td><h3 class="codatos">'+str(contador_errorm_a)+'</h3></td>', '<td><h3 class="codatos">'+str(x.start())+'</h3></td>', '<td><h3 class="codatos">'+x.group()+'</h3></td>','<td><h3 class="codatos">Identificador Invalido</h3></td></tr>'])
        contador_errorm_a += 1
    for i in range(len(lista_errm_a)):
        listado_errores.append(lista_errm_a[i])

    lista_errm_b = []
    contador_errorm_b = 0
    for i in lectura_texto_menu:
        for x in error_b.finditer(i):
            lista_errm_b.append([0, '<td><h3 class="codatos">'+str(contador_errorm_b)+'</h3></td>', '<td><h3 class="codatos">'+str(x.start())+'</h3></td>', '<td><h3 class="codatos">'+x.group()+'</h3></td>','<td><h3 class="codatos">Caracter Desconocido</h3></td></tr>'])
        contador_errorm_b += 1
    for i in range(len(lista_errm_b)):
        listado_errores.append(lista_errm_b[i])

    lista_errm_c = []
    contador_errorm_c = 0
    for i in lectura_texto_menu:
        for x in error_c.finditer(i):
            lista_errm_c.append([0, '<td><h3 class="codatos">'+str(contador_errorm_c)+'</h3></td>', '<td><h3 class="codatos">'+str(x.start())+'</h3></td>', '<td><h3 class="codatos">'+x.group()+'</h3></td>','<td><h3 class="codatos">Caracter Desconocido</h3></td></tr>'])
        contador_errorm_c += 1
    for i in range(len(lista_errm_c)):
        listado_errores.append(lista_errm_c[i])

    lista_errm_d = []
    contador_errorm_d = 0
    for i in lectura_texto_menu:
        for x in error_d.finditer(i):
            lista_errm_d.append([0, '<td><h3 class="codatos">'+str(contador_errorm_d)+'</h3></td>', '<td><h3 class="codatos">'+str(x.start())+'</h3></td>', '<td><h3 class="codatos">'+x.group()+'</h3></td>','<td><h3 class="codatos">Caracter Desconocido</h3></td></tr>'])
        contador_errorm_d += 1
    for i in range(len(lista_errm_d)):
        listado_errores.append(lista_errm_d[i])

    lista_errm_e = []
    contador_errorm_e = 0
    for i in lectura_texto_menu:
        for x in error_e.finditer(i):
            lista_errm_e.append([0, '<td><h3 class="codatos">'+str(contador_errorm_e)+'</h3></td>', '<td><h3 class="codatos">'+str(x.start())+'</h3></td>', '<td><h3 class="codatos">'+x.group()+'</h3></td>','<td><h3 class="codatos">Caracter Desconocido</h3></td></tr>'])
        contador_errorm_e += 1
    for i in range(len(lista_errm_e)):
        listado_errores.append(lista_errm_e[i])

    lista_errm_f = []
    contador_errorm_f = 0
    for i in lectura_texto_menu:
        for x in error_f.finditer(i):
            lista_errm_f.append([0, '<td><h3 class="codatos">'+str(contador_errorm_f)+'</h3></td>', '<td><h3 class="codatos">'+str(x.start())+'</h3></td>', '<td><h3 class="codatos">'+x.group()+'</h3></td>','<td><h3 class="codatos">Caracter Desconocido</h3></td></tr>'])
        contador_errorm_f += 1
    for i in range(len(lista_errm_f)):
        listado_errores.append(lista_errm_f[i])

    lista_errm_g = []
    contador_errorm_g = 0
    for i in lectura_texto_menu:
        for x in error_g.finditer(i):
            lista_errm_g.append([0, '<td><h3 class="codatos">'+str(contador_errorm_g)+'</h3></td>', '<td><h3 class="codatos">'+str(x.start())+'</h3></td>', '<td><h3 class="codatos">'+x.group()+'</h3></td>','<td><h3 class="codatos">Caracter Desconocido</h3></td></tr>'])
        contador_errorm_g += 1
    for i in range(len(lista_errm_g)):
        listado_errores.append(lista_errm_g[i])

    lista_errm_h = []
    contador_errorm_h = 0
    for i in lectura_texto_menu:
        for x in error_h.finditer(i):
            lista_errm_h.append([0, '<td><h3 class="codatos">'+str(contador_errorm_h)+'</h3></td>', '<td><h3 class="codatos">'+str(x.start())+'</h3></td>', '<td><h3 class="codatos">'+x.group()+'</h3></td>','<td><h3 class="codatos">Caracter Desconocido</h3></td></tr>'])
        contador_errorm_h += 1
    for i in range(len(lista_errm_h)):
        listado_errores.append(lista_errm_h[i])

    #----------------------------------------Grupo de Facturas - Errores------------------------------------

    contador_factura = 0
    lista_errf_a = [] 
    contador_errorf_a = 0
    for i in lectura_texto_factura:
        for x in error_a.finditer(i):
            lista_errf_a.append([0, '<td><h3 class="codatos">'+str(contador_errorf_a)+'</h3></td>', '<td><h3 class="codatos">'+str(x.start())+'</h3></td>', '<td><h3 class="codatos">'+x.group()+'</h3></td>','<td><h3 class="codatos">Identificador Invalido</h3></td></tr>'])
        contador_errorf_a += 1
    for i in range(len(lista_errf_a)):
        listado_errores.append(lista_errf_a[i])

    lista_errf_b = []
    contador_errorf_b = 0
    for i in lectura_texto_factura:
        for x in error_b.finditer(i):
            lista_errf_b.append([0, '<td><h3 class="codatos">'+str(contador_errorf_b)+'</h3></td>', '<td><h3 class="codatos">'+str(x.start())+'</h3></td>', '<td><h3 class="codatos">'+x.group()+'</h3></td>','<td><h3 class="codatos">Caracter Desconocido</h3></td></tr>'])
        contador_errorf_b += 1
    for i in range(len(lista_errf_b)):
        listado_errores.append(lista_errf_b[i])

    lista_errf_c = []
    contador_errorf_c = 0
    for i in lectura_texto_factura:
        for x in error_c.finditer(i):
            lista_errf_c.append([0, '<td><h3 class="codatos">'+str(contador_errorf_c)+'</h3></td>', '<td><h3 class="codatos">'+str(x.start())+'</h3></td>', '<td><h3 class="codatos">'+x.group()+'</h3></td>','<td><h3 class="codatos">Caracter Desconocido</h3></td></tr>'])
        contador_errorf_c += 1
    for i in range(len(lista_errf_c)):
        listado_errores.append(lista_errf_c[i])

    lista_errf_d = []
    contador_errorf_d = 0
    for i in lectura_texto_factura:
        for x in error_d.finditer(i):
            lista_errf_d.append([0, '<td><h3 class="codatos">'+str(contador_errorf_d)+'</h3></td>', '<td><h3 class="codatos">'+str(x.start())+'</h3></td>', '<td><h3 class="codatos">'+x.group()+'</h3></td>','<td><h3 class="codatos">Caracter Desconocido</h3></td></tr>'])
        contador_errorf_d += 1
    for i in range(len(lista_errf_d)):
        listado_errores.append(lista_errf_d[i])

    lista_errf_e = []
    contador_errorf_e = 0
    for i in lectura_texto_factura:
        for x in error_e.finditer(i):
            lista_errf_e.append([0, '<td><h3 class="codatos">'+str(contador_errorf_e)+'</h3></td>', '<td><h3 class="codatos">'+str(x.start())+'</h3></td>', '<td><h3 class="codatos">'+x.group()+'</h3></td>','<td><h3 class="codatos">Caracter Desconocido</h3></td></tr>'])
        contador_errorf_e += 1
    for i in range(len(lista_errf_e)):
        listado_errores.append(lista_errf_e[i])

    lista_errf_f = []
    contador_errorf_f = 0
    for i in lectura_texto_factura:
        for x in error_f.finditer(i):
            lista_errf_f.append([0, '<td><h3 class="codatos">'+str(contador_errorf_f)+'</h3></td>', '<td><h3 class="codatos">'+str(x.start())+'</h3></td>', '<td><h3 class="codatos">'+x.group()+'</h3></td>','<td><h3 class="codatos">Caracter Desconocido</h3></td></tr>'])
        contador_errorf_f += 1
    for i in range(len(lista_errf_f)):
        listado_errores.append(lista_errf_f[i])

    lista_errf_g = []
    contador_errorf_g = 0
    for i in lectura_texto_factura:
        for x in error_g.finditer(i):
            lista_errf_g.append([0, '<td><h3 class="codatos">'+str(contador_errorf_g)+'</h3></td>', '<td><h3 class="codatos">'+str(x.start())+'</h3></td>', '<td><h3 class="codatos">'+x.group()+'</h3></td>','<td><h3 class="codatos">Caracter Desconocido</h3></td></tr>'])
        contador_errorf_g += 1
    for i in range(len(lista_errf_g)):
        listado_errores.append(lista_errf_g[i])

    lista_errf_h = []
    contador_errorf_h = 0
    for i in lectura_texto_factura:
        for x in error_h.finditer(i):
            lista_errf_h.append([0, '<td><h3 class="codatos">'+str(contador_errorf_h)+'</h3></td>', '<td><h3 class="codatos">'+str(x.start())+'</h3></td>', '<td><h3 class="codatos">'+x.group()+'</h3></td>','<td><h3 class="codatos">Caracter Desconocido</h3></td></tr>'])
        contador_errorf_h += 1
    for i in range(len(lista_errf_h)):
        listado_errores.append(lista_errf_h[i])

    for i in range(len(listado_errores)):
        listado_errores[i][0] = '<tr><td><h3 class="codatos">'+str(contador_menu)+'</h3></td>'
        contador_menu += 1
    lista_errores_codigo = listado_errores
    lista_errores_codigo.insert(0, encabezado_errores)
    lista_errores_codigo.insert(0, ['<h2>Tabla de Errores<h2>'])
    lista_errores_codigo.insert(0, [Titulo])
    lista_errores_codigo.append(['</table><br><h4 class="totas">Errores Totales: '+ str(contador_menu-1)+'</h4>'])
    

    








#------XXXXXXXXXXXXXXXXX---XXXXXXXXXXXXXXXXXX---XXXXXXXXXXXXXXXXX------------XXXXXXXXXXXXXXXXXXXXXXXX------------------------------
#------XXXXXXXXXXXXXXXXX---XXXXXXXXXXXXXXXXXX---XXXXXXXXXXXXXXXXX------------XXXXXXXXXXXXXXXXXXXXXXXX------------------------------
#------XXXXXX------XXXXX---XXXXXX------XXXXXX---XXXXX------XXXXXX---------------------XXXXXX---------------------------------------
#------XXXXXX------XXXXX---XXXXXX------XXXXXX---XXXXX------XXXXXX---------------------XXXXXX---------------------------------------
#------XXXXXXXXXXXXXXXXX---XXXXXXXXXXXXXXXXXX---XXXXXXXXXXXXXXXXX---------------------XXXXXX---------------------------------------
#------XXXXXXXXXXXXXXXXX---XXXXXXXXXXXXXXXXXX---XXXXXXXXXXXXXXXXX---------------------XXXXXX---------------------------------------
#------XXXXXX--------------XXXXXX------XXXXXX--------------XXXXXX---------------------XXXXXX---------------------------------------
#------XXXXXX--------------XXXXXX------XXXXXX---XXXXXXXXXXXXXXXXX---------------------XXXXXX---------------------------------------
#------XXXXXX--------------XXXXXX------XXXXXX---XXXXXXXXXXXXXXXXX---------------------XXXXXX---------------------------------------
def pagina_token():
    print('Creando Tabla de TOKENS')
    time.sleep(0.5)
    print('. . . . . . . . . . . .')
    time.sleep(0.5)
    f = open('Desktop\C.201906051_Proyecto1\Token.html', 'w')
    mensaje = '''<!DOCTYPE html>
    <html lang="en"><head><title>Tokens - Proyecto 1</title><link rel="icon" href="https://es.seaicons.com/wp-content/uploads/2016/06/NFSShift-logo-2-icon.png">
    <style>
    body{background-image: url("https://elandroidelibre.elespanol.com/wp-content/uploads/2020/10/Fondos-pantalla-Huawei-Mate-40-10.jpg"); background-repeat:no-repeat;background-attachment: fixed;} 
    h1{text-align:center; color: white; font-weight: bold; margin:left;} h2{text-align:center; color: gray;margin:left;} h3{text-align:left; margin-left: 30%; color: #483D8B;} 
    .dates{text-align:left; margin-left: 30%; color: #2F4F4F;} h4{text-align:left; margin-left: 30%; color: #6A5ACD;} .totas{text-align:right; margin-right: 35%; margin-top: -40px; color: #008B8B;} 
    h6{color: white; text-align: right; margin-right: 5%; font-size: 15px; margin-bottom: -25px;}
    .codatos{color: white; text-align: left; font-size: 14px;}
    .coencabezado{color: #008B8B; text-align: left; font-size: 14px;}
    table{width: 50%; text-align: left; margin-left: 25%; margin:left; margin-right: 25%;}
    </style></head><body>'''
    for i in range(len(lista_token_codigo)):
        for k in range(len(lista_token_codigo[i])):
            mensaje += lista_token_codigo[i][k]   
    mensaje += '''</body><h6>Alumno</h6><h6>Carne</h6></html>'''
    f.write(mensaje)
    f.close()
    os.startfile('Desktop\C.201906051_Proyecto1\Token.html')
    





#--XXXXXXXXXXXXXXXXX------------------XXXXXXXXXXXXXXXXXXXXXXXXXX---XXXXXXXXXXXXXXX---XXXXXXXXXX------XXXXXX-------------------------------
#--XXXXXXXXXXXXXXXXX------------------XXXXXXXXXXXXXXXXXXXXXXXXXX---XXXXXXXXXXXXXXX---XXXXXXXXXX------XXXXXX-------------------------------
#--XXXXXX------XXXXX------------------XXXXXXXXXXXXXXXXXXXXXXXXXX---XXXXXX------------XXXXXX--XXXX----XXXXXX-------------------------------
#--XXXXXX------XXXXX---XXXXXXXXXXXX---XXXXXX-----XXXX-----XXXXXX---XXXXXXXXXXX-------XXXXXX--XXXX----XXXXXX-------------------------------
#--XXXXXXXXXXXXXXXXX---XXXXXXXXXXXX---XXXXXX-----XXXX-----XXXXXX---XXXXXXXXXXX-------XXXXXX---XXXX---XXXXXX-------------------------------
#--XXXXXXXXXXXXXXXXX---XXXXXXXXXXXX---XXXXXX-----XXXX-----XXXXXX---XXXXXXXXXXX-------XXXXXX----XXXX--XXXXXX-------------------------------
#--XXXXXX-----------------------------XXXXXX-----XXXX-----XXXXXX---XXXXXX------------XXXXXX----XXXX--XXXXXX-------------------------------
#--XXXXXX-----------------------------XXXXXX-----XXXX-----XXXXXX---XXXXXXXXXXXXXXX---XXXXXX------XXXXXXXXXX-------------------------------
#--XXXXXX-----------------------------XXXXXX-----XXXX-----XXXXXX---XXXXXXXXXXXXXXX---XXXXXX------XXXXXXXXXX-------------------------------
def pagina_menu():
    print('Procesando')
    time.sleep(0.5)
    print('.  .  .  .')
    time.sleep(0.5)
    f = open('Desktop\C.201906051_Proyecto1\Menu.html', 'w')
    mensaje = '''<!DOCTYPE html>
    <html lang="en"><head><title>Menu - Proyecto 1</title><link rel="icon" href="https://es.seaicons.com/wp-content/uploads/2016/06/NFSShift-logo-2-icon.png">
    <style>
    body{background-image: url("https://elandroidelibre.elespanol.com/wp-content/uploads/2020/10/Fondos-pantalla-Huawei-Mate-40-10.jpg");background-repeat:no-repeat;background-attachment: fixed;} 
    h1{text-align:center; color: white; font-weight: bold;} h2{text-align:left; margin-left: 20%; color: gray;} h3{text-align:left;margin-left: 30%; color: #483D8B;} 
    h4{text-align:left; margin-left: 70%; margin-top:-40px; color: #6A5ACD;} .con{text-align:left; margin-left: 35%; width: 30%; color: #008B8B;} h6{color: white; text-align: right; margin-right: 5%; font-size: 15px; margin-bottom: -25px;}
    </style></head><body><h1></h1>'''
    for i in range(len(objeto_completo)):
        for k in range(len(objeto_completo[i])):
            for m in range(len(objeto_completo[i][k])):
                mensaje += objeto_completo[i][k][m]
    mensaje += '''</body><h6>Alumno</h6><h6>Carne</h6></html>'''
    f.write(mensaje)
    f.close()
    os.startfile('Desktop\C.201906051_Proyecto1\Menu.html')
#FIN PAGINA






#-----------------------XXXXXXXXXXXXXXXXXXXXXXXXXX---XXXXXXXXXXXXXXX---XXXXXXXXXX------XXXXXX--------------------------------------
#-----------------------XXXXXXXXXXXXXXXXXXXXXXXXXX---XXXXXXXXXXXXXXX---XXXXXXXXXX------XXXXXX--------------------------------------
#-----------------------XXXXXXXXXXXXXXXXXXXXXXXXXX---XXXXXX------------XXXXXX--XXXX----XXXXXX--------------------------------------
#-----------------------XXXXXX-----XXXX-----XXXXXX---XXXXXXXXXXX-------XXXXXX--XXXX----XXXXXX--------------------------------------
#-----------------------XXXXXX-----XXXX-----XXXXXX---XXXXXXXXXXX-------XXXXXX---XXXX---XXXXXX--------------------------------------
#-----------------------XXXXXX-----XXXX-----XXXXXX---XXXXXXXXXXX-------XXXXXX----XXXX--XXXXXX--------------------------------------
#-----------------------XXXXXX-----XXXX-----XXXXXX---XXXXXX------------XXXXXX----XXXX--XXXXXX--------------------------------------
#-----------------------XXXXXX-----XXXX-----XXXXXX---XXXXXXXXXXXXXXX---XXXXXX------XXXXXXXXXX--------------------------------------
#-----------------------XXXXXX-----XXXX-----XXXXXX---XXXXXXXXXXXXXXX---XXXXXX------XXXXXXXXXX--------------------------------------
def cargar_menu():
    global salida, Titulo, objeto_completo, lista_objeto_receta, menu_existente, lista_token_codigo, lectura_texto_menu, Titulo_limpio
    lectura_texto_menu = lectura_texto_menu
    Titulo_limpio = Titulo_limpio
    menu_existente = menu_existente
    lista_token_codigo = lista_token_codigo
    lista_objeto_receta = lista_objeto_receta
    objeto_completo = objeto_completo
    root = tkinter.Tk()
    Titulo = Titulo#()[]
    print('Cargando Menu')
    funciones = re.compile(r".*'*'\s*:?\s*\]?")#Lee lineas con los datos completos
    filtro_objeto_receta = re.compile(r"[a-z][a-z0-9_]*(\s*);\s*'[^']*'\s*;(\s*)[0-9]+(\.[0-9]*)?(\s*);(\s*)'[^']*'")#Lee los objetos que tienen las recetas
    filtro_receta = re.compile(r"^'[^']*'")#Lee nombres de recetas
    filtro_titulo = re.compile(r"'.*'")
    filtro_ob_tit = re.compile(r"\b.*")
    filtro_sep_rec = re.compile(r"\b[a-z]*.*'")
    filtro_un_se = re.compile(r'[a-z][a-z0-9_]*')#Columna 1 para objeto recetas
    filtro_mon = re.compile(r'\b[0-9]+(\.[0-9]*)?')
    filtro_com = re.compile(r"\b[a-z]*.*'")
    ruta = filedialog.askopenfilename(title="Seleccionar Archivo")
    archivo_contenido = open(ruta, 'r', encoding='utf-8')
    #archivo_contenido = open('C:/Users/Pacos/Desktop/LFP-Proyecto1-2021S1-main/menu.lfp', encoding='utf-8')
    texto = archivo_contenido.readlines()
    lectura_texto_menu = texto
    menu_existente = True
    contador = 1
    salida = salida
    root.destroy() #Cerrar ventana
    for i in texto:
        for x in funciones.finditer(i):
            salida += 'Lexema: ' + x.group() + '\n' 
        contador += 1
    #Objeto que contiene todo
    cont_inicio = 0
    texto_objeto_completo = []
    texto_objeto_ufo = []
    for i in texto:
        for x in funciones.finditer(i):
            texto_objeto_completo.append([cont_inicio, x.group().rstrip('\n').split(';')])
            objeto_completo.append(x.group().rstrip('\n').split(';'))
        cont_inicio+=1
    #Objeto con info recetas
    cont_objeto_receta = 0
    texto_objeto_recetas = []
    texto_objeto_recetas2 = []
    for i in texto:
        for x in filtro_objeto_receta.finditer(i):
            texto_objeto_recetas.append([cont_objeto_receta,x.group().rstrip('\n').split(';')])
            texto_objeto_recetas2.append([cont_objeto_receta,x.group().rstrip('\n').split(';')])
            #lista_objeto_receta.append(x.group().rstrip('\n').split(';'))
        cont_objeto_receta+=1
    #FIN Objeto con Nombre Recetas
    cont_receta = 0
    texto_recetas = []
    texto_recetas2 = []
    for i in texto:
        for x in filtro_receta.finditer(i):
            texto_recetas.append([cont_receta, x.group().rstrip('\n')])
            texto_recetas2.append([cont_receta, x.group().rstrip('\n')])
            #lista_receta.append(x.group().rstrip('\n'))
        cont_receta += 1
    tie = texto_objeto_completo[0][1][0]
    coushi = ""
    for x in filtro_titulo.finditer(tie):
        coushi = x.group()
    for x in filtro_ob_tit.finditer(coushi):
        Titulo = '<h1>'+ x.group().rstrip("'") +'</h1>'
        Titulo_limpio = x.group().rstrip("'")
    texto_objeto_completo[0][1] = [Titulo]
    #Nombre Recetas
    texto_recetalimpia = []
    texto_receta_falta = []
    texto_recetalimpia2 = []
    texto_receta_falta2 = []
    for i in range(len(texto_recetas)):
        texto_receta_falta.append(texto_recetas[i][1])
    for i in texto_receta_falta:
        for x in filtro_sep_rec.finditer(i):
            texto_recetalimpia.append(x.group())
            texto_recetalimpia2.append(x.group())
    for i in range(len(texto_recetalimpia)):
        texto_receta_falta[i] = texto_recetalimpia[i].rstrip("'")
    for i in range(len(texto_recetalimpia)):
        texto_recetas[i][1] = texto_receta_falta[i]
    for i in range(len(texto_recetalimpia2)):
        texto_recetas2[i][1] = ['<h2>'+texto_receta_falta[i]+'</h2>']
        
        
        
        
    for i in range(len(texto_recetas)):
        Nombre_Recetas.append(texto_recetas[i][1])
    #FIN Nombre Recetas
    #Contenido Recetas - Codigo
    #---XXXXXXXXXXXXXXXXXXXXXXXX---XXXXXXXXXXXXXXXXXXXXXX---XXXXXXX-------XXXXXXX---XXXXXXXXXXXXXXXXX---XXXXXXXXXXXX-----XXXXXX-----------
    #---XXXXXXXXXXXXXXXXXXXXXXXX---XXXXXXXXXXXXXXXXXXXXXX---XXXXXXX----XXXXXXXX-----XXXXXXXXXXXXXXXXX---XXXXXXXXXXXX-----XXXXXX-----------
    #-------------XXXX-------------XXXXXX----------XXXXXX---XXXXXXX---XXXXXXX-------XXXXXX--------------XXXXXX-XXXXXX----XXXXXX-----------
    #-------------XXXX-------------XXXXXX----------XXXXXX---XXXXXXXXXXXXXX----------XXXXXXXXXXXX--------XXXXXX--XXXXXX---XXXXXX-----------
    #-------------XXXX-------------XXXXXX----------XXXXXX---XXXXXXXXXXXXXX----------XXXXXXXXXXXX--------XXXXXX---XXXXXX--XXXXXX-----------
    #-------------XXXX-------------XXXXXX----------XXXXXX---XXXXXXX----XXXXXXX------XXXXXX--------------XXXXXX----XXXXXX-XXXXXX-----------
    #-------------XXXX-------------XXXXXXXXXXXXXXXXXXXXXX---XXXXXXX---- XXXXXXXX----XXXXXXXXXXXXXXXXX---XXXXXX-----XXXXXXXXXXXX-----------
    #-------------XXXX-------------XXXXXXXXXXXXXXXXXXXXXX---XXXXXXX-------XXXXXXX---XXXXXXXXXXXXXXXXX---XXXXXX-----XXXXXXXXXXXX-----------
    
    lista_token_encabezado = ['<table><tr><td><strong><h3 class="coencabezado">No.</h3></strong></td>', '<td><strong><h3 class="coencabezado">Lexema</h3></strong></td>', '<td><strong><h3 class="coencabezado">Fila</h3></strong></td>', '<td><strong><h3 class="coencabezado">Columna</h3></strong></td>', '<td><strong><h3 class="coencabezado">Token</h3></strong></td></tr>']
    contador_token_codigo = 1
    desorden_cod = []
    desorden_cod2 = []
    semides_cod = []
    semides_cod2 = []
    for i in range(len(texto_objeto_recetas)):
        desorden_cod.append(texto_objeto_recetas[i][1][0])
        desorden_cod2.append(texto_objeto_recetas[i][1][0])
    for i in desorden_cod:
        for x in filtro_un_se.finditer(i):
            semides_cod.append(x.group())
            semides_cod2.append(x.group())
            lista_token_codigo.append(['<tr><td><h3 class="codatos">'+str(contador_token_codigo)+'</h3></td>', '<td><h3 class="codatos">'+x.group()+'</h3></td>', 1, '<td><h3 class="codatos">'+str(x.start())+'</h3></td>', '<td><h3 class="codatos">identificador</td></tr>'])
        contador_token_codigo += 1
    
    for i in range(len(semides_cod)):
        texto_objeto_recetas[i][1][0] = semides_cod[i]
        texto_objeto_recetas2[i][1][0] = semides_cod[i]
        lista_token_codigo[i][2] = '<td><h3 class="codatos">'+str(texto_objeto_recetas[i][0])+'</h3></td>'
    #print(lista_token_codigo)
    #print(texto_objeto_recetas) ------------> texto_objeto_recetas es el contenido de las recetas
    lista_token_numero = []
    contador_token_filas = 0
    for i in texto:
        for x in filtro_mon.finditer(i):
            lista_token_numero.append([0, '<td><h3 class="codatos">'+x.group()+'</h3></td>', '<td><h3 class="codatos">'+str(contador_token_filas)+'</h3></td>', '<td><h3 class="codatos">'+str(x.start())+'</h3></td>', '<td><h3 class="codatos">numero</h3></td></tr>'])
        contador_token_filas += 1
    for i in range(len(lista_token_numero)):
        lista_token_numero[i][0] = '<td><h3 class="codatos">'+str(contador_token_codigo)+'</h3></td>'
        contador_token_codigo += 1
        lista_token_codigo.append(lista_token_numero[i])
    lista_token_codigo.insert(0, lista_token_encabezado)
    lista_token_codigo.insert(0, ['<h2>Tabla de Tokens<h2>'])
    lista_token_codigo.insert(0, [Titulo])
    lista_token_codigo.append(['</table><br><h4 class="totas">Total Lexemas: '+ str(contador_token_codigo-1)+'</h4>'])
    #FIN TOKEN FIN TOKEN FIN TOKEN FIN TOKEN FIN TOKEN FIN TOKEN FIN TOKEN FIN TOKEN FIN TOKEN FIN TOKEN FIN TOKEN FIN TOKEN
    #FIN TOKEN FIN TOKEN FIN TOKEN FIN TOKEN FIN TOKEN FIN TOKEN FIN TOKEN FIN TOKEN FIN TOKEN FIN TOKEN FIN TOKEN FIN TOKEN
    #FIN TOKEN FIN TOKEN FIN TOKEN FIN TOKEN FIN TOKEN FIN TOKEN FIN TOKEN FIN TOKEN FIN TOKEN FIN TOKEN FIN TOKEN FIN TOKEN

    #FIN Contenido Recetas - Codigo
    #Columna Nombre de Receta
    desorden_nom = []
    desorden_nom2 = []
    semides_nom = []
    semides_nom2 = []
    for i in range(len(texto_objeto_recetas)):
        desorden_nom.append(texto_objeto_recetas[i][1][1])
        desorden_nom2.append(texto_objeto_recetas[i][1][1])
    for i in desorden_nom:
        for x in filtro_sep_rec.finditer(i):
            semides_nom.append(x.group().rstrip("'"))
    for i in range(len(semides_nom)):
        texto_objeto_recetas[i][1][1] = semides_nom[i]
        texto_objeto_recetas2[i][1][1] = '<h3>'+'@ '+semides_nom[i]+'</h3>'
        #print(texto_objeto_recetas2[i][1][1:])
    #FIN Columna Nombre de Receta
    #Columna Costo Receta
    desorden_cos = []
    desorden_cos2 = []
    semides_cos = []
    semides_cos2 = []
    for i in range(len(texto_objeto_recetas)):
        desorden_cos.append(texto_objeto_recetas[i][1][2])
        desorden_cos2.append(texto_objeto_recetas[i][1][2])
    for i in desorden_cos:
        for x in filtro_mon.finditer(i):
            semides_cos.append(float(x.group()))
    for i in range(len(semides_cos)):
        texto_objeto_recetas[i][1][2] = semides_cos[i]
        texto_objeto_recetas2[i][1][2] = '<h4>'+'Q.'+str(semides_cos[i])+'0'+'</h4>'
    #FIN Columna Costo Receta
    #Columna Comentario Receta
    desorden_com = []
    desorden_com2 = []
    semides_com = []
    semides_com2 = []
    for i in range(len(texto_objeto_recetas)):
        desorden_com.append(texto_objeto_recetas[i][1][3])
        desorden_com2.append(texto_objeto_recetas2[i][1][3])
    for i in desorden_com:
        for x in filtro_com.finditer(i):
            semides_com.append(x.group().rstrip("'"))
    for i in range(len(semides_com)):
        texto_objeto_recetas[i][1][3] = semides_com[i]
        texto_objeto_recetas2[i][1][3] = '<h3 class="con">'+'Descripción: \n'+semides_com[i]+'</h3>'
        #print(texto_objeto_recetas2[i])
    #FIN Columna Comentario Receta
    #print(texto_objeto_completo[2][1])
    #print(texto_objeto_recetas[2][1])
    #Lista Arreglada
    for i in range(len(texto_objeto_recetas)):
        Recetas_Obtenidas.append([texto_objeto_recetas[i][1][1], "Q."+"{0:.2f}".format(texto_objeto_recetas[i][1][2]), texto_objeto_recetas[i][1][3]])
    texto_objeto_normal = texto_objeto_completo
    for i in range(len(texto_objeto_completo)):
        for x in range(len(texto_recetas)):
            if texto_objeto_completo[i][0] == texto_recetas[x][0]:
                texto_objeto_completo[i][1] = texto_recetas[x][1]
                texto_objeto_normal[i][1] = texto_recetas2[x][1]
    for i in range(len(texto_objeto_completo)):
        for x in range(len(texto_objeto_recetas)):
            if texto_objeto_completo[i][0] == texto_objeto_recetas[x][0]:
                texto_objeto_completo[i][1] = texto_objeto_recetas[x][1]
                texto_objeto_normal[i][1] = texto_objeto_recetas2[x][1]
        for x in range(len(texto_objeto_recetas)):
            if texto_objeto_completo[i][0] == texto_objeto_recetas[x][0]:
                texto_objeto_completo[i][1] = texto_objeto_recetas[x][1][1:]
                texto_objeto_normal[i][1] = texto_objeto_recetas2[x][1][1:]
        objeto_completo[i] = texto_objeto_normal[i][1:]
    lista_objeto_receta = texto_objeto_recetas
    '''for i in range(len(texto_objeto_completo)):
        for k in range(1,len(texto_objeto_completo[i])):
            print(texto_objeto_completo[i][k])'''
    '''for i in range(len(texto_recetas)):
        print(texto_recetas[i])'''
    print('Menu Cargado')
    archivo_contenido.close()
#FIN CARGA DE ARCHIVO MENU






#-------XXXXXXXXXXXXXXXXX----------------XXXXXXXXXXXXXXXXX---XXXXXXXXXXXXXXXXXX---XXXXXXXXXXXXXXXX----------------------------------------
#-------XXXXXXXXXXXXXXXXX----------------XXXXXXXXXXXXXXXXX---XXXXXXXXXXXXXXXXXX---XXXXXXXXXXXXXXXX----------------------------------------
#-------XXXXXX------XXXXX----------------XXXXXXXXXXXXXXXXX---XXXXXXXXXXXXXXXXXX---XXXXXXXXXXXXXXXX----------------------------------------
#-------XXXXXX------XXXXX----------------XXXXXX--------------XXXXXX------XXXXXX---XXXXXX------XXXX----------------------------------------
#-------XXXXXXXXXXXXXXXXX---XXXXXXXXXX---XXXXXX--------------XXXXXX------XXXXXX---XXXXXX--------------------------------------------------
#-------XXXXXXXXXXXXXXXXX---XXXXXXXXXX---XXXXXXXXXXXXX-------XXXXXXXXXXXXXXXXXX---XXXXXX--------------------------------------------------
#-------XXXXXX---------------------------XXXXXXXXXXXXX-------XXXXXXXXXXXXXXXXXX---XXXXXX------XXXX----------------------------------------
#-------XXXXXX---------------------------XXXXXX--------------XXXXXX------XXXXXX---XXXXXXXXXXXXXXXX----------------------------------------
#-------XXXXXX---------------------------XXXXXX--------------XXXXXX------XXXXXX---XXXXXXXXXXXXXXXX----------------------------------------
#-------XXXXXX---------------------------XXXXXX--------------XXXXXX------XXXXXX---XXXXXXXXXXXXXXXX----------------------------------------
def pagina_factura():
    if factura_valida == True:
        print('Procesando')
        time.sleep(0.5)
        print('.  .  .  .')
        time.sleep(0.5)
        f = open('Desktop\C.201906051_Proyecto1\Factura.html', 'w')
        mensaje = '''<!DOCTYPE html>
        <html lang="en"><head><title>Factura - Proyecto 1</title><link rel="icon" href="https://es.seaicons.com/wp-content/uploads/2016/06/NFSShift-logo-2-icon.png">
        <style>
        body{background-image: url("https://elandroidelibre.elespanol.com/wp-content/uploads/2020/10/Fondos-pantalla-Huawei-Mate-40-10.jpg");background-repeat:no-repeat;background-attachment: fixed;} 
        h1{text-align:center; color: white; font-weight: bold; margin:left;} h2{text-align:center; color: gray;margin:left;} h3{text-align:left; margin-left: 30%; color: #483D8B;} 
        .dates{text-align:left; margin-left: 30%; color: #2F4F4F;} h4{text-align:left; margin-left: 30%; color: #6A5ACD;} .totas{text-align:right; margin-right: 35%; margin-top: -40px; color: #008B8B;} 
        h6{color: white; text-align: right; margin-right: 5%; font-size: 15px; margin-bottom: -25px;}
        .codatos{color: white; text-align: left; font-size: 14px;}
        .coencabezado{color: #008B8B; text-align: left; font-size: 14px;}
        table{width: 50%; text-align: left; margin-left: 25%; margin:left; margin-right: 25%;}
        </style></head><body>'''
        for i in range(len(objeto_obtener_factura)):
            for k in range(len(objeto_obtener_factura[i])):
                mensaje += objeto_obtener_factura[i][k]   
        mensaje += '''</body><h6>Alumno</h6><h6>Carne</h6></html>'''
        f.write(mensaje)
        f.close()
        os.startfile('Desktop\C.201906051_Proyecto1\Factura.html')
    else:
        print("FACTURA INVALIDA")
#FIN PAGINA FACTURA






#-----------------------------XXXXXXXXXXXXXXXXX---XXXXXXXXXXXXXXXXXX---XXXXXXXXXXXXXXXX----------------------------------------
#-----------------------------XXXXXXXXXXXXXXXXX---XXXXXXXXXXXXXXXXXX---XXXXXXXXXXXXXXXX----------------------------------------
#-----------------------------XXXXXXXXXXXXXXXXX---XXXXXXXXXXXXXXXXXX---XXXXXXXXXXXXXXXX----------------------------------------
#-----------------------------XXXXXX--------------XXXXXX------XXXXXX---XXXXXX------XXXX----------------------------------------
#-----------------------------XXXXXX--------------XXXXXX------XXXXXX---XXXXXX--------------------------------------------------
#-----------------------------XXXXXXXXXXXXX-------XXXXXXXXXXXXXXXXXX---XXXXXX--------------------------------------------------
#-----------------------------XXXXXXXXXXXXX-------XXXXXXXXXXXXXXXXXX---XXXXXX------XXXX----------------------------------------
#-----------------------------XXXXXX--------------XXXXXX------XXXXXX---XXXXXXXXXXXXXXXX----------------------------------------
#-----------------------------XXXXXX--------------XXXXXX------XXXXXX---XXXXXXXXXXXXXXXX----------------------------------------
#-----------------------------XXXXXX--------------XXXXXX------XXXXXX---XXXXXXXXXXXXXXXX----------------------------------------
def cargar_factura():
    if menu_existente == True:
        global salida_factura, objeto_factura, objeto_obtener_factura, factura_valida, lectura_texto_factura
        lectura_texto_factura = lectura_texto_factura
        factura_valida = factura_valida
        salida_factura = salida_factura
        objeto_factura = objeto_factura
        objeto_obtener_factura = objeto_obtener_factura
        root = tkinter.Tk()
        print('Cargando Factura')
        encabezado_factura = re.compile(r"\s*'[^']*'\s*,\s*'[^']*'\s*,\s*'[^']*'\s*,\s*[0-9]+(\.[0-9]*)?%")#Conseguir encabezado
        contenido_factura = re.compile(r"[1-9]+\s*,\s*[a-z][a-z0-9_]*")#conseguir cuerpo
        letras_factura = re.compile(r"[A-Z][a-z]+.*'")
        numeros_factura = re.compile(r'\b[0-9]+(\.[0-9]*)?(-[a-z0-9])?')
        num_content_fac = re.compile(r'[0-9]+')
        funciones = re.compile(r"\b.*,.*")
        let_content_fac = re.compile(r"\b[a-z][a-z0-9_]*")
        ruta = filedialog.askopenfilename(title="Seleccionar Archivo")
        archivo_contenido = open(ruta, 'r', encoding='utf-8')
        #archivo_contenido = open('C:/Users/Pacos/Desktop/LFP-Proyecto1-2021S1-main/orden.lfp', encoding='utf-8')
        texto = archivo_contenido.readlines()
        lectura_texto_factura = texto
        root.destroy() #Cerrar ventana
        factura_ha = []
        conte = 0
        coni = 0
        conf = 0
        factura_des = []
        factura_des2 = []
        for i in texto:
            for x in funciones.finditer(i):
                factura_des.append([coni, x.group().split(',')])
            coni += 1
        cons = 0
        factura_des2 = factura_des
        fa_re = []
        for i in texto:
            for x in encabezado_factura.finditer(i):
                factura_ha.append(x.group().rstrip('\n').split(','))   
        #CONTENIDO FACTURA
        obtention = []
        contad = 0
        for i in texto:
            for x in contenido_factura.finditer(i):
                obtention.append([contad, x.group().split(',')])
            contad += 1
        #FIN CONTENIDO FACTURA
        #CAMBIO CABECERA DE FACTURA
        nume = []
        nume2 = []
        for i in factura_ha[0]:
            for x in numeros_factura.finditer(i):
                nume.append([conte, x.group()])
                nume2.append([conte, x.group()]) 
            conte += 1
        coned = 0
        let = []
        encabezado_factura2 = []
        factura_encab = []
        factura_encab2 = []
        for i in factura_ha[0]:
            for x in letras_factura.finditer(i):
                let.append([coned, x.group().rstrip("'")])
            coned += 1
        fi = nume2[0][1]
        nume2[0][1] = fi
        nume[0][1] = fi
        fa = float(nume[1][1])
        fa2 = float(nume2[1][1])
        porcentaje = fa2/100
        nume[1][1] = str(fa)+'%'
        nume2[1][1] = porcentaje
        factura_encab.append(let[0][1])
        factura_encab.append(nume[0][1])
        factura_encab.append(let[1][1])
        factura_encab.append(nume[1][1])
        encabezado_factura = [0,factura_encab]
        factura_des[0] = encabezado_factura
        factura_encab2.append(let[0][1])
        factura_encab2.append(nume2[0][1])
        factura_encab2.append(let[1][1])
        factura_encab2.append(nume2[1][1])
        encabezado_factura2 = [0,factura_encab2]
        factura_des2[0] = encabezado_factura2
        factura_des_5 = []
        factura_des_5.append(encabezado_factura)
        #FIN CAMBIO CABECERA FACTURA
        #obtention
        #print(obtention[0][1][1])
        #print(len(obtention))
        numeros_fat = []
        for i in range(len(obtention)):
            numeros_fat.append(obtention[i][1][0])
            obtention[i][1][0] = int(numeros_fat[i])
        
        palabras_fat = []
        palabras_fet = []
        for i in range(len(obtention)):
            palabras_fat.append(obtention[i][1][1])
        for i in palabras_fat:
            for x in let_content_fac.finditer(i):
                palabras_fet.append(x.group())
        for i in range(len(palabras_fet)):
            obtention[i][1][1] = palabras_fet[i]
        #print(obtention[1][0])
        #print(factura_des[1])
        for i in range(len(factura_des)):
            for x in range(len(obtention)):
                if factura_des[i][0] == obtention[x][0]:
                    factura_des[i] = obtention[x]
                    factura_des2[i] = obtention[x]
                    factura_des_5.append(obtention[x])
        factura_des_5.insert(0,[0,Titulo])
        #print(obtention[0][1][1])
        #print(lista_objeto_receta[0][1][0])
        seguir = False      
        lista_pedido = []
        lista_pedido2 = []
        for i in range(len(lista_objeto_receta)):
            for k in range(len(obtention)):
                if lista_objeto_receta[i][1][0] == obtention[k][1][1]:
                    objeto_factura.append(obtention[k][1])
        for i in range(len(objeto_factura)):
            lista_pedido.append(objeto_factura[i])
        lista_para_pagina = []
        for i in range(len(lista_objeto_receta)):
            for k in range(len(obtention)):        
                if lista_objeto_receta[i][1][0] == obtention[k][1][1]:
                    lista_pedido2.append([obtention[k][1][0], lista_objeto_receta[i][1][1], lista_objeto_receta[i][1][2], ''])
                    lista_para_pagina.append([obtention[k][1][0], lista_objeto_receta[i][1][1], lista_objeto_receta[i][1][2], ''])
                    seguir = True
                    factura_valida = True
        #print(lista_para_pagina)
        if seguir == True:
            total = []
            total_suma = 0
            porcentaje_dado = porcentaje
            cantidad_de_cosas = []
            concepto_de_cosas = []
            precio_de_cosas = []
            for i in range(len(lista_pedido2)):
                total.append(lista_pedido2[i][2]*lista_pedido2[i][0])
                lista_pedido2[i][3] = total[i]
                lista_para_pagina[i][3] = '<td><h3 class="codatos">'+str(total[i])+'</h3></td></tr>'
                cantidad_de_cosas.append('<tr><td><h3 class="codatos">'+str(lista_pedido2[i][0])+'</h3></td>')
                concepto_de_cosas.append('<td><h3 class="codatos">'+lista_pedido2[i][1]+'</h3></td>')
                precio_de_cosas.append('<td><h3 class="codatos">'+str(lista_pedido2[i][2])+'0'+'</h3></td>')
                lista_para_pagina[i][0] = cantidad_de_cosas[i]
                lista_para_pagina[i][1] = concepto_de_cosas[i]
                lista_para_pagina[i][2] = precio_de_cosas[i]
                total_suma = total_suma + total[i]
            propina = total_suma*porcentaje
            propina_obtenida = round(propina, 2)
            sub_total = "{0:.2f}".format(total_suma)
            porc = str(fa)+'%'
            men = ['<table><tr><td><strong><h3 class="coencabezado">Cantidad</h3></strong></td>','<td><strong><h3 class="coencabezado">Concepto</h3></strong></td>', '<td><strong><h3 class="coencabezado">Precio</h3></strong></td>', '<td><strong><h3 class="coencabezado">Total</h3></strong></td></tr>']
            sube = ['</table><h4>Sub total</h4>', '<h4 class="totas">'+str(sub_total)+'</h4>']
            propina_seccion = ['<h4>Propina '+'('+porc+')</h4>', '<h4 class="totas">'+str(propina_obtenida)+'</h4>']
            total_total = float(sub_total) + propina_obtenida
            Final_Seccion = ['<h4>Total</h4>', '<h4 class="totas">'+str(total_total)+'</h4>']
            Titulo_Restaurante = Titulo
            Numero_Factura = ['<h2>'+'Factura No. 01'+'</h2>']
            now = datetime.now()
            segundo = now.second
            minuto = now.minute
            hora = now.hour
            dia = now.day
            mes = now.month
            anyo = now.year
            fecha_factura = ['<h2>'+'Fecha: '+str(anyo)+' / '+str(mes)+' / '+str(dia)+' - '+str(hora)+':'+str(minuto)+':'+str(segundo)+'</h2>']
            datos_cliente_falta = encabezado_factura[1][:3]
            datos_cliente_final = ['<h3>Datos del Cliente</h3>', '<h3 class="dates">Nombre: '+datos_cliente_falta[0]+'</h3>', '<h3 class="dates">NIT: '+datos_cliente_falta[1]+'</h3 class="dates">', '<h3 class="dates">Direccion: '+datos_cliente_falta[2]+'</h3><br>','<h3>Descripcion</h3>']
            lista_para_pagina.insert(0, men)
            lista_para_pagina.insert(0, datos_cliente_final)
            lista_para_pagina.insert(0, fecha_factura)
            lista_para_pagina.insert(0, Numero_Factura)
            lista_para_pagina.insert(0, [Titulo_Restaurante])
            lista_para_pagina.append(sube)
            lista_para_pagina.append(propina_seccion)
            lista_para_pagina.append(Final_Seccion)
            objeto_obtener_factura = lista_para_pagina


            errores()
        else:
            print("Factura NO VALIDA")
    else:
        print('El Menu no ha sido Cargado')
        #print(objeto_obtener_factura)
#FIN CARGA FACTURA






#-------XXXXXXXXXXXXXXXXXX---XXXXXXXXXXXXXXXXX----XXXXXXXXXXXXXXXXX----XXXXXXXXXXXXXXXXXXXX---XXXXXX-----------------------------------------
#-------XXXXXXXXXXXXXXXXXX---XXXXXXXXXXXXXXXXXX---XXXXXXXXXXXXXXXXXX---XXXXXXXXXXXXXXXXXXXX---XXXXXX-----------------------------------------
#-------XXXXXXXXXXXXXXXXXX---XXXXXXXXXXXXXXXXX----XXXXXX-------XXXX----XXXXXXXXXXXXXXXXXXXX---XXXXXX-----------------------------------------
#-------XXXXXX------XXXXXX---XXXXXX------XXXX-----XXXXXX------XXXX-----XXXXXX--------XXXXXX---XXXXXX-----------------------------------------
#-------XXXXXX------XXXXXX---XXXXXX------XXX------XXXXXXXXXXXXXX-------XXXXXX--------XXXXXX---XXXXXX-----------------------------------------
#-------XXXXXXXXXXXXXXXXXX---XXXXXXXXXXXXXX-------XXXXXX------XXXX-----XXXXXX--------XXXXXX---XXXXXX-----------------------------------------
#-------XXXXXXXXXXXXXXXXXX---XXXXXXXXXXXXXXX------XXXXXX-------XXXXX---XXXXXXXXXXXXXXXXXXXX---XXXXXX-----------------------------------------
#-------XXXXXX------XXXXXX---XXXXXX-----XXXXX-----XXXXXXXXXXXXXXXXXX---XXXXXXXXXXXXXXXXXXXX---XXXXXXXXXXXXXXXXX------------------------------
#-------XXXXXX------XXXXXX---XXXXXX-----XXXXXX----XXXXXXXXXXXXXXXXX----XXXXXXXXXXXXXXXXXXXX---XXXXXXXXXXXXXXXXX------------------------------
def generar_arbol():
    print('Generando Arbol')
    time.sleep(0.5)
    print('. . . . . . . .')
    time.sleep(0.5)
    arbol = Digraph('Arbol', filename='Desktop\C.201906051_Proyecto1\Arbol.pdf', node_attr={'color': 'lightgrey', 'style':'filled', 'constraint': 'false'})
    #print(Recetas_Obtenidas)
    #arbol.edge(Titulo_limpio, 'hola')
    #print(Recetas_Obtenidas)
    for i in range(len(Nombre_Recetas)):
        arbol.edge(Titulo_limpio, Nombre_Recetas[i])
        for k in range(len(Recetas_Obtenidas)):
            for m in range(len(Recetas_Obtenidas[k])):
                arbol.edge(Nombre_Recetas[i], Recetas_Obtenidas[k][m])
    
    
    arbol.node(Titulo_limpio, shape='Mdiamond')
    
    
    arbol.view()
    exit()
    
    
    
    
    
    
    '''
    arbol = open('Desktop\C.201906051_Proyecto1\Arbol.dot', 'w')
    contenido = ''
    contenido = Titulo_limpio 
    arbol.write('digraph D{\n')
    arbol.write(contenido )
    arbol.write('}')
    arbol.close()
    os.system('dot -Tpdf Desktop\C.201906051_Proyecto1\Arbol.dot -o Desktop\C.201906051_Proyecto1\Arbol.pdf')
    os.startfile('Desktop\C.201906051_Proyecto1\Arbol.pdf')
    '''
#FIN GENERAR ARBOL












#-------------------------XXXXXXXXXXXXXXXXX-------------------XXXXXXXXXXXXXXXXXXX-------------------------------------------------
#-------------------------XXXXXXXXXXXXXXXXXX------------------XXXXXXXXXXXXXXXXXXX-------------------------------------------------
#-------------------------XXXXXXXXXXXXXXXXXXXX----------------XXXXXX-------XXXXXX-------------------------------------------------
#-------------------------XXXXXX--------XXXXXX---XXXXXXXXXX---XXXXXX-------XXXXXX-------------------------------------------------
#-------------------------XXXXXX--------XXXXXX---XXXXXXXXXX---XXXXXXXXXXXXXXXXXXX-------------------------------------------------
#-------------------------XXXXXX--------XXXXXX---XXXXXXXXXX---XXXXXXXXXXXXXXXXXXX-------------------------------------------------
#-------------------------XXXXXXXXXXXXXXXXXXXX----------------XXXXXX--------------------------------------------------------------
#-------------------------XXXXXXXXXXXXXXXXXX------------------XXXXXX--------------------------------------------------------------
#-------------------------XXXXXXXXXXXXXXXXX-------------------XXXXXX--------------------------------------------------------------
def datos_personales():
    print("Universidad de San Carlos de Guatemala")
    print("-----------------  Facultad de Ingenieria")
    print("------- Ingenieria en Ciencias & Sistemas")
    print("Lab. Lenguajes Formales & de Programacion")
    print("Seccion: --------------------------->  A-")
    print("Alumno")
    print("Carne")






#-------------------------XXXXXXXX-----------XXXXXXXX----------------XXXXXXXXXXXXXXXXXXX-------------------------------------------------
#-------------------------XXXXXXXXX---------XXXXXXXXX----------------XXXXXXXXXXXXXXXXXXX-------------------------------------------------
#-------------------------XXXXXXXXXX-------XXXXXXXXXX----------------XXXXXX-------XXXXXX-------------------------------------------------
#-------------------------XXXXXXXXXXXX---XXXXXXXXXXXX---XXXXXXXXXX---XXXXXX-------XXXXXX-------------------------------------------------
#-------------------------XXXXXX-----XXXXX-----XXXXXX---XXXXXXXXXX---XXXXXXXXXXXXXXXXXXX-------------------------------------------------
#-------------------------XXXXXX-----XXXXX-----XXXXXX---XXXXXXXXXX---XXXXXXXXXXXXXXXXXXX-------------------------------------------------
#-------------------------XXXXXX-----XXXXX-----XXXXXX----------------XXXXXX--------------------------------------------------------------
#-------------------------XXXXXX-----XXXXX-----XXXXXX----------------XXXXXX--------------------------------------------------------------
#-------------------------XXXXXX-----XXXXX-----XXXXXX----------------XXXXXX--------------------------------------------------------------
if os.path.isdir('Desktop/C.201906051_Proyecto1/'):
    print('                             Ruta Existente')
else:
    print('                             Creando Directorio')
    directorio_nuevo = 'Desktop/C.201906051_Proyecto1'
    os.mkdir(directorio_nuevo)

salir = False
while salir == False:
    print("------ Menu Inicial ------")
    print("1. Cargar Menu")
    print("2. Cargar Orden")
    print("3. Generar Menu")
    print("4. Generar Factura")
    print("5. Generar Arbol")
    print("6. Salir")
    option = int(input("Ingresar Opcion: "))
    if option == 1:
        cargar_menu()
    elif option == 2:
        cargar_factura()
    elif option == 3:
        pagina_menu()
        pagina_token()
    elif option == 4:
        pagina_factura()
        pagina_errores()
    elif option == 5:
        generar_arbol()
    elif option == 6:
        datos_personales()
        salir = True
    else:
        print("Syntax Error  --  Saliendo del Programa")
        exit()
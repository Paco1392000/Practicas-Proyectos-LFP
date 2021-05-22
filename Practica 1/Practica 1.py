from tkinter import filedialog
from collections import Counter
from collections import defaultdict
import webbrowser
import os

absFilePath = os.path.abspath(__file__)
path, directorio = os.path.split(absFilePath)
lele = ("La direccion es {} y el nombre es {}".format(path, directorio))
pathmod = path.replace('\\', '/')

archivo_contenido = []
part2 = []#Obtener partes
part3 = []#Obtener partes
part4 = []#Obtener partes
part5 = []#Obtener partes
part6 = []#Obtener partes
part7 = []#Obtener partes
part8 = []#Obtener partes
part9 = []#Obtener partes
part10 = []#Obtener partes
part11 = []#Obtener partes
part12 = []#Obtener partes
l_copy = []#copia de la lista
perof = []#copia de lista
Tamano = 0#tamaño de lista
titulo = []#titulos
lista = []#listas
lista2 = []#listas
listacor = []
lista_cop2 = []
ea = 0
eo = 0
ea2 = 0
eo2 = 0
lista_copia = []#copia lista
lista_copia2 = []#copia lista
contenido = []#contenido de lista
instrucciones = []#instrucciones de lista
instruc1 = []#instrucciones primeras
instruc2 = []#instrucciones segundas
lista_ordenada = []
lista_ordenada2 = []
busquedas = []
busquedas2 = []
lista_busqueda = []
lista_busqueda2 = []
#-------------------------------------Primer Parte----------------------------------------------------
def bubble_sort(lista_cop):#Metodo de arreglo primeras ordenes ""
    global lista_ordenada, lista_copia, ea, listacor
    listacor = listacor
    ea = ea 
    lista_ordenada = lista_ordenada
    lista_copia = lista_copia
    cantidad = len(lista_copia)
    for eb in range(cantidad):
        if lista_copia[eb] == lista_copia[ea]:
            for j in range(len(lista_cop)):
                for k in range(len(lista_cop) - 1):
                    if lista_cop[k] > lista_cop[k + 1]:
                        lista_cop[k], lista_cop[k + 1] = lista_cop[k + 1], lista_cop[k]
    for eb in range(cantidad):
        if lista_copia[eb] == lista_copia[ea]:
            lista_copia[ea][1] = lista_cop    
    lista_ordenada.append(titulo[ea])
    lista_ordenada.append(lista_cop)
    return lista_ordenada

def ordenar_lista(i): #Metodo ordenar primera parte
    global lista_copia, ea, part11
    part11 = part11
    lista_copia = lista_copia
    ea = ea
    for eb in range(len(lista)):
        if lista[eb] == lista[i]:
            l_copy = lista_copia[eb][1]
            for ed in range(len(l_copy)):
                if l_copy[ed] == '':
                    l_copy.pop(ed)
                    l_copy = [int(j) for j in l_copy]
                    lista_copia[eb][1] = l_copy
                    lista[eb] = lista_copia[eb]
                    ea = eb
                    bubble_sort(l_copy)
       
def busqueda_lista(i):#Busqueda en 1°
    global busquedas, lista_copia, eo, lista_busqueda
    lista_busqueda = lista_busqueda
    lista_copia = lista_copia
    eo = eo
    busquedas = busquedas
    for eb in range(len(lista)):
        if busquedas[eb] == busquedas[i]:
            l_copy = lista_copia[eb][1]
            for ed in range(len(l_copy)):
                if l_copy[ed] == '':
                    l_copy.pop(ed)
                    eo = ed
                    l_copy = [int(j) for j in l_copy]
                    busquedas[eb][1] = l_copy 
                    eo = eb
                    les = int(instruc1[eb][1])
                    inte = les
                    if (inte in l_copy) == True:
                        kl = [ks for ks,x in enumerate(l_copy) if x == les]
                        lista_busqueda.append(busquedas[eb][0])
                        lista_busqueda.append(kl)   
                    else:
                        lista_busqueda.append(busquedas[eb][0])
                        lista_busqueda.append('No Encontrado')
    return lista_busqueda
#-------------------------------------Segunda Parte--------------------------------------------------- 
def bubble_sort2(lista_cop):#Metodo de arreglo primeras ordenes ""
    global lista_ordenada2, lista_copia2, ea2, listacor
    listacor = listacor
    ea2 = ea2 
    lista_ordenada2 = lista_ordenada2
    lista_copia2 = lista_copia2
    cantidad = len(lista_copia2)
    for eb in range(cantidad):
        if lista_copia2[eb] == lista_copia2[ea2]:
            for j in range(len(lista_cop)):
                for k in range(len(lista_cop) - 1):
                    if lista_cop[k] > lista_cop[k + 1]:
                        lista_cop[k], lista_cop[k + 1] = lista_cop[k + 1], lista_cop[k]
    for eb in range(cantidad):
        if lista_copia2[eb] == lista_copia2[ea2]:
            lista_copia2[ea2][1] = lista_cop    
    lista_ordenada2.append(titulo[ea2])
    lista_ordenada2.append(lista_cop)
    return lista_ordenada2

def ordenar_lista2(i): #Metodo ordenar segunda parte
    global lista_copia2, ea2, part11
    part11 = part11
    lista_copia2 = lista_copia2
    ea2 = ea2
    for eb in range(len(lista2)):
        if lista2[eb] == lista2[i]:
            l_copy = lista_copia2[eb][1]
            for ed in range(len(l_copy)):
                if l_copy[ed] != ' ':
                    l_copy = [int(j) for j in l_copy]
                    lista_copia2[eb][1] = l_copy
                    lista2[eb] = lista_copia2[eb]
                    ea2 = eb
                    bubble_sort2(l_copy)
       
def busqueda_lista2(i):#Busqueda en 2°
    global busquedas2, lista_copia2, eo2, lista_busqueda2
    lista_busqueda2 = lista_busqueda2
    lista_copia2 = lista_copia2
    eo2 = eo2
    busquedas2 = busquedas2
    for eb in range(len(lista2)):
        if busquedas2[eb] == busquedas2[i]:
            l_copy = lista_copia2[eb][1]
            for ed in range(len(l_copy)):
                if l_copy[ed] != ' ':
                    eo2 = ed
                    l_copy = [int(j) for j in l_copy]
                    busquedas2[eb][1] = l_copy 
                    eo2 = eb
                    les = int(instruc2[eb][1])
                    inte = les
                    if (inte in l_copy) == True:
                        kl = [ks for ks,x in enumerate(l_copy) if x == les]
                        lista_busqueda2.append(busquedas2[eb][0])
                        lista_busqueda2.append(kl)
                    else:
                        lista_busqueda2.append(busquedas2[eb][0])
                        lista_busqueda2.append('No Encontrado')
                    
    return lista_busqueda2
#-----------------------------Procedimiento Programa--------------------------
def cargar_archivo():
    global archivo_contenido, titulo, lista, instrucciones, part2, part3, part4, part5, part6, part7, part8, part9, part10, part11, Tamano
    global instruc1, instruc2, l_copy, lista_copia, perof, part12, busquedas, lista2, lista_copia2, busqueda_lista2
    lista2 = lista2
    lista_copia2 = lista_copia2
    busqueda_lista2 = busqueda_lista2
    busquedas = busquedas
    part12 = part12
    perof = perof
    lista_copia = lista_copia
    instrucciones = instrucciones
    l_copy = l_copy
    instruc1 = instruc1
    instruc2 = instruc2
    Tamano = Tamano
    lista = lista
    titulo = titulo
    part2 = part2
    part3 = part3
    part4 = part4
    part5 = part5
    part6 = part6
    part7 = part7
    part8 = part8
    part9 = part9
    part10 = part10
    part11 = part11
    archivo_contenido = archivo_contenido
    print('....................................')
    print('----------CARGANDO ARCHIVO----------')
    print(' ---------------------------------- ')
    
    nom_archivo = filedialog.askopenfilename()
    try:
        if nom_archivo != '':
            archivo = open(nom_archivo, 'r', encoding='utf-8')
            content = archivo.read()
            archivo_contenido = content.split('\n')
            Tamano = len(archivo_contenido)
            for i in range(len(archivo_contenido)):
                part1 = archivo_contenido[i].split('=')
                titulo.append(part1[0])
                part2.append(part1[1])
            for i in range(len(archivo_contenido)):
                part3.append(','.join(part2[i].split(',')[0:-2]).replace(' ', ''))#lista//Contenido
                part4.append(part2[i].split(',')[-2:])
            for i in range(0, Tamano):
                part5.append(part4[i][0].split()[0])#Continuación Lista p1
                part6.append(' '.join(part4[i][0].split()[1:]))#Ordenes
                part7.append(part4[i][1].split(' ')[0])#Continuación Lista p2
                part8.append(' '.join(part4[i][1].split(' ')[-2:]))#Ordenes 2
                part10.append(' '.join(part4[i][1].split(' ')[-2:]).split(' '))
                part3[i]+= ',' + part5[i] + ',' + part7[i]#Lista Full
                part9.append(' '.join(part4[i][0].split()[1:]).split(' '))
                part6[i] += ',' + part8[i]
            for i in range(0, Tamano):
                perof.append(part3[i].splitlines())
                part12.append(perof[i][0].split(','))
                l_copy.append(part12[i])
                lin = l_copy[i]
                lista.append(titulo[i].splitlines() + part3[i].splitlines() + part6[i].splitlines())
                lista[i][1] = lin
                lista2.append(titulo[i].splitlines() + part3[i].splitlines() + part6[i].splitlines())
                lista2[i][1] = lin
                lista_copia.append(titulo[i].splitlines() + part3[i].splitlines() + part6[i].splitlines())
                lista_copia[i][1] = lin
                lista_copia2.append(titulo[i].splitlines() + part3[i].splitlines() + part6[i].splitlines())
                lista_copia2[i][1] = lin
                busquedas.append(titulo[i].splitlines() + part3[i].splitlines())
                busquedas[i][1] = lin
                busquedas2.append(titulo[i].splitlines() + part3[i].splitlines())
                busquedas2[i][1] = lin
            instrucciones = part6
            instruc1 = part9
            instruc2 = part10
            archivo.close()
            print('.          .           .           .')
            print('-----------ARCHIVO LEIDO------------')
            print(' -                                - ')
            for i in range(0, Tamano):
                if instruc1[i][-1] == 'ORDENAR':
                    ordenar_lista(i)
                elif instruc1[i][-1] == '':
                    continue
                elif instruc1[i][-2] == 'BUSCAR':
                    busqueda_lista(i)
            for i in range(0, Tamano):
                if instruc2[i][-1] == 'ORDENAR':
                    ordenar_lista2(i)
                elif instruc2[i][-2] == 'BUSCAR':
                    busqueda_lista2(i)           
    except:
        print('Error')
            
def pagina():
    f = open('Reporte.html', 'w')
    f.write("<DOCTYPE html>\n")
    f.write("<head>\n")
    f.write("<meta charset=\"UTF-8>\n")
    f.write("<title>Reporte 1</title>\n")
    f.write("<head>\n")
    f.write("<body background=\"blue\">\n")
    f.write("<div id=\"encabezado\"> <header><center><h2>Reporte Practica 1 LFP</h2></center>")
    f.write("</header></div><hr border=\"2\"><h3>Listados Ordenados</h3>")
    f.write("<div id=\"table1-container\">\n")
    f.write("<center><table><thead><tr><th>Listado Ordenado</th></tr></thead><tbody>")
    f.write(str(lista_ordenada))
    f.write(str(lista_ordenada2))
    f.write("</tbody></table></center></div><h3>Listado Objetos Buscados</h3><div id=\"table1-container\"><center><table><thead><tr>")
    f.write("<th>Listado</th><th>Posicion</th></thead><tbody>")
    f.write(str(lista_busqueda))
    f.write(str(lista_busqueda2))
    f.write("</tbody></table></center></div></body>")
    f.write("<footer><h4 align=\"right\">Carne - Alumno</h4></footer>")
    f.close()
    os.startfile("Reporte.html")


def opciones():
    corr = False
    numero = 0
    while(not corr):
        try:
            numero = int(input("Opcion a Elegir: "))
            corr = True
        except:
            print("Error")
    return numero

op = 0
salir = False

while not salir:
    
    print('')
    print ('   Menu Opciones')
    print('1. Cargar Archivo')
    print('2. Desplegar Listas Ordenadas')
    print('3. Desplegar Búsquedas')
    print('4. Desplegar Todo')
    print('5. Desplegar Todas a Archivo')
    print('6. Salir')
    print('')
    op = opciones()
    if op == 1:
        cargar_archivo()
    elif op == 2:
        print('....................................')
        print('----------LISTAS ORDENADAS----------')
        print(' ---------------------------------- ')
        print(lista_ordenada)
        print(lista_ordenada2)
    elif op == 3:
        print('....................................')
        print('-----------BUSQUEDA LISTA-----------')
        print(' ---------------------------------- ')
        print(lista_busqueda)
        print(lista_busqueda2)
    elif op == 4:
        print('....................................')
        print('----------LISTAS ORDENADAS----------')
        print(' ---------------------------------- ')
        print(lista_ordenada)
        print(lista_ordenada2)
        print('....................................')
        print('-----------BUSQUEDA LISTA-----------')
        print(' ---------------------------------- ')
        print(lista_busqueda)
        print(lista_busqueda2)
    elif op == 5:
        pagina()
    elif op == 6:
        print('Fin del Programa')
        exit()
    else:
        print('Error - Vuelva a intentar')



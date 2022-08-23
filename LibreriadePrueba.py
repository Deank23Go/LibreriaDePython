import sys
#varibles reservadas para el registro de libros
titulos =[]
autores =[]
fechas = []
editoriales =[]
codigos =[]
precios =[]
cantidades = []
#varibles reservadas para el registro de las revistas
nombres=[]
fechas_revistas=[]
editores = []
codigo_revista =[]
precios_revista =[]
#Variables Aumentan/acumuladas en la Opcion #3
indices = 0
totales = 0

def libros():
    input('\n=======Registro de Libros=======')
    titulo= input('titulo del libro: ')
    autor = input('autor del libro: ')
    fecha = input('fecha de publicacion del libro: ')
    editorial = input('editorial del libro: ')
    codigo = int(input('codigo de referencia: '))
    precio = float(input('precio del libro: '))
    cantidad = 0.0
    titulos.append(titulo)
    autores.append(autor)
    fechas.append(fecha)
    editoriales.append(editorial)
    codigos.append(codigo)
    precios.append(precio)
    cantidades.append(cantidad)
def revistas():
    input('\n=======Registro de revistas======')
    nombre= input('nombre de la revista: ')
    editor = input('editor de la revista: ')
    fecha_re= input('fecha de publicacion de la revista: ')
    codidor = int(input('codigo de referencial: '))
    precio_re = float(input('precio de la revista: '))
    nombres.append(nombre)
    editores.append(editor)
    fechas_revistas.append(fecha_re)
    codigo_revista.append(codidor)
    precios_revista.append(precio_re)
def IMPRIMIR():
    print("/=====================================================/")
    print("|NOMBRE              |CANT.     |PRECIO    |IMPORTE   |")
    print("/=====================================================/")
def vacio():
    print("|--------------------+----------+----------+----------|")
    print('|===========No Hay Articulos Disponibles==============|')
    print("|--------------------+----------+----------+----------|")

        



while True:
    print("""""
    menu de Nuestra libreria

    """)
    elecion = input("""""
    1 - Registrar Un  nuevo libro o Revista
    2 - Hacer Compra de libros o Revistas
    3 - Mostrar información
    4 - Borrar un artículo
    5 - Salir
    Seleccione:   """)

    if elecion == "1":
        if input('Desea registrar (l/r): ') =="l":
            libros()
        else:
            revistas()

    elif elecion == "2":
        if input('Que deseas Comprar (l / r): ')  == "l":
            nombre_libro = input('Nombre del libro a comprar: ')
            if nombre_libro in titulos:
                if input('Desea fisico o copis (f / c): ') == "f":
                    cantidadw = float(input('Cuantas copias fisicas necesita? : '))
                    indice = titulos.index(nombre_libro)
                    precio = precios[indice]
                    porcen = (18/100)
                    automento_de = precios[indice] * porcen
                    total = precio + automento_de
                    cantidades[indice] += cantidadw
                    print('+++++++++++++++++++++++Total de Pagar+++++++++++++++++++++++++++++')
                    print(f"Se vendieron {cantidadw} copias del libro de {nombre_libro} en fisico. Total: {cantidadw * total}")
                    print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
                else:
                    cantidadw = float(input('Cuantas copias digitales necesita? : '))
                    indice = titulos.index(nombre_libro)
                    precio = precios[indice]
                    porcen = (8 / 100)
                    automento_de = precios[indice] * porcen
                    total = precio + automento_de
                    cantidades[indice] += cantidadw
                    print('+++++++++++++++++++++++Total de Pagar+++++++++++++++++++++++++++++')
                    print(f"Se vendieron  {cantidadw} copias del libro de {nombre_libro} digitales. Total: {cantidadw * total}")
                    print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')

        else:
            nombre_libro = input('Nombre del libro a comprar: ')
            if input('Desea fisico o copis (f / c): ') == "f":
                cantidadw = float(input('Cuantas copias fisicas necesita? : '))
                indice = nombres.index(nombre_libro)
                precio = precios[indice]
                porcen = (22/100)
                automento_de = precios[indice] * porcen
                total = precio + automento_de
                cantidades[indice] += cantidadw
                print('+++++++++++++++++++++++++++++++Total de Pagar+++++++++++++++++++++++++++++')
                print(f"""Se vendieron  {cantidadw} copias de revistas de {nombre_libro} en fisico  . Total: {cantidadw * total}""")
                print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
            else:
                cantidadw = float(input('Cuantas copias digitales necesita? : '))
                indice = nombres.index(nombre_libro)
                precio = precios[indice]
                porcen = (12 / 100)
                automento_de = precios[indice] * porcen
                total = precio + automento_de
                cantidades[indice] += cantidadw
                print('+++++++++++++++++++++++++++++++Total de Pagar+++++++++++++++++++++++++++++')
                print(f"""Se vendieron {cantidadw} copias de revistas de {nombre_libro} digitales. Total: {cantidadw * total}""")
                print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')


    elif elecion == "3":
        if len(titulos) and len(nombres) <=0:
            vacio()
            continue
        
        if input('Desea ver la informacion del los libros o revistas (l/r): ') == "l":
            
            IMPRIMIR()
            while indices < len(titulos):
                titulo = titulos[indices]
                precio = precios[indices]
                cantidad = cantidades[indices]
                importe = precio * cantidad
                print('|{:<20}|{:>10.2f}|{:>10.2f}|{:>10.2f}|'.format(
                            titulo, cantidad, precio, importe))
                print('+=============+===========+===========+==========+====')
                totales += importe
                indices += 1
        else:
            IMPRIMIR()
            while indices < len(nombres):
                nombre = nombres[indices]
                precio = precios_revista[indices]
                cantidad = cantidades[indices]
                importe = precios_revista * cantidad
                print('|{:<20}|{:>10.2f}|{:>10.2f}|{:>10.2f}|'.format(
                            nombre, cantidad, precio, importe))
                print('+=============+===========+===========+==========+====')
                totales += importe
                indices += 1



    elif elecion == "4":

        if input('que tipo de registro desea eliminar (r / l) : ') =="r":
            nombre_libro = input('Digitar el nombre del libro o revista a eliminar : ')
            if nombre_libro in nombres:
                indexx = nombres.index(nombre_libro)
                del nombres[indexx]
                del fechas_revistas[indexx]
                del editores[indexx]
                del codigo_revista[indexx]
                del precios_revista[indexx]
                print(f'se ha Eliminado la revista {nombre_libro}')
            else:
                print(f'no es posible la eliminacion del registro')
        else:
            if nombre_libro in titulos:
                indexx = titulos.index(nombre_libro)
                del titulos[indexx]
                del autores[indexx]
                del fechas[indexx]
                del editoriales[indexx]
                del codigos[indexx]
                del precios[indexx]
                del cantidades[indexx]
                print(f'se ha Eliminado la revista {nombre_libro}')
            else:
                print(f'no es posible la eliminacion del registro')



    elif elecion == "5":
        if input(" * Seguro (s/n) : ") == "s":
            print('  * Ahs salido de nuestro servicios * ')
            print('  * Que tengo un feliz Dia *_* :B *')
            sys.exit()
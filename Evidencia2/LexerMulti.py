import os
import time

start_time = time.time()
#esta funcion, gracias a la magica libreria de os, nos ayuda a encontrar todas las files
#que terminen en .py
def find_python_files(folder_path):
    python_files = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".py"):
                ruta_completa = os.path.join(root, file)
                python_files.append(ruta_completa)
    return python_files

#accedemos al directorion en el que estamos trabajando para de ahi poder
#llegar al folder que queremos y cambiamos el directorio al deseado, 
#en este caso queremos, del working dir, acceder a Evidencia2/SAMPLEFOLDER
currentWorkDir=os.getcwd()
folder_path = os.path.join(currentWorkDir, 'Evidencia2', 'SAMPLEFOLDER')


#guardamos todas las direcciones en una lista
pathlist=[]
python_files = find_python_files(folder_path)
for file in python_files:
    pathlist.append(file)

#casi todo lo relacionado a la evidencia 1 se queda igual, salgo algunas cosas en las
#que necesitabamos codigo mas flexible, como la generacion de html's
tabla = [[0,1,5,12,6,13,7,8,16,2,17,5,16,5,0],
         [9,1,9,9,9,9,9,9,9,2,9,9,9,9,9],
         [10,2,10,10,10,10,10,10,10,10,10,3,10,10,10],
         [10,3,10,10,10,10,10,10,10,10,10,10,4,10,10],
         [10,4,10,10,10,10,10,10,10,10,10,10,10,10,10],
         [11,5,5,11,11,11,11,11,11,11,11,5,11,5,11],
         [6,6,6,6,6,6,6,6,6,6,6,6,6,6,14],
         [7,7,7,7,7,7,15,7,7,7,7,7,7,7,17],
         [8,8,8,8,8,8,8,15,8,8,8,8,8,8,17]
        ]
def lexerAritmetico(path):
    with open(path, 'r') as file:
        code = file.read()

    estado = 0
    htmlinsertion=""
    p = 0
    lexema = ''
    token = ''
    num = "0123456789"
    letras = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ" #no incluye E ni e
    Ee= "Ee"
    blanco = ' '
    keywords = [
                'or','and','not','assert','with','def','include','string','bool', 'int', 'float', 'char', 'double', 'long', 'if', 'else', 'switch', 'case', 'for', 'while', 'do',
                'break', 'continue', 'return', 'void', 'const', 'static', 'public', 'private', 'protected', 'None', 'write', 'async', 'in', 'range', 'print', 'del', 'pass', 'raise', 'except', 'finally', 'from', 'nonlocal', 'global', 'is', 'lambda', 'yield', 'match', 'run',
                'class', 'struct', 'union', 'enum', 'typename', 'namespace', 'using', 'virtual', 'as', 'await',
                'override', 'this', 'nullptr', 'True', 'False', 'new', 'delete', 'try', 'catch', 'throw',
                'template', 'friend', 'inline', 'operator', 'explicit', 'constexpr', 'mutable',
                'register', 'volatile', 'asm', 'export', 'import', 'sizeof', 'dynamic_cast',
                'static_cast', 'reinterpret_cast', 'const_cast', 'typeid', 'decltype', 'noexcept', 
                ';', '::', '->', '?','<<','>>'
                ]
    opening = ['(', '[', '{']
    closing = [')', ']', '}']
    
    operators = [
                '=','+', '*', '/', '%', '++', '--', '=', '+=', '-=', '*=', '/=', '%=', '==', '!=', '>', '<', '>=', '<=',
                '&&', '||', '!', '^',':',','
                ] #no incluye -
    
    while p<len(code) and estado != 17:
        c = code[p]

        if c in blanco:
            col = 0
        elif c in num:
            col = 1
        elif c in letras:
            col = 2
        elif c in opening:
            col = 3
        elif c == '#':
            col = 4
        elif c in closing:
            col = 5
        elif c == '"':
            col = 6
        elif c == "'":
            col = 7
        elif c in operators:
            col = 8
        elif c in '.':
            col = 9
        elif c in Ee:
            col = 11
        elif c == '-':
            col = 12
        elif c == '_':
            col = 13
        elif c == "\n":
            if not htmlinsertion.endswith("<br>"):
                htmlinsertion += "<br>"
            col = 14
        else:
            col = 10

        estado = tabla[estado][col]
        if estado == 9:
            token = 'Int'
            htmlinsertion += "<span style='color:red'>{}</span>".format(lexema)
            print(lexema, token)
            lexema = ''
            estado = 0
            p -= 1
        elif estado == 10:
            token = 'Float'
            htmlinsertion += "<span style='color:purple'>{}</span>".format(lexema)
            print(lexema, token)
            lexema = ''
            estado = 0
            p -= 1
        elif estado == 11:
            if lexema in keywords:
                token = 'keyword'
                htmlinsertion += "<span style='color:blue'>{}</span>".format(lexema)
                print(lexema, token)
            else:
                token = 'variable'
                htmlinsertion += "<span style='color:lightblue'>{}</span>".format(lexema)
                print(lexema, token)
            lexema = ''
            estado = 0
            p -= 1
        elif estado == 12:
            token = 'Opening symbol'
            lexema=c
            htmlinsertion += "<span style='color:yellow'>{}</span>".format(lexema)
            print(lexema, token)
            lexema = ''
            estado = 0
        elif estado == 13:
            token = 'Closing symbol'
            lexema=c
            htmlinsertion += "<span style='color:yellow'>{}</span>".format(lexema)
            print(lexema, token)
            lexema = ''
            estado = 0
        elif estado == 14:
            token = 'Comment'
            
            htmlinsertion += "<span style='color:green'>{}</span><br>".format(lexema)
            print(lexema, token)
            lexema = ''
            estado = 0
        elif estado == 15:
            token = 'String'
            htmlinsertion += "<span style='color:orange'>{}</span>".format(lexema)
            print(lexema, token)
            lexema = ''
            estado = 0
        elif estado == 16:
            token = 'Operator'
            lexema=c
            htmlinsertion += "<span style='color:purple'>{}</span>".format(lexema)
            print(lexema, token)
            lexema = ''
            estado = 0
        elif estado == 17:
            htmlinsertion += "<span style='color:red'>{}</span>".format("ERROR")
            print('Error')
        p += 1
        if estado != 0:
            lexema += c 
            
    htmlcode="""
            <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Document</title>
        </head>
        <body>
            {}
        </body>
        </html>

        """.format(htmlinsertion)

    #conseguimos el current working path y le adjuntamos un nombre construido por el 
    #nombre del archivo py +.html
    folder_path = os.path.join(currentWorkDir, 'Evidencia2', 'HTMLs')
    os.chdir(folder_path)
    filename = os.path.basename(path)
    filename+='.html'
    folder_path+=filename

    #abrimos un file que posiblemente no exista, con w+ lo creamos y escribimos sobre el
    with open(filename, 'w+') as file:
        file.write(htmlcode)

    os.chdir(currentWorkDir)


#por cada path encontrado anteriormente, ejecutamos la funcion, pasando el path de la lista como parametro
#revisamos el tiempo desde aqui, pues es el proceso que nos interesa analizar.

for path in pathlist:
    lexerAritmetico(path)
end_time=time.time()

print(end_time-start_time)

"""
La forma de acceder y moverse entre directorios es diferente, pues aqui, como estamos en el
mismo programa, si cambiamos de directorio para hacer alguna task, debemos regresar al directorio
original, pues las acciones de una iteracion pueden afectar a todo el programa.

Esto no funciona asi en el programa paralelo, pues cada proceso es independiente y no afecta a los otros.
"""
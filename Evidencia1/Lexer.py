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

    with open('resaltador.html', 'w') as file:
        file.write(htmlcode)
            
lexerAritmetico('samplecode.py')


def validar_numero(mensaje, mensaje_error):
    valor = False
    while valor == False:
        entrada = input(mensaje)
        digito_op = True

        if len(entrada) == 0:
            digito_op = False
        else:
            for caracter in entrada:
                if caracter>='0' and caracter<='9':
                    pass
                else:
                    digito_op = False
        
        if digito_op == True:
            numero = int(entrada)
            if numero>0:
                valor =True
            else:
                print(mensaje_error)
                valor = True
        else:
            print(mensaje_error)
            valor =False

    return numero        



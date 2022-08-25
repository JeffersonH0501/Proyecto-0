# -*- coding: utf-8 -*-
"""
Created on Fri Aug 19 11:12:04 2022

@author: Jefferson
"""

"""
Leer codigo
"""

def verificarSyntaxis(programa):
    
    variables = []
    nombresfunciones = []
    
    if programa[:4] == "PROG" and programa[-4:] == "GORP":
        programa = programa[4:-4]
        
        palabra = ""
        for caracter in programa:
            
            if caracter == "{": #Para entrar al ultimo bloque
                break
            
            programa = programa[1:]
            palabra += caracter
            
            if palabra == "VAR":
                validez = funcionVAR(programa)
                if validez[1] == False:
                    return False
                programa = validez[0]
                variables = validez[2]
                
            elif palabra == "PROC":
                validez = funcionPROC(programa, variables)
                if validez[1] == False:
                    return False
                programa = validez[0]
                nombresfunciones += [validez[2]]
            
            palabra = ""
        
        
        instrucciones = validarbloquePROG(programa)
        if instrucciones[1] == False:
            return "Error"
        
        programa = instrucciones[0]
        print(programa)
        return "No errores"
               
    elif programa[:4] != "PROG" and programa[-4:] == "GORP":
        return False
    
    elif programa[:4] == "PROG" and programa[-4:] != "GORP":
        return False


def funcionVAR(programa):
    
    variables = []
    
    nombre = ""
    for caracter in programa:
        programa = programa[1:]
        
        if caracter == ",":
            if validarnombre(nombre) == False:
                return programa, False
            variables += [nombre]
            nombre = ""
        elif caracter == ";":
            if validarnombre(nombre) == False:
                return programa, False
            variables += [nombre]
            break
        
        nombre += caracter
        
    return programa, True, variables


def funcionPROC(programa, variables):
    
    nombre = ""
    for caracter in programa:
        programa = programa[1:]
        
        if caracter == "(":
            if validarnombre(nombre) == False:
                return programa, False, nombre
            break
        nombre += caracter
    
    parametros = []
    parametro = ""
    for caracter in programa:
        programa = programa[1:]
        
        if caracter == ")" and parametro == "":
            return programa, True, nombre
        
        if caracter == ",":
            if validarparametros(parametro) == False:
                return programa, False, nombre
            parametros = [parametro]
            parametro = ""
        elif caracter == ")":
            if validarparametros(parametro) == False:
                return programa, False, nombre
            parametros = [parametro]
            break
        parametro += caracter
    
    for caracter in programa: #///////////////////////////////////////////////////////////////////
        
        if caracter == "{":
            programa = programa[1:]
            validar = validarbloquePROC(programa, parametros, variables)
            if validar[1] == False:
                return programa, False, nombre
            programa = validar[0]
    
    return programa, True, nombre

def validarnombre(nombre):
    
    if nombre.isalnum() == False:
        return False
    elif nombre[0].isalpha() == False:
        return False
    else:
        return True

def validarparametros(parametro):
    
    if parametro.isalpha() == False:
        return False
    else:
        return True

def validarbloquePROC(programa, parametros, variables):
    
    comandos = ["walk","jump","jumpTo","veer","look"
                "drop","grab","get","free","pop"]
    
    condicionales = ["while","do","if","else"]
    
    condiciones = ["isfacing","isValid","canWalk", "not"]
    
    orientacion = ["north","south","east","west"]
    
    movimiento = ["right","left","front","back"]
    
    ins = ["walk","jump","pop","pick","free","drop"]
    
    
    
    funcion = ""
    for caracter in programa:
        programa = programa[1:]
        funcion += caracter
        
        if caracter == "(":
            
            
            if funcion[:-1] in comandos:
                
                parametro = ""
                for caracterparametro in programa:
                    programa = programa[1:]
                    parametro += caracterparametro
                    if caracterparametro == ")":
                        if parametro[:-1] not in parametros:
                            return programa, False
                        parametro = ""
                    elif caracterparametro == ";":
                        if parametro != "":
                            return programa, False
                    elif caracterparametro == "}":
                        return programa, True
                    break
                funcion = ""
                
                
                
            elif funcion[:-1] in condicionales:
                
                if funcion[:-1] == "while":
                    
                    condicion = ""
                    for caractercondicion in programa:
                        programa = programa[1:]
                        if caractercondicion == "(":
                            if condicion not in condiciones:
                                return programa, False
                            programa = validarcondicion(programa, condicion)
                            break
                        condicion += caractercondicion
        
                    if programa[:4] != ")do{":
                        return programa, False
                    programa = programa[:4]
                    
                    comando = ""
                    for caractercomando in programa:
                        programa = programa[1:]
                        if caractercomando == "(":
                            if comando not in comandos:
                                return programa, False
                            programa = validarcomandos(programa, comando)
                            break
                        comando += caractercomando
                    
                    if programa[:4] != "}od}":
                        return programa, False
    
                    
                            
                elif funcion[1:-1] == "if":
                    condicion = ""
                    for caractercondicion in programa:
                        programa = programa[1:]
                        if caractercondicion == "(":
                            if condicion not in condiciones:
                                return programa, False
                            programa = validarcondicion(programa, condicion)
                            break
                        condicion += caractercondicion
                    
                    if programa[:2] != "){":
                        return programa, False
                    programa = programa[:2]
                    
                    comando = ""
                    for caractercomando in programa:
                        programa = programa[1:]
                        if caractercomando == "(":
                            if comando not in comandos:
                                return programa, False
                            programa = validarcomandos(programa, comando)
                            break
                        comando += caractercomando
                    
                    if programa[:4] != "}fi}":
                        return programa, False

            else:
                return programa, False
        
    pass


#Valida los parametos de la condicion
def validarcondicion(programa, condicion):
    pass

#Valida los parametos del comando
def validarcomandos(programa, comando):
    pass


def validarbloquePROG(programa, variables, nombrefunciones):
    pass


def leerarchivo():
    
    programa = open("prueba.txt", "r").read().replace("\n", "").replace("\t", "").replace(" ","")
    print(programa)
    validez = verificarSyntaxis(programa)
    if validez == "True":
        return "El programa no tiene problemas de sintaxis"
    else:
        return "Error: el programa tiene problema/s de sistanxis"
    
leerarchivo()



    

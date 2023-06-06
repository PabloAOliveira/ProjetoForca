import os
import time

def limparTela():
    os.system("cls")

def esperarSegundos(segundos=1):
    time.sleep(segundos)

def soma(numero1, numero2):
    soma = numero1 + numero2
    return 

def lerString(mensagem):
    while True:
        variavel = input(mensagem)
        if len(variavel)>1:
            return variavel
        else:
            print("Valor informado incorretamente!")



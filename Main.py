from colorama import Fore, Style
from Queue import Queue

def Menu():
    print(Style.BRIGHT, Fore.LIGHTMAGENTA_EX)
    print('|---    **********************************   ---|',end='')
    print(Fore.LIGHTYELLOW_EX,Style.NORMAL)
    print('|---'+Fore.LIGHTCYAN_EX+Style.BRIGHT+'         🍕[ Josue\'s Pizzas ]🍕         '+Fore.LIGHTYELLOW_EX,Style.NORMAL+'---|')
    print('|---    1) Generar pedido                    ---|')
    print('|---    2) Enviar al horno                   ---|')
    print('|---    3) Ver pizzas pendientes             ---|')
    print('|---    4) Datos de desarrollador            ---|')
    print('|---    5) Salir                             ---|',Fore.LIGHTMAGENTA_EX,Style.BRIGHT)
    print('|---    **********************************   ---|')

def Menu2():
    print(Style.NORMAL, Fore.LIGHTMAGENTA_EX)
    print('|---    **********************************   ---|',end='')
    print(Fore.LIGHTYELLOW_EX,Style.NORMAL)
    print('|---    1) Ingresar nombre de cliente        ---|')
    print('|---    2) Seleccionar ingredientes          ---|')
    print('|---    3) Seleccionar cantidad de pizzas    ---|')
    print('|---    4) Regresar                          ---|',Fore.LIGHTMAGENTA_EX,Style.NORMAL)
    print('|---    **********************************   ---|')

def Ingredientes():
    print(Fore.LIGHTWHITE_EX+'\n|-----------------------------------------------|')
    print(Fore.LIGHTBLUE_EX+Style.BRIGHT+'|-------[🍴 Ingredientes de la casa 🍴]---------|'+Fore.LIGHTWHITE_EX)
    print('|-----------------------------------------------|')
    print('|---     Pepperoni -----|-----   3 min       ---|')
    print('|---     Salchicha -----|-----   4 min       ---|')
    print('|---     Carne     -----|-----   10 min      ---|')
    print('|---     Queso     -----|-----   5 min       ---|')
    print('|---     Piña      -----|-----   2 min       ---|')
    print('|-----------------------------------------------|')

queue = Queue()
Menu()
aux=input(Fore.GREEN+'Ingrese una opcion: ')
time=0
while(aux != '5'):
    if aux == '1':
        Menu2()
        op = input(Fore.LIGHTBLACK_EX+Style.BRIGHT+'Eliga una opcion: ')
        while(op != '4'):
            if op == '1':
                name=''
                name = input(Fore.GREEN+Style.BRIGHT+'Ingrese nombre: ')
                Menu2()
                op = input(Fore.LIGHTBLACK_EX+'Eliga una opcion: ')
            elif op == '2':
                Ingredientes()
                op2 = input(Fore.GREEN+'¿Cuantos ingredientes desea?: ')
                time = 0
                for i in range(int(op2)):
                    ingredientes = input(Fore.GREEN+'Ingrese ingrediente '+str(i+1)+': '+Fore.LIGHTWHITE_EX)
                    if ingredientes.lower() == 'pepperoni':
                        time +=3
                    elif ingredientes.lower() == 'salchicha':
                        time +=4
                    elif ingredientes.lower() == 'carne':
                        time +=10
                    elif ingredientes.lower() == 'queso':
                        time +=5
                    elif ingredientes.lower() == 'piña':
                        time +=2
    
                Menu2()
                op = input(Fore.LIGHTBLACK_EX+'Eliga una opcion: ')
            elif op == '3':
                cant = input(Fore.GREEN+'Ingrese cantidad de pizzas: ')
                time = time * int(cant) 
                Menu2()
                op = input(Fore.LIGHTBLACK_EX+'Eliga una opcion: ')
            else:
                print(Fore.LIGHTRED_EX+Style.BRIGHT+'Ingrese un comando valido')
                Menu2()
                op = input(Fore.LIGHTBLACK_EX+'Eliga una opcion: ')
        Menu()
        aux=input(Fore.GREEN+'Ingrese una opcion: ')
    elif aux == '2':
        queue.Enqueue(name,cant,time)
        queue.Front()
        queue.Rear()
        Menu()
        aux=input(Fore.GREEN+'Ingrese una opcion: ') 
    elif aux == '3':
        queue.Report()
        queue.crearReporte()
        Menu()
        aux=input(Fore.GREEN+'Ingrese una opcion: ') 
    else:
        print(Fore.GREEN,'')
        aux=input('Ingrese una opcion: ')
exit



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
    print('|---    4) Sacar pizzas                      ---|')
    print('|---    5) Datos de desarrollador            ---|')
    print('|---    6) Salir                             ---|',Fore.LIGHTMAGENTA_EX,Style.BRIGHT)
    print('|---    **********************************   ---|')

def Menu2():
    print(Style.NORMAL, Fore.LIGHTMAGENTA_EX)
    print('|---    **********************************   ---|')
    print(Fore.LIGHTYELLOW_EX+Style.NORMAL+'|---'+Fore.LIGHTCYAN_EX+Style.BRIGHT+'       📝  GENERADOR DE ORDENES  📝'+Fore.LIGHTYELLOW_EX+Style.NORMAL+'      ---|')
    print('|---    1) Ingresar nombre de cliente        ---|')
    print('|---    2) Seleccionar ingredientes          ---|')
    print('|---    3) Seleccionar cantidad de pizzas    ---|')
    print('|---    4) Regresar                          ---|',Fore.LIGHTMAGENTA_EX,Style.NORMAL)
    print('|---    **********************************   ---|')

def Ingredientes():
    print(Fore.LIGHTWHITE_EX+Style.BRIGHT+'\n|-----------------------------------------------|')
    print(Fore.LIGHTBLUE_EX+Style.BRIGHT+'|-------[🍴 Ingredientes de la casa 🍴]---------|'+Fore.LIGHTWHITE_EX)
    print('|-----------------------------------------------|')
    print('|---     Pepperoni -----|-----   3 min       ---|')
    print('|---     Salchicha -----|-----   4 min       ---|')
    print('|---     Carne     -----|-----   10 min      ---|')
    print('|---     Queso     -----|-----   5 min       ---|')
    print('|---     Piña      -----|-----   2 min       ---|')
    print('|-----------------------------------------------|')

def Datos():
    print(Fore.LIGHTWHITE_EX+'\n|-----------------------------------------------|')
    print(Fore.LIGHTBLUE_EX+Style.BRIGHT+'|----------------[👾 '+Fore.LIGHTCYAN_EX+'iJosuer'+Fore.LIGHTBLUE_EX+Style.BRIGHT+' 👾]----------------|'+Fore.LIGHTWHITE_EX)
    print('|-----------------------------------------------|')
    print('|---        UNIVERSIDAD DE SAN CARLOS        ---|')
    print('|---         FACULTAD DE INGENIERIA          ---|')
    print('|---                 IPC2 B-                 ---|')
    print('|---      JOSUE ROLANDO GRAMAJO ROLDAN       ---|')
    print('|---                202000895                ---|')
    print('|-----------------------------------------------|')

queue = Queue()
Menu()
aux=input(Fore.GREEN+'Ingrese una opcion: '+Fore.LIGHTWHITE_EX)
time=0
while(aux != '6'):
    if aux == '1':
        Menu2()
        op = input(Fore.GREEN+Style.BRIGHT+'Eliga una opcion: '+Fore.LIGHTWHITE_EX)
        while(op != '4'):
            if op == '1':
                name=''
                name = input(Fore.LIGHTCYAN_EX+Style.BRIGHT+'-Ingrese nombre: '+Fore.LIGHTWHITE_EX)
                Menu2()
                op = input(Fore.GREEN+'Eliga una opcion: '+Fore.LIGHTWHITE_EX)
            elif op == '2':
                Ingredientes()
                op2 = input(Fore.LIGHTCYAN_EX+'¿Cuantos ingredientes desea?: '+Fore.LIGHTWHITE_EX)
                time = 0
                for i in range(int(op2)):
                    ingredientes = input(Fore.GREEN+'-Ingrese ingrediente '+str(i+1)+': '+Fore.LIGHTWHITE_EX)
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
                    else:
                        print(Fore.LIGHTRED_EX+Style.BRIGHT+'Ingrese un comando valido')

                Menu2()
                op = input(Fore.GREEN+'Eliga una opcion: '+Fore.LIGHTWHITE_EX)
            elif op == '3':
                cant = input(Fore.GREEN+'-Ingrese cantidad de pizzas: '+Fore.LIGHTWHITE_EX)
                time = time * int(cant) 
                Menu2()
                op = input(Fore.LIGHTCYAN_EX+'Eliga una opcion: '+Fore.LIGHTWHITE_EX)
            else:
                print(Fore.LIGHTRED_EX+Style.BRIGHT+'Ingrese un comando valido')
                Menu2()
                op = input(Fore.LIGHTCYAN_EX+'Eliga una opcion: '+Fore.LIGHTWHITE_EX)
        Menu()
        aux=input(Fore.GREEN+'Ingrese una opcion: '+Fore.LIGHTWHITE_EX)
    elif aux == '2':
        queue.Enqueue(name,cant,time)
        Menu()
        aux=input(Fore.GREEN+'Ingrese una opcion: ') 
    elif aux == '3':
        queue.Report()
        queue.crearReporte()
        Menu()
        aux=input(Fore.GREEN+'Ingrese una opcion: ') 
    elif aux == '4':
        queue.Dequeue()
        Menu()
        aux=input(Fore.GREEN+'Ingrese una opcion: ') 
    elif aux =='5':
        Datos()
        Menu()
        aux=input(Fore.GREEN+'Ingrese una opcion: ') 
    else:
        print(Fore.GREEN,'')
        aux=input('Ingrese una opcion: ')
exit



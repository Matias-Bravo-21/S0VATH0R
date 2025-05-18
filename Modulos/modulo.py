import os
import time
import subprocess
def menu():
    menu_animation()
    #listamos las opciones
    print("1. Herramientas OSINT") 
    print("2. Herramientas para escanear puertos")
    print("3. Herramientas para buscar exploit")
    print("4. Herramientas de sniffing de resdes(MITM)")
    print("5. ataque wireless")
    print("6. camaras Publicas")
    print("7. Phishing")
    print("8. hacking android")
    print("9. salir")
    
    if(os.name == 'posix'):
        print("sistema operativo linux")
    elif(os.name == 'nt'):
        print('Windows system')
        
def menu_animation():
    #limpiamos la terminal 
    os.system('clear')
    frames = [
    """╔╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╗""",
    """╟┼┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┼╢""",
    """╟┤███████╗ ██████╗ ██╗   ██╗ █████╗ ████████╗██╗  ██╗ ██████╗ ██████╗ ├╢""",
    """╟┤██╔════╝██╔═══██╗██║   ██║██╔══██╗╚══██╔══╝██║  ██║██╔═══██╗██╔══██╗├╢""",
    """╟┤███████╗██║   ██║██║   ██║███████║   ██║   ███████║██║   ██║██████╔╝├╢""",
    """╟┤╚════██║██║   ██║╚██╗ ██╔╝██╔══██║   ██║   ██╔══██║██║   ██║██╔══██╗├╢""",
    """╟┤███████║╚██████╔╝ ╚████╔╝ ██║  ██║   ██║   ██║  ██║╚██████╔╝██║  ██║├╢""",
    """╟┤╚══════╝ ╚═════╝   ╚═══╝  ╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝├╢""",
    """╟┤                       Autores: Matias Bravo                        ├╢""",
    """╟┼┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┼╢""",
    """╚╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╝"""
    ]
    #"animacion de cascada"
    for i in frames:
        time.sleep(0.2)
        print(i)

def osint_menu():
    opciones = ["seleccione una opcion (en int):\n","1. osint\n","2.osint telefonico\n"]
    
    for i in opciones:
        time.sleep(0.4)
        print(i)
        #listamos las herramientas de osint 
    
    opcion_tipo = int(input("escriba el numero de la opcion: ")) #debe validar solo entero
    
    if(opcion_tipo == 1):
        os.chdir('herramientas/osint')
        print("--------------->"+ os.getcwd())
        print(os.listdir("."))
        
        tool_option = input("seleccione una herramienta: ")
        
        if(tool_option.lower() == 'argus'):
            #nos movemos a la carpeta argus y lo iniciamos con python3
            os.chdir('argus')
            os.system('python3 argus.py')
        elif(tool_option.lower() == 'holehe'):
            #solicitamos el email y lo pasamos al programa
            email_objetivo = input("escriba un email: ")
            os.system('holehe '+ email_objetivo)
            input("presione cualquier tecla para volver al menu ...")
        elif(tool_option == 'osintgram'):
            #nos cambiamos a la carpeta osintgram t llamamos a la aplicacion
            os.chdir("Osintgram")
            os.system("python3 main.py")
            input("presione cualquier tecla para volver al menu ...")
    if(opcion_tipo == 2):
        osint_Phone_menu()

def osint_Phone_menu():
    #listamos las herramientas de osint 
    os.chdir('herramientas/OsintPhone')
    print("--------------->"+ os.getcwd())
    print(os.listdir("."))#listamos todo en el directorio
    
    #solicitamos el numeorque ingresaremos como parametro en los diferentes apps
    while True:
        scan_Phone = input("coloque el numero a escanear: ")
        if(len(scan_Phone) == 12):
            break
        else:
            print("valida las aplicaciones con el periferico estandar ejemplo +111 1111 1111\n vuelva a intentarlo...")
    
    opcion = input("seleccione una herramienta: ")
    
    if(opcion.lower() == 'inspector'):
        #nos movemos a la carpeta Inspector y le pasamos el parametro
        os.chdir('Inspector/core')
        os.system('clear')
        os.system('python3 inspector.py '+ scan_Phone)
        input("presione cualquier tecla para volver al menu ...")
        
    elif(opcion.lower() == 'phoneinfoga'):
        #lo pasamos a la app infoga
        os.system('phoneinfoga scan -n '+ scan_Phone)
        input("presione cualquier tecla para volver al menu ...")
    elif(opcion.lower() == 'storm'):
        #nos movemos a la carpeta storm 
        os.chdir('Storm-Breaker')
        os.system('python3 st.py')
        time.sleep(2)
        #solucion a STORM BREAKER

def ports_scan():
    def listar_puertos(lista):
        contador = 1
        for i in lista:
            time.sleep(0.1)
            print(str(contador) + " : " + str(i))
            contador += 1
        input("ingrese un valor para terminar...")
    #mostramos el directorio
    tools =["nmap"]
    print("herramientas de scaneo de puertos: \n")
    #imprimira las herramientas
    for i in tools:
        print(i)
    time.sleep(0.2)
    #selecciona la herramienta
    tool_select=input("seleccione una opcion: ")
    
    if(tool_select.lower() == "nmap" or tool_select == "1"):
        #logica de scaneo en nmap 
        puerto_scan = str(input("desea puertos personalisados Y o N?:  ")).upper()
        if(puerto_scan == "Y" or puerto_scan == "S"):
            puerto_escogido=int(input("indique el puerto a agregar: "))
            limite = puerto_escogido
            puertos = []
            while limite != 0 :
                #agregamos a la lista el puerto
                puertos.add(puerto_escogido)
                print(f"la cantidad de puertos escogidos son: {len(puertos + 1)}\n listando ...\n (si desea salir coloque 0)")
                #listamos los puertos
                print(listar_puertos(puertos))
                break
        elif(puerto_scan == "N"):
            ip=input("inserte una direccion ip: ")    
            if (tool_select == 1):
                os.system(f"nmap -sC -sV -O {ip} -p {puertos}")
            else:
                os.system(f"nmap -sC -sV -O {ip}")
            time.sleep(5)
            input("desea salir?...")

def buscar_exploits():
    tools = ['searchsploit']

    #listamos las herramientas
    for i in tools:
        print(i)
    op = input("seleccione una herramienta: ")
    if(op == "searchsploit" or op == "1"):
        name_exploit = input("ingrese nombre del exploit: ")
        os.system("searchsploit " + name_exploit)
        time.sleep(3)
        input("presione algo xd")

def Wireshark():
    os.system("wireshark")

def CamPublicas():
    os.chdir('herramientas/Cam/cam-hackers')
    os.system("python3 cam-hackers.py")

def Phishing():
    os.chdir('herramientas/Phishing/B-Phish')
    os.system('python3 bphish.py')

def instalador():
    pass


def actualizador():
    pass


#esta era la solucion
def pruebas():
    """
    print(os.getcwd())
    os.chdir('../../../Terminales')
    print(os.getcwd())
    print(os.listdir("."))
    time.sleep(2)
    os.system("./ngrok.sh")"""
def Pruebas2():
    print(os.getcwd())
    os.chdir('herramientas/osint')
    diccionario = {
        "1,-OSINT":list(os.listdir(".")),
        "2.-OsintPhone":list(os.listdir("."))
    }
    for key in diccionario:
        print(key)
        for value in diccionario[key]:
            print(value)


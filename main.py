from Modulos import modulo

while True:
    modulo.menu()
    
    opcion = int(input("Por favor, elige una opción: "))
    
    if(opcion == 1):
        modulo.osint_menu()  
    elif (opcion == 2):
        #aca llamaremos a la herramienta nmap principalmente y hara tanto escaneo personalizado como por defecto
        modulo.ports_scan()
    elif(opcion == 3):
        #aca por defecto llamaremos a searchsploit
        modulo.buscar_exploits()
    elif(opcion==4):
        #aca llamaremos a wireshark
        modulo.Wireshark()
    elif(opcion ==5):
        #aca llamaremos a fluxion o ofrecemos el personalizable para lohrar un mejor ataque, luego llamar la herrameinta jhon para romper hacshes automaticamente
        print()
    elif(opcion == 6):
        #llamamos a la herramienta cam y la usamos
        modulo.CamPublicas()
    elif(opcion == 7):
        #llamaremos a herramientas como B-pish 
        modulo.Phishing()
        print()
    elif(opcion == 8):
        #aca llamaremos al instador llamamaos al instalador de todos los modulos
        print("instalando....") 
    elif(opcion == 9):
        #limpiaremos la pantalla y imprimermos el nombre de la app
        modulo.menu_animation()
        break
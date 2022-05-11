#=================================================
#SCRIPT PARA ESCANEAR DIRECCIONES IPs ACTIVAS
#EN UNA MISMA RED O EN UN FUTURO VARIAS SUBREDES
#=================================================

#ESQUEMATIZACION DE EJECUCION DEL SCRIPT

#=================================================

#PEDIR RANGO DE IPs PARA RESTREAR
#                |
#                |
#                |
#       SEPARAMOS EL RANGO   Check
#       PARA HACER EL BUCLE
#                |
#                |
#                |
#       HACEMOS PING A CADA IP (USAMOS LAS PROPIEDADES DE FILE Y READLINE PARA ENCONTRAR EL TEXTO QUE NECESITAMOS) Check
#                |
#                |
#                | 
#       FILTRAMOS EL RESULTADO Check
#       PARA ENCONTRAR LA RESPUESTA
#                |
#                |
#                |
#       ALMACENAMOS LA IP CONECTADA
#       PARA MANEJARLA MAS TARDE
#


import os

def titulo():


    print("                ___  ")
    print("              /'___\ ")
    print(" __  _   ____/\ \__/ ")
    print("/\ \/'\ /',__\ \ ,__\\")
    print(" />  <//\__, `\ \ \_/")
    print(" /\_/\_\/\____/\ \_\ ")
    print(" \//\/_/\/___/  \/_/ ")

def menuPrincipal():
    rango=input("[*] Introduce el rango de Ips a escanear (xxx.xxx.xxx.xxx-xxx): ")
    return rango

def conseguirRango(rangoDeIps):
    #192.168.0.1-255
    
    #['192.168.0.1','255']
    #255 -> fin de escaneo
    #192.168.0.1 -> ip inicial
    
    #['192.168.0','1']
    #192.168.0 -> direccion de red
    #1 -> inicio de rango
    #192.168.0.x -> formato de ips

    arrayInicioYFinDeRango = rangoDeIps.split("-") #Separo la cadena en dos partes ['192.168.0.1','255']
    finDeRango = arrayInicioYFinDeRango[1] #Consigo la ultima parte '255'
    cadenaInicioRango = arrayInicioYFinDeRango[0] #Consigo la primera cadena '192.168.0.1'
    arrayInicioRango = cadenaInicioRango.split(".") #Separo la cadena en cuatro partes ['192','168','0','1']
    inicioDeRango = arrayInicioRango[-1] #Consigo la ultima parte '1'
    direccionDeRed = arrayInicioRango[0]+"."+arrayInicioRango[1]+"."+arrayInicioRango[2]+"." #Consigo la direccion de red

    return inicioDeRango,finDeRango,direccionDeRed

def escaneo(inicioDeRango,finDeRango,direccionDeRed):

    print("\tEscaneando Ips...")
    for byte in range(int(inicioDeRango),int(finDeRango)+1):
        ipParaPingear = str(direccionDeRed) + str(byte)
        #Hariamos ping a cada ip
        resultadoPing = os.popen("ping -n 1 " + ipParaPingear) #Esta funcion te ejecuta un comando com si fuese os.system() pero te devuelve el resultado de la ejecucion de comandos
        for linea in resultadoPing.readlines(): #Leemos un array de lineas con cada linea del resultado
            if("TTL" in linea): #Si se encuentra la cadena "TTL" en cualquier linea entonces sera porque ha habido respuerta de la ip
                print("\t\t[+] {} Its Up".format(ipParaPingear))

                
titulo()
rango=menuPrincipal()
i,f,d=conseguirRango(rango)
escaneo(i,f,d)

    
    


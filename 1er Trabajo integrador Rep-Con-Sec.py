#Trabajo integrador Repetitivas-Condicionales-Secuenciales

#Ejercicio 1 “Caja del Kiosco”
nombre_cliente = input("Escribi el nombre del cliente: ")  
while not nombre_cliente.isalpha():    # Pido nombre del cliente y valido de que sean letras dentro del ciclo while
    print("Incorrecto, vuelve a ingresar el nombre") 
    nombre_cliente = input("Escribi su nombre: ")

productos =(input("Cuantos productos va a comprar: ")) #Pedi el numero de productos que iba a comprar
while not productos.isdigit() or int(productos) <= 0: #valide el numero de que sea siempre numeros y ademas numeros positivos
    print("Tiene que ser un numero entero")
    productos = input("Ingrese nuevamente: ")

productos = int(productos)
precio_sin_descuento = 0    #Inicie los contadores en 0
precio_con_descuento = 0
precio_final = 0

for i in range(int(productos)):            #hice bucle for para pasar por cada producto comprado
    precio = (input("Que precio tiene: "))
    while not precio.isdigit() or int(precio) <= 0:   #en el bucle while valido los datos ingresados
        print("Vuelve a ingresar el precio, tiene que ser un numero entero")
        precio = input("Vuelve a ingresar el precio: ")
        
    descuento = input("Tiene descuento? escriba s/n: ")
    while descuento.lower() != "s" and descuento.lower() != "n": #valido que solo se pueda ingresar s y n en minusculas o mayusculas
        print("Descuento invalido")
        descuento = input("Ingrese nuevamente s o n: ")
    precio = int(precio)  
    precio_sin_descuento += precio  
    if descuento.lower() == "s":         #Un if para aplicar o no el descuento segun lo ingresado anteriormente
            precio_final = precio  * 0.9
            print("Se aplicara el descuento del 10%")
            print(f"Producto {i+1} - Precio: {precio} Descuento (S/N): {descuento}")
    else:
            print("No tiene descuento")
            precio_final = precio
            print(f"Producto {i+1} - Precio: {precio} Descuento (S/N): {descuento}")
    precio_con_descuento += precio_final

ahorro = precio_sin_descuento - precio_con_descuento
promedio = precio_con_descuento / productos

print(f"cliente: {nombre_cliente}")
print(f"Total sin decsuentos: {precio_sin_descuento:.2f}" )
print(f"Total con descuentos: {precio_con_descuento:.2f}")
print(f"Ahorro total: {ahorro:.2f}")
print(f"Promedio por producto: {promedio:.2f}")
print(f"{precio:.2f}")


#ejercicio 2 “Acceso al Campus y Menú Seguro
usuario_correcto = "alumno"
clave_correcta = "python123"
contador = 0

while contador < 3:  #se repite el bucle hasta que el contador llegue a 3 y corte
    usuario = input("Ingrese su usuario: ")
    clave= input("ingrese clave: ") 
    if usuario == usuario_correcto and clave == clave_correcta: #valido si el usuario y la contraseña son correctas
        print("Usuario y contraseña correctas")
        break
    else:
        print("Vuelve a ingresar su usuario y contraseña") #se vuelve a repetir el bucle porque no fue correcto el ingreso
        contador += 1

if contador == 3:       #cuando el contador llega a 3 se bloque los intentos 
    print("Cuenta bloqueada")
confirmacion = ""
nueva_clave = ""

if contador < 3:             #Mientras la clave se cumpla dentro de los primeros tres intentos se ejecutara el sigiente bucle
    while True:
        print("opcion 1: Inscripcion, Opcion 2: Cambiar clave, Opcion 3: Frase motivacional, opcion 4: Salir")
        opcion = input("Opcion: ")    
        if not opcion.isdigit():   #Muestro el menu con las cuatro opciones y aclaro que tiene que ser numeros y dentro del rango ya aclarado
            print("Ingrese un numero valido del 1 al 4: ")
        elif int(opcion) < 1 or int(opcion) > 4 :
            print("Ingrese nuevamente una opcion dentro del rango")
        else:
            print("Opcion valida")#Procedo a explicar que pasa en cada una de las opciones

            if opcion == "1":
                print("su estado de insripcion es: Inscripto")
            elif opcion == "2":
                print("Cambio de clave")
                while True:         #Hago un bucle while para el cambio de contraseña y pido la confimacion de la misma
                    nueva_clave = input("Ingresa su nueva clave: ")
                    if len(nueva_clave) < 6: 
                        print ("La clave debe tener menos de 6 digitos")
                    else:
                        confirmacion = input("Confirma la clave: ")
                    if nueva_clave != confirmacion:
                        print("las claves no coinciden")
                    else:
                        print("Las claves coinciden")
                        break
            elif opcion == "3":           
                print("No bajes los brazos, vos podes")
            elif opcion == "4":
                print("salir")      #Doy cierre cuando se elige la opcion 4
                break

#Ejercicio 3 (Alta) — “Agenda de Turnos con Nombres (sin listas)”
operador = input("Esribi el nombre del operador: ")
while not operador.isalpha():   # Pido nombre del operador y valido de que sean letras dentro del ciclo while
    print("No se pueden ingresar numeros")
    operador = input("Escribi nuevamente su nombre solamente con letras: ")

lunes1 =" "
lunes2 = " "
lunes3 = " "
lunes4 = " "
martes1 = " "
martes2 = " "
martes3 = " "

while True:
    print("Menu: 1)reservar turno, 2)Cancelar turno, 3)Ver agenda del dia, 4)Ver resumen general, 5)cerrar session")
    menu = input("Eligue una opcion del menu: ") 
    if not menu.isdigit():
        print("Solo numeros")
    elif int(menu) < 1 or int(menu) > 5:  #Valido de que el numero sea dentro de lo solicitado
        print("Eligue dentro del rango numerico")
    else:
        print("Opcion valida")  

    if menu == "1":   
            print("Reservar Turno")
            dia = input("Elegir dia(indicar numero): 1)Lunes o 2)Marte: ")
            while not dia.isdigit() or (dia != "1" and (dia != "2")):  #Valido que solo se ingrese 1 o 2
                print("Solo puede elejir 1 como lunes o 2 como martes")
                dia = input("Elegir dia(indicar numero): 1)Lunes o 2)Marte: ")
                print("Opcion valida")
            nombre = input("Ingrese su nombre para agendar el turno: ")
            while not nombre.isalpha():
                print("El nombre solo tiene que contener letras")
                nombre = input("Ingrese su nombre para agendar el turno: ")

            if dia == "1":
                print("Quiere reservar dia lunes")
                if not (nombre == lunes1 or nombre == lunes2 or nombre == lunes3 or nombre == lunes4): #Compra para ver si el nombre ya esta agendado en algun dia
                    print("No esta repetido el nombre")
                    if lunes1 == " ":       
                        lunes1 = nombre
                        print("Primer turno ocupado del dia lunes")
                    elif lunes2 == " ":
                        lunes2 = nombre
                        print("Segundo turno ocupado del dia lunes")
                    elif lunes3 == " ":
                        lunes3 = nombre
                        print("Tercero turno ocupado del dia lunes")
                    elif lunes4 == " ":
                        lunes4 = nombre
                        print("Cuarto turno ocupado del dia lunes")
                    else:
                        print("Ya no hay turnos libres para el dia lunes")
                else:
                    print("Su nombre esta repetido en los turnos del lunes, pida para otro dia")   
            else:
                        print("Reservar Martes")

            if dia == "2":
                print("Quiere reservar martes")
                if not (nombre == martes1 or nombre == martes2 or nombre == martes3): #Se vuelve a comparar solo que ahora con los dias martes
                    print("El nombre no esta repetido el dia martes")
                    if martes1 == " ":
                        martes1 = nombre
                        print("Primer turno ocupado del dia martes")
                    elif martes2 == " ":
                        martes2 = nombre
                        print("Segundo turno ocupado del dia martes")
                    elif martes3 == " ":
                        martes3 = nombre
                        print("Tercer turno ocupado del dia martes")
                    else:
                        print("Ya no hay turnos libres para el dia martes")
                else:
                    print("El nombre si esta repetido para el dia martes")

    elif menu == "2":    
        print("Cancelar turno")
        dia = input("Elegir dia: ")
        while not dia.isdigit() or (dia != "1" and dia != "2"): #Se verifica que solo se ingrese numeros del 1 al 2
            print("Error")
            dia = input("Elegir dia: ")
        nombre = input("Ingrese su nombre para cancelar el turno: ")
        while not nombre.isalpha():
            print("El nombre solo tiene que contener letras")
            nombre = input("Ingrese su nombre: ")

        if dia == "1":  #Se vuelve a comparar a ver si algun nombre ya esta guardado en aluna variable
            if lunes1 == nombre:       
                lunes1 = " "
                print("Turno cancelado")  #Si esta guardado entonces se cancela el turno
            elif lunes2 == nombre:
                lunes2 = " "
                print("Turno cancelado")
            elif lunes3 == nombre:
                lunes3 = " "
                print("Turno cancelado")
            elif lunes4 == nombre:
                lunes4 = " "
                print("Turno cancelado ")
            else:
                print("No hay ningun turno con ese nombre")

        elif dia == "2":
            if martes1 == nombre:
                martes1 = " "
                print("Turno cancelado ")
            elif martes2 == nombre:
                martes2 = " "
                print("Turno cancelado ")
            elif martes3 == nombre:
                martes3 = " "
                print("Turno cancelado ")
            else:
                print("No hay ningun turno con ese nombre")

    elif menu == "3":
            print("Ver agenda del dia")  #Se muestra los resultados de lo que se guardo en cada variable 
            dia = input("Elegir dia: ")
            while not dia.isdigit() or (dia != "1" and dia != "2"):
                print("Error")
                dia = input("Elegir dia: ")
            if dia == "1":
                if lunes1 == " ":
                    print("Turno lunes 1: Libre ")
                else:
                    print("Turno lunes 1: ", lunes1)
                if lunes2 == " ":
                    print("Turno lunes 2: Libre")
                else:
                    print("Turno lunes 2: ", lunes2)
                if lunes3 == " ":
                    print("Turno lunes 3: Libre ")
                else:
                    print("Turno lunes 3: ", lunes3)
                if lunes4 == " ":
                    print("Turno lunes 4: Libre")
                else:
                    print("Turno lunes 4: ", lunes4)

            elif dia == "2":
                if  martes1== " ":
                    print("Turno martes 1: Libre ")
                else:
                    print("Turno martes 1: ", martes1)
                if martes2 == " ":
                    print("Turno martes 2: Libre")
                else:
                    print("Turno martes 2: ", martes2)
                if martes3 == " ":
                    print("Turno martes 3: Libre ")
                else:
                    print("Turno martes 3: ", martes3)

    elif menu == "4":  
            print ("Ver resumen general") 
            print("Turnos del dia lunes: ")
            if lunes1 == " ":
                    print("Turno lunes 1: Libre ")
            else:
                    print("Turno lunes 1: ", lunes1)
            if lunes2 == " ":
                    print("Turno lunes 2: Libre")
            else:
                    print("Turno lunes 2: ", lunes2)
            if lunes3 == " ":
                    print("Turno lunes 3: Libre ")
            else:
                    print("Turno lunes 3: ", lunes3)
            if lunes4 == " ":
                    print("Turno lunes4: Libre")
            else:
                    print("Turno lunes 4: ", lunes4)
                    
                    print("Turnos del dia martes: ")
            if  martes1== " ":
                    print("Turno martes 1: Libre ")
            else:
                    print("Turno martes 1: ", martes1)
            if martes2 == " ":
                    print("Turno martes 2: Libre")
            else:
                    print("Turno martes 2: ", martes2)
            if martes3 == " ":
                    print("Turno martes 3: Libre ")
            else:
                    print("Turno martes 3: ", martes3)
    elif menu == "5":
            print("Cerrar session")
            break

#Ejercicio 4 — “Escape Room: La Bóveda”
energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""
contador = 0

nombre_agente= input("Escribi el nombre del agente: ")  #Valido que solo se ingresen letras
while not nombre_agente.isalpha():
    print("Solo usar letras")
    nombre_agente = input("Escribir nombre nuevamente: ")

while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3 and not alarma:  #Se contienua mientras esto se cumpla 
    print("Energia: ",energia)
    print("Tiempo: ",tiempo)
    print("Cerraduras abiertas: ",cerraduras_abiertas)
    print("Alarma: ",alarma)
    opcion = input("Elegir la opcion, puede ser 1, 2 o 3: ")   #Validar que solo se ingresen numeros y dentro del rango pedidio
    while not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 3:
            print("Solamente numero del 1 al 3")
            opcion = input("Elegi nuevamente la opcion: ")

    if opcion == "1":  #En el caso que se elija la opcion 1 se descuenta algunos valores y se suma el contador 
        print("Forzar cerradura")
        contador += 1
        energia -= 20
        tiempo -= 2 

        if energia < 40:        
            print("Riesgo de alarma")
            numero = input("Elegir un numero 1, 2 o 3: ")
            while not numero.isdigit() or int(numero) < 1 or int(numero) > 3:
                print("Solamente numero del 1 al 3")
                numero = input("Elegi nuevamente la opcion: ")
            if numero == "3":
                alarma = True 
            else:
                print("Se abre una cerradura")
                cerraduras_abiertas += 1 
        if contador == 3:  # si se elige tres veces seguidas la primera opcion, gracias al contador suena la alarma
            alarma = True

    if opcion == "2":
        contador = 0   #El contador se reinicia en cada nueva opcion 
        print("Hackear panel")
        energia -= 10
        tiempo -= 3
        for i in range (1, 5):     #Se hace un bucle para agragar las letras para el codigo parcial
            codigo_parcial += input ("Agregar una letra: ")
            if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:
                print("Se abre una cerradura")
                cerraduras_abiertas += 1

    if opcion == "3":
        contador = 0  #De nuevo se reinicia el contador para una nueva opcion 
        print("Descansar")
        energia += 15
        tiempo -= 1
        if energia > 100:   #Se aclaran los valores maximos que se pueden alcanzar 
            energia = 100
            print("El maximo es 100")
        if alarma:
            energia -= 10

if alarma == True and tiempo <= 3 and cerraduras_abiertas < 3: #Las reglas del bloqueo 
    print("El sistema se bloqueo, perdiste")

if cerraduras_abiertas == 3: # Motivos de victorias o derrotas
    print("Victoria")
elif energia <= 0 or tiempo <= 0:
    print("Derrota")
else:
    print("Se bloqueo por alarma: Derrota")

#Ejercicio 5 — “Escape Room:"La Arena del Gladiador"
vida_del_Gladiador = 100 
vida_del_Enemigo = 100 
pociones_de_Vida = 3 
daño_base_Ataque_Pesado = 15 
daño_base_del_enemigo = 12 
turno_Gladiador = True  
daño = 0

gladiador = input("Esribi el nombre del gladiador: ")  #Validar el nombre del gladiador 
while not gladiador.isalpha():   
    print("No se pueden ingresar numeros")
    gladiador = input("Error: Solo se permiten letras")

while vida_del_Gladiador > 0 and vida_del_Enemigo > 0: #Se juega mientras sus vidas sean mayor a 0 
    print(f"La vida del gladiador: {vida_del_Gladiador}, La vida del enemigo: {vida_del_Enemigo}, Pocionones: {pociones_de_Vida}")

    menu = input("Menu: 1)Ataque pesado, 2)Rafaga veloz, 3)Curar: ")
    while not menu.isdigit() or (int(menu) < 1 or int(menu) > 3):  #Se valida que se ingresen numeros en el rango solicitado
        print("Error, Solo numeros del 1 al 3")
        menu = input("Ingrese nuevamente: ")
    daño = daño_base_Ataque_Pesado
    if menu == "1":  # OPCION 1 
            if vida_del_Enemigo < 20:
                daño = daño * 1.5
                print("Golpe critico")
            vida_del_Enemigo -= daño
            print(f"Atacaste al enemigo por {daño} puntos")
            
    elif menu == "2": #OPCION 2
            for i in range(3):
                vida_del_Enemigo -= 5 
                print("Golpe conectado por 5 de daño")

    elif menu == "3":     #OPCION 3
                if pociones_de_Vida > 0:
                    vida_del_Gladiador += 30
                    pociones_de_Vida -= 1
                    print("Te curaste 30 puntos")
                else:
                    print("¡No quedan pociones!")
#Turno enemigo
if vida_del_Gladiador > 0:
    vida_del_Gladiador -= daño_base_del_enemigo
    print("El enemigo te ataco por 12 puntos de daño")
        
#Final
    if vida_del_Gladiador > 0:
        print(f"Victoria {gladiador} ha ganado la batalla")
    else:    
        print("Derrota. Has caido en combate")

print("Vida del gladiador: ",vida_del_Gladiador)
print("vida del enemigo: ",vida_del_Enemigo)
print("Pociciones de vida: ",pociones_de_Vida)

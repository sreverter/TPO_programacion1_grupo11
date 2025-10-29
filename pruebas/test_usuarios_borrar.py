from iniciacion_listas import datos_globales_usuarios, dni_en_uso, datos_globales_reserva,id_usuarios,datos_de_ingreso_dni
from entidades.usuarios import ver_m3,id_usuarios,ver_busqueda_usuarios
from funciones.funciones_reservas import obt_id_Actual
from funciones.funciones_globales import mostrar_tabla
import re
import json

def borrado_usuarios():
        while True:
            try:
                id_eliminar = int(input("Seleccione id a eliminar: "))
                if id_eliminar not in id_usuarios:
                    print("ID no encontrado")
                    continue
                else:
                    break
            except(ValueError,KeyboardInterrupt):
                print("porfavor ponga caracteres valido")
                continue
            
        print("\033[1;91m Recuerde que esta acción es irrevertible \033[0m")
        print()
        print("\033[1;91m Por favor vuelva a dar confirmación \033[0m")
        
        while True:
            try:
                opcion = int(input(
                    "\033[35m  → [1] Eliminar cuenta\033[0m\n"
                    "\033[35m  → [2] Volver al menú\033[0m\n"
                ))
                if opcion in (1,2):
                    break
                else:
                    print("solo 1 y 2 son numeros validos")
            except(KeyboardInterrupt,ValueError):
                print("porfavor ponga caracteres valido")
                continue

        usuarios_eliminar=[]
        if opcion == 1:
            """
                        with open("datos_usuarios.json","r", encoding="utf-8") as archivo:
                            usuarios = json.load(archivo)
                            for user in usuarios:
                                if user["id"]==id_eliminar:
                                    user["estado"]=False
                            usuarios_eliminar.append(user)
                        with open("datos/datos_usuarios.json", "w", encoding="utf-8") as archivo:
                            json.dump(usuarios_eliminar, archivo, indent=4, ensure_ascii=False)
                        
                        
            
                        with open("datos/datos_reserva.txt","r", encoding="utf-8") as archivo:
                            usuarios = json.load(archivo)
                            for user in usuarios:
                                if user["id"]==id_eliminar:
                                    
                            usuarios_eliminar.append(user)
                        with open("datos/datos_reservas.txt", "w", encoding="utf-8") as archivo:
                            json.dump(usuarios_eliminar, archivo, indent=4, ensure_ascii=False)
            """
#tecnicamente no es un json o un txt depende de lo que usemos esta 
# funcion va a variar sobre todo en la lectura por ahora lo deje como para un json aunque 
# seguramente sea un txt
            for i in datos_globales_usuarios:
                if i[0] == id_eliminar:
                    i[5] = False   
            for i in datos_globales_reserva[:]:
                if i[1] == id_eliminar:
                    datos_globales_reserva.remove(i)
            print(f"Usuario con ID {id_eliminar} y las reservas que tiene asociadas fueron eliminados correctamente.")
        elif opcion == 2:
                print("volviendo al menu")
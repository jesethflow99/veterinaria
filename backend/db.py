import pymysql
import pymysql.cursors
import config
from colorama import Fore,init
init(autoreset=True)

try:
    conn = pymysql.connect(**config.DB_CONFIG, cursorclass=pymysql.cursors.DictCursor)
    cursor = conn.cursor()
except:
    pass

def conectar():
    try:
        if conn:
            print(Fore.GREEN + "✅ Conexion Exitosa")
            print(Fore.WHITE +"")
            return conn
    except Exception as e:
        print(Fore.RED + f"❌ Error de conexion: {e}")
        print(Fore.WHITE +"")
        return None

def ver(nombre):
    try:
        cursor.execute(f"SELECT * FROM {nombre}")
        data = cursor.fetchall()
        print(f"Tipo de 'data': {type(data)}")
        print(f"Contenido de 'data': {data}")
        return data
    except Exception as e:
        print(Fore.RED + f"❌ Error al obtener datos: {e}")
        print(Fore.WHITE +"")
        return {"Error": str(e)}
    
def ver_1(id,nombre):
    try:
        cursor.execute(f"SELECT * FROM {nombre} WHERE id = %s",id)
        data=cursor.fetchall()
        return data
    except Exception as e:
        return {"Error":str(e)}
    
def eliminar(id,nombre):
    try:
        cursor.execute(f"DELETE FROM {nombre} WHERE id = %s",(id,))
        return {"message":f"{id} Eliminado"}
    except Exception as e:
        return {"message":f"{id} no se pudo eliminar: {str(e)}"}
    
    
def registrar_cliente(data):
    try:
            if not all(key in data for key in ("id","nombre","contacto","domicilio")):
                raise ValueError("Faltan campos obligatorios")

            if not isinstance(data["id"],int):
                raise ValueError("el campo id debe ser un numero entero")
            print(data)
            cursor.execute(
                "INSERT INTO CLIENTES(id, nombre, contacto, domicilio) values(%s, %s, %s, %s)", 
                (data['id'], data['nombre'], data['contacto'], data['domicilio'])
             )
            print(Fore.GREEN + "✅ Cliente agregado con éxito!!!")
            print(Fore.WHITE +"")
            conn.commit()
            return {"mensaje": "usuario agregado con éxito"}
    except pymysql.MySQLError as e:
        print(Fore.RED + f"❌ Error de base de datos: {str(e)}")
        print(Fore.WHITE +"")    
        return {"error": str(e)}
    except Exception as e:
        print(Fore.RED + f"❌ Error desconocido: {str(e)}")
        print(Fore.WHITE +"")
        return {"error": str(e)}
    

    

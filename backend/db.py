from flask import jsonify
import pymysql
import pymysql.cursors
import config
from colorama import Fore

conn = pymysql.connect(**config.DB_CONFIG, cursorclass=pymysql.cursors.DictCursor)
cursor = conn.cursor()

def conectar():
    try:
        print(Fore.GREEN + "✅ Conexion Exitosa")
        print(Fore.WHITE +"")
        return conn
    except Exception as e:
        print(Fore.RED + f"❌ Error de conexion: {e}")
        print(Fore.WHITE +"")
        return None

def ver_clientes():
    try:
        cursor.execute("SELECT * FROM CLIENTES")
        data = cursor.fetchall()
        print(f"Tipo de 'data': {type(data)}")
        print(f"Contenido de 'data': {data}")
        return data
    except Exception as e:
        print(Fore.RED + f"❌ Error al obtener clientes: {e}")
        print(Fore.WHITE +"")
        return jsonify({"Error": str(e)})

def registrar_cliente(data):
    try:
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
    

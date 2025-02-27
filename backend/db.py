import pymysql
import pymysql.cursors
import config
from colorama import Fore

def conectar():
    try:
        conexion=pymysql.connect(**config.DB_CONFIG,cursorclass=pymysql.cursors.DictCursor)
        print(Fore.GREEN +"✅ Conexion Exitosa")
        return conexion
    except Exception as e:
        print(Fore.RED + f"❌ Error de conexion: {e}")
        return None
        
    
conectar()
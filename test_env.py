from dotenv import load_dotenv
import os

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Imprimir las variables cargadas
print("DATABASE_URL:", os.getenv("DATABASE_URL"))
print("JWT_SECRET:", os.getenv("JWT_SECRET"))

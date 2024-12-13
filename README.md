# Copysistem-back

Este repositorio contiene el backend del proyecto Copysistem.

## Configuración inicial

Para que el proyecto funcione correctamente, es necesario configurar las variables de entorno. Sigue los pasos a continuación:

1. Crear el archivo `.env`

Crea un archivo llamado `.env` en la raíz del proyecto. Este archivo será utilizado para definir las variables de entorno necesarias para la ejecución del proyecto.

2. Copiar el contenido de `.env.example`
En el archivo recién creado (`.env`), copia el contenido del archivo `.env.example` que se encuentra en la raíz del repositorio.

3. Configurar las variables de entorno

Edita el archivo `.env` y asegúrate de proporcionar los valores adecuados para las siguientes variables:

 ```shell
DATABASE_URL=
JWT_SECRET=
```
DATABASE_URL: URL de conexión a la base de datos.

JWT_SECRET: Clave secreta utilizada para generar y validar JSON Web Tokens (JWT).
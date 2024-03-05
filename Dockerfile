# Usar una imagen base de Python
FROM python:3.12.2

# Establecer el directorio de trabajo
WORKDIR /usr/src/app

# Copiar los archivos del proyecto al contenedor
COPY . .

# Instalar las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Exponer el puerto en el que se ejecutará la aplicación
EXPOSE 8000

# Comando para ejecutar la aplicación
CMD ["python", "web2py.py", "-a", "8000"]

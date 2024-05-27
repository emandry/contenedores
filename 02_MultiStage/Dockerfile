# Etapa 1: Construcción
FROM node:19-alpine AS build

# Establecer el directorio de trabajo en la imagen intermedia
WORKDIR /app

# Copiar los archivos de dependencias
COPY package*.json ./

# Instalar las dependencias
RUN npm install

# Copiar el código de la aplicación
COPY . .

# Etapa 2: Imagen final
FROM node:19-alpine

# Establecer el directorio de trabajo en la imagen final
WORKDIR /app

# Copiar los archivos necesarios desde la imagen de construcción
COPY --from=build /app .

# Exponer el puerto en el que la aplicación correrá
EXPOSE 3000

# Comando para ejecutar la aplicación
CMD ["npm", "start"]

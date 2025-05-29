# GodsPlan WebApp
Elaborado por : Romel Gualoto, Daniel Cornejo , Jose Perez 
Aplicación web construida con Flask y SQL Server para la gestión de estudiantes en el contexto de una catequesis. Permite registrar, editar, listar y eliminar estudiantes utilizando procedimientos almacenados  en la base de datos.

Hemos utilizado las siguientes herramientas en base a los requerimientos de la asignacion   :
-Python 3.10+
-Flask
-SQL Server
-HTML 
-Git

# Requisitos previos para ejecutar la aplicación
- Python 3.10 o superior
- Git
- SQL Server (con la base de datos `GodsPlan` creada) , 
Importante: La base de datos esta adjuntada en el envio de la asignacion , enviada por el estudiante Romel Gualoto , (solo lo envia un estudiante debido al espacio de buzon de envio)
- Tener configurado el esquema `persona` con los procedimientos almacenados requeridos:
  - `sp_ListEstudiantes`
  - `sp_CreateEstudiante`
  - `sp_GetEstudianteById`
  - `sp_UpdateEstudiante`
  - `sp_DeleteEstudiante`
Dichos procedimientos ya se encuentran dentro de la base de datos 

# Instrucciones para ejecutar el proyecto
- Clonar el repositorio
- Crear el entorno virtual: python -m venv env
- Activar el entorno virtual:  .\env\Scripts\activate
- Instalar dependendencias: pip install -r requirements.txt
NOTA: Instalar adicionalmente flask con el siguiente comando : pip install flask pyodbc 

*IMPORTANTE*

- Configurar el archivo config.json
Dentro del archivo config.json cambiar la linea "name_server": "ROMELLAPTOP\\SQLEXPRESS" por el nombre de servidor propio para que se conecte a sql sin problemas 

- Ejecutamos la aplicacion con: python app.py
- Verificamos dirigiendonos a http://127.0.0.1:5000/ en cualquier navegador 
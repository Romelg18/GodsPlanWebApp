from flask import Flask, render_template, request, redirect
import pyodbc
import json
from datetime import datetime

app = Flask(__name__)

# Cargar configuración desde config.json
with open('config.json') as f:
    config = json.load(f)
    print("Conectado a la base de datos:", config['database'])

# Conexión a SQL Server usando autenticación de Windows
conn_str = (
    f"DRIVER={{{config['controlador_odbc']}}};"
    f"SERVER={config['name_server']};"
    f"DATABASE={config['database']};"
    f"Trusted_Connection=yes;"
)

conn = pyodbc.connect(conn_str)
cursor = conn.cursor()

# Página principal
@app.route('/')
def index():
    return render_template('index.html')

# Ver lista de estudiantes
@app.route('/ver')
def ver_estudiantes():
    cursor.execute("EXEC persona.sp_ListEstudiantes")
    estudiantes = cursor.fetchall()
    estudiantes_ordenados = sorted(estudiantes, key=lambda x: x.Id_Estudiante)
    return render_template('ver_estudiantes.html', estudiantes=estudiantes_ordenados)

# Agregar estudiante
@app.route('/agregar', methods=['GET', 'POST'])
def agregar_estudiante():
    if request.method == 'POST':
        nombre = request.form['Nombre']
        parroquia_id = request.form['Parroquia_Id_Parroquia']
        persona_id = request.form['Persona_Id_Persona']

        if not nombre or not parroquia_id or not persona_id:
            return "Error: Nombre, Parroquia ID y Persona ID son obligatorios", 400

        fecha_nac = request.form['FechaNacimiento'] or None
        direccion = request.form['Direccion'] or None
        telefono = request.form['Telefono'] or None

        cursor.execute("EXEC persona.sp_CreateEstudiante ?, ?, ?, ?, ?, ?",
                       nombre,
                       fecha_nac,
                       direccion,
                       telefono,
                       int(parroquia_id),
                       int(persona_id))
        conn.commit()
        return redirect('/ver')
    return render_template('agregar_estudiante.html')

# Editar estudiante
@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar_estudiante(id):
    if request.method == 'POST':
        nombre = request.form['Nombre']
        parroquia_id = request.form['Parroquia_Id_Parroquia']
        persona_id = request.form['Persona_Id_Persona']

        if not nombre or not parroquia_id or not persona_id:
            return "Error: Nombre, Parroquia ID y Persona ID son obligatorios", 400

        fecha_nac = request.form['FechaNacimiento'] or None
        direccion = request.form['Direccion'] or None
        telefono = request.form['Telefono'] or None

        cursor.execute("EXEC persona.sp_UpdateEstudiante ?, ?, ?, ?, ?, ?, ?",
                       id,
                       nombre,
                       fecha_nac,
                       direccion,
                       telefono,
                       int(parroquia_id),
                       int(persona_id))
        conn.commit()
        return redirect('/ver')
    else:
        cursor.execute("EXEC persona.sp_GetEstudianteById ?", id)
        estudiante = cursor.fetchone()

        # ✅ Preparar fecha para el input date
        fecha_str = ''
        if estudiante.FechaNacimiento:
            fecha_str = estudiante.FechaNacimiento.strftime('%Y-%m-%d')

        return render_template('editar_estudiante.html', estudiante=estudiante, fecha_nacimiento=fecha_str)

# Eliminar estudiante
@app.route('/eliminar/<int:id>')
def eliminar_estudiante(id):
    cursor.execute("EXEC persona.sp_DeleteEstudiante ?", id)
    conn.commit()
    return redirect('/ver')

if __name__ == '__main__':
    app.run(debug=True)

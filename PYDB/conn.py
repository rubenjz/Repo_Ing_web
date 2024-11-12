import pymysql  # type: ignore

# Conexión a la base de datos
conn = pymysql.connect(
    host='localhost',
    user='root',
    passwd='UTPL2023',
    database='universidad',
    port=3306
)

# Función para insertar una nueva carrera
def insertar_carrera(codigo, nombre, modalidad_id):
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO carrera (codigo, nombre, modalidad_id) VALUES (%s, %s, %s)", 
            (codigo, nombre, modalidad_id)
        )
        conn.commit()
        print("Carrera insertada correctamente.")
    except pymysql.Error as e:
        print(f"Error al insertar la carrera: {e}")

# Función para consultar todas las carreras
def consultar_carreras():
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM carrera')
    resultados = cursor.fetchall()
    for fila in resultados:
        print(f"ID: {fila[0]} - Código: {fila[1]} - Nombre: {fila[2]} - Modalidad ID: {fila[3]}")

# Función para consultar una carrera por su código
def consultar_carrera_por_codigo(codigo):
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM carrera WHERE codigo = %s', (codigo,))
    resultado = cursor.fetchone()
    if resultado:
        print(f"ID: {resultado[0]} - Código: {resultado[1]} - Nombre: {resultado[2]} - Modalidad ID: {resultado[3]}")
    else:
        print(f"No se encontró la carrera con código {codigo}")

# Función para actualizar el nombre de una carrera dado su ID
def actualizar_carrera_por_id(carrera_id, nuevo_nombre):
    cursor = conn.cursor()
    cursor.execute('UPDATE carrera SET nombre = %s WHERE id = %s', (nuevo_nombre, carrera_id))
    conn.commit()

# Función para eliminar una carrera por su ID
def eliminar_carrera_por_id(carrera_id):
    cursor = conn.cursor()
    cursor.execute('DELETE FROM carrera WHERE id = %s', (carrera_id,))
    conn.commit()

# Función para contar el número total de registros en la tabla carrera
def contar_carreras():
    cursor = conn.cursor()
    cursor.execute('SELECT COUNT(*) FROM carrera')
    total = cursor.fetchone()[0]
    print(f"Total de carreras: {total}")

# Llamadas a las funciones de prueba
insertar_carrera('uwu', 'arquitectura', 1)
consultar_carreras()
consultar_carrera_por_codigo('uwu')
actualizar_carrera_por_id(4, 'ingenieria en ciencias de la computacion')
eliminar_carrera_por_id(3)
contar_carreras()

conn.close()

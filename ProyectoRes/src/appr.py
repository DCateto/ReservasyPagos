from flask import Flask, render_template, request , redirect, url_for,flash
from flask_mysqldb import MySQL
import mysql.connector
import os
template_dir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
template_dir = os.path.join(template_dir, 'src', 'templates')

app = Flask(__name__,template_folder=template_dir)
db = mysql.connector.connect(
    host='localhost',
    user='root',
    password = '12345nicolas',
    database= 'reservasrest',
    port= '3307',
    consume_results=True
)
app.secret_key='mysecretkey'
#Rutas de la app
@app.route('/')
def home():
    cur=db.cursor()
    cur.execute('DELETE FROM disponibilidad')
    cur.close()
    return render_template('index.html')

@app.route('/Reservas')
def reservas():
    cur=db.cursor()
    cur.execute('SELECT * FROM reservas')
    myresult= cur.fetchall()
    insertObject=[]
    columnNames=[column[0] for column in cur.description]
    for record in myresult:
        insertObject.append(dict(zip(columnNames, record)))
    cur.close()
    return render_template('Reservas.html', data=insertObject)
@app.route('/add_reserva', methods=['POST'])
def add_reserva():
    if request.method == 'POST':
        Nombre = request.form['Nombre']
        Contacto = request.form['Contacto']
        Mesa = request.form['Mesa']
        Hora_Reserva = request.form['Hora_Reserva']
        Hora_Salida = request.form['Hora_Salida']
        Fecha = request.form['Fecha']
        cur= db.cursor()
        cur.execute('SELECT MIN(IDReserva) FROM reservas WHERE Mesa=%s AND ((Hora_Reserva>=%s AND Hora_Reserva<=%s) OR (Hora_Salida>=%s AND Hora_Salida<=%s)) AND Fecha=%s', (Mesa, Hora_Reserva, Hora_Salida, Hora_Reserva, Hora_Salida, Fecha))
        Result=cur.fetchone()
        if Result[0]==None:
            cur.execute('INSERT INTO reservas ( Nombre , Contacto , Mesa , Hora_Reserva , Hora_Salida, Fecha ) VALUES (%s,%s,%s,%s,%s,%s)',(Nombre,Contacto,Mesa,Hora_Reserva,Hora_Salida, Fecha))
            flash('Reserva realizada.')
        else:
            flash('No hay disponibilidad.')
        db.commit()
    return redirect(url_for('reservas'))

@app.route('/Pagos')
def pagos():
    cur=db.cursor()
    cur.execute('SELECT * FROM pagos')
    myresult= cur.fetchall()
    insertObject=[]
    columnNames=[column[0] for column in cur.description]
    for record in myresult:
        insertObject.append(dict(zip(columnNames, record)))
    cur.close()
    return render_template('Pagos.html', data=insertObject)
@app.route('/add_pago', methods=['POST'])
def add_pago():
    if request.method == 'POST':
        Costo = request.form['Costo']
        Mesa = request.form['Mesa']
        Medio_de_pago= request.form['Medio_de_pago']
        Contacto = request.form['Contacto']
        Reserva = request.form['Reserva']
        HoraFecha = request.form['HoraFecha']
        cur= db.cursor()
        cur.execute('INSERT INTO pagos ( Costo , Mesa , Medio_de_pago , Contacto, Reserva, HoraFecha ) VALUES (%s,%s,%s,%s,%s,%s)',(Costo,Mesa,Medio_de_pago,Contacto,Reserva, HoraFecha))
        db.commit()
        flash('Pago realizado.')
    return redirect(url_for('pagos'))
@app.route('/delete/<string:id>')
def delete_reserva(id):
    cur=db.cursor()
    cur.execute('DELETE FROM reservas WHERE IDReserva={0}'.format(id))
    cur.execute('ALTER TABLE reservas AUTO_INCREMENT = {0}'.format(id))
    db.commit()
    flash('Reserva Eliminada.')
    return redirect(url_for('reservas'))

@app.route('/Disponibilidad')
def disponibilidad():
    cur=db.cursor()
    cur.execute('SELECT * FROM disponibilidad')
    myresult= cur.fetchall()
    insertObject=[]
    columnNames=[column[0] for column in cur.description]
    for record in myresult:
        insertObject.append(dict(zip(columnNames, record)))
    cur.close()
    return render_template('Disponibilidad.html', data=insertObject)
@app.route('/actDisponibilidad', methods=['POST'])
def actdisponibilidad():
    if request.method == 'POST':
        Hora_Reserva = request.form['Hora_Reserva']
        Hora_Salida = request.form['Hora_Salida']
        Fecha = request.form['Fecha']
        cur= db.cursor()
        cur.execute('DELETE FROM disponibilidad')
        cur.execute('INSERT INTO disponibilidad (IDMesa, Capacidad, Ambiente) SELECT IDMesa, Capacidad, Ambiente FROM Mesas WHERE Mesas.IDMesa NOT IN (SELECT Mesa FROM reservas WHERE (Hora_Reserva<=%s AND Hora_Salida<=%s) OR (Hora_Reserva>=%s AND Hora_Salida>=%s) OR Fecha!=%s)', (Hora_Reserva, Hora_Salida, Hora_Reserva, Hora_Salida, Fecha))
        db.commit()
    return redirect(url_for('disponibilidad'))
    
if __name__ == '__main__':
    app.run(port = 3000, debug = True)
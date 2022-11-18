from flask import Flask
from flask import render_template,request
from flaskext.mysql import MySQL

app =Flask(__name__,template_folder='theme',static_folder='theme',)

mysql=MySQL()
app.config['MYSQL_DATABASE_HOST']='localhost'
app.config['MYSQL_DATABASE_USER']='root'
app.config['MYSQL_DATABASE_PASSWORD']=''
app.config['MYSQL_DATABASE_DB']='quimica'
mysql.init_app(app)

@app.route('/')
def index():

    sql="SELECT * FROM `datoscontacto` WHERE `id` = 1"
    conn=mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql)
    datos_generales=cursor.fetchall()
    sql="SELECT * FROM `redes_sociales`"
    conn=mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql)
    redes_sociales=cursor.fetchall()

    conn.commit()
    print(datos_generales)
    
    return render_template('index.html',datos_generales=datos_generales[0],redes_sociales=redes_sociales)

@app.route('/presentacion')
def presentacion():

    sql="SELECT * FROM `datoscontacto` WHERE `id` = 1"
    conn=mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql)
    datos_generales=cursor.fetchall()
    sql="SELECT * FROM `redes_sociales`"
    conn=mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql)
    redes_sociales=cursor.fetchall()

    conn.commit()
    print(datos_generales)
    
    return render_template('presentacion.html',datos_generales=datos_generales[0],redes_sociales=redes_sociales)

if __name__=='__main__':
    app.run(debug=True)
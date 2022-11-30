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
    sql="SELECT * FROM `datos_presentacion`"
    conn=mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql)
    presentacion=cursor.fetchall()

    conn.commit()
    
    return render_template('presentacion.html',datos_generales=datos_generales[0],redes_sociales=redes_sociales,presentacion=presentacion)

@app.route('/mision_vision')
def misionvision():

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
    sql="SELECT * FROM `datos_misionvision`"
    conn=mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql)
    misionvision=cursor.fetchall()
    conn.commit()
    
    return render_template('mision_vision.html',datos_generales=datos_generales[0],redes_sociales=redes_sociales,
    mision=misionvision[0],vision=misionvision[1]
    )

@app.route('/objetivos')
def objetivos():

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
    sql="SELECT * FROM `datos_objetivos`"
    conn=mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql)
    presentacion=cursor.fetchall()

    conn.commit()
    
    return render_template('objetivos.html',datos_generales=datos_generales[0],redes_sociales=redes_sociales,presentacion=presentacion)

@app.route('/organizacion')
def organizacion():

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
    
    return render_template('organizacion.html',datos_generales=datos_generales[0],redes_sociales=redes_sociales)

@app.route('/comites')
def comites():

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
    sql="SELECT * FROM `datos_comites`"
    conn=mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql)
    comites=cursor.fetchall()

    conn.commit()
    
    return render_template('comites_de_trabajo.html',datos_generales=datos_generales[0],redes_sociales=redes_sociales,comites=comites) 

@app.route('/autoridades')
def autoridades():

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
    sql="SELECT * FROM `datos_autoridades`"
    conn=mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql)
    autoridades=cursor.fetchall()
    conn.commit()
    print(datos_generales)
    
    return render_template('autoridades.html',datos_generales=datos_generales[0],redes_sociales=redes_sociales
    ,autoridades=autoridades) 

@app.route('/historica')
def historica():

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
    sql="SELECT * FROM `datos_historica`"
    conn=mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql)
    historica=cursor.fetchall()

    conn.commit()
    
    return render_template('historica.html',datos_generales=datos_generales[0],redes_sociales=redes_sociales,historica=historica) 

@app.route('/plan')
def plan():

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
    sql="SELECT * FROM `datos_plan-estudios`"
    conn=mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql)
    plan=cursor.fetchall()

    conn.commit()
    
    return render_template('plan_de_estudios.html',datos_generales=datos_generales[0],redes_sociales=redes_sociales,plan=plan) 

@app.route('/mallacurricular')
def malla():

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
    sql="SELECT * FROM `datos_malla`"
    conn=mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql)
    malla=cursor.fetchall()

    conn.commit()
    
    return render_template('malla_curricular.html',datos_generales=datos_generales[0],redes_sociales=redes_sociales,malla=malla[0]) 

@app.route('/horarios')
def horarios():

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
    sql="SELECT * FROM `datos_horarios`"
    conn=mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql)
    horario=cursor.fetchall()

    conn.commit()
    
    return render_template('horarios.html',datos_generales=datos_generales[0],redes_sociales=redes_sociales,horario=horario[0]) 

@app.route('/tutorias')
def tutorias():

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
    sql="SELECT * FROM `datos_tutorias`"
    conn=mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql)
    tutorias=cursor.fetchall()

    conn.commit()
    print(datos_generales)
    
    return render_template('tutorias.html',datos_generales=datos_generales[0],redes_sociales=redes_sociales,
    tutoria=tutorias[0]) 

@app.route('/lineas_investigacion')
def lineas():

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

@app.route('/proyectos_investigacion')
def proyectos():

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

@app.route('/repositorio')
def repositorio():

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

@app.route('/reglamentos_escuela')
def reglamentos_escuela():

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

@app.route('/reglamentos_estudiantes')
def reglamentos_estudiantes():

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

@app.route('/seguridad')
def seguridad():

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

@app.route('/protocolos')
def protocolos():

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

@app.route('/planes')
def planes():

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

@app.route('/institucionales')
def institucionales():

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

@app.route('/docentes')
def docentes():

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

@app.route('/administrativos')
def administrativos():

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

@app.route('/postulantes_ingresantes')
def postulantes_ingresantes():

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

@app.route('/estudiantes_egresados')
def estudiantes_egresados():

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

@app.route('/laboratorios')
def laboratorios():

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

@app.route('/oficinas')
def oficinas():

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

@app.route('/faq')
def faq():

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

@app.route('/contacto')
def contactenos():

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

@app.route('/tramites')
def tramites():

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

if __name__=='__main__':
    app.run(debug=True)
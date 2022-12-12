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
    sql="SELECT * FROM `datos_lineas-inv`"
    conn=mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql)
    lineas=cursor.fetchall()

    conn.commit()
    
    return render_template('lineas.html',datos_generales=datos_generales[0],redes_sociales=redes_sociales,
    lineas=lineas) 

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
    sql="SELECT * FROM `datos_proyectos-inv`"
    conn=mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql)
    proyectos=cursor.fetchall()

    conn.commit()
    
    return render_template('proyectos.html',datos_generales=datos_generales[0],redes_sociales=redes_sociales,
    proyectos=proyectos)

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
    sql="SELECT * FROM `datos_repositorio-tesis`"
    conn=mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql)
    repositorio=cursor.fetchall()

    conn.commit()
    
    return render_template('repositorio_tesis.html',datos_generales=datos_generales[0],redes_sociales=redes_sociales,repositorio=repositorio[0])  

@app.route('/reglamento')
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
    sql="SELECT * FROM `datos_reglamento`"
    conn=mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql)
    reglamento=cursor.fetchall()

    conn.commit()
    
    return render_template('reglamento.html',datos_generales=datos_generales[0],redes_sociales=redes_sociales,reglamento=reglamento[0]) 

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
    sql="SELECT * FROM `datos_seguridad`"
    conn=mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql)
    seguridad=cursor.fetchall()

    conn.commit()
    
    return render_template('seguridad.html',datos_generales=datos_generales[0],redes_sociales=redes_sociales,seguridad=seguridad)

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
    sql="SELECT * FROM `datos_protocolos`"
    conn=mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql)
    protocolo=cursor.fetchall()

    conn.commit()

    return render_template('protocolo.html',datos_generales=datos_generales[0],redes_sociales=redes_sociales,protocolo=protocolo) 

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
    sql="SELECT * FROM `datos_planes`"
    conn=mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql)
    planes=cursor.fetchall()
    conn.commit()
    
    return render_template('planes.html',datos_generales=datos_generales[0],redes_sociales=redes_sociales,planes=planes) 

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
    sql="SELECT * FROM `datos_personal-docente`"
    conn=mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql)
    personal=cursor.fetchall()
    
    conn.commit()
    
    return render_template('personal-docente.html',datos_generales=datos_generales[0],redes_sociales=redes_sociales,personal=personal) 

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
    sql="SELECT * FROM `datos_personal-administrativo`"
    conn=mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql)
    personal=cursor.fetchall()

    conn.commit()
    
    return render_template('personal-administrativo.html',datos_generales=datos_generales[0],redes_sociales=redes_sociales,
    personal=personal) 

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
    sql="SELECT *,(CEPU_I+CEPU_II+CEPU_III+FASE_I+FASE_II+COLEGIOS+TRASLADO_EXTERNO+TRASLADO_INTERNO) as total,IF(postulantes_ingresantes=0, CONCAT('Postulantes - ',año), CONCAT('Ingresantes - ',año)) as titulo FROM `datos_postulantes-ingresantes` order by año asc, postulantes_ingresantes asc;"
    conn=mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql)
    postulantes_ingresantes=cursor.fetchall()

    conn.commit()
    
    return render_template('postulantes-ingresantes.html',datos_generales=datos_generales[0],redes_sociales=redes_sociales,postulantes_ingresantes=postulantes_ingresantes) 

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
    sql="SELECT * FROM `datos_estudiantes-egresados` order by año asc"
    conn=mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql)
    estudiantes_egresados=cursor.fetchall()
    conn.commit()
    
    return render_template('estudiantes-egresados.html',datos_generales=datos_generales[0],redes_sociales=redes_sociales,estudiantes_egresados=estudiantes_egresados) 

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
    
    return render_template('laboratorios.html',datos_generales=datos_generales[0],redes_sociales=redes_sociales) 

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
    
    return render_template('oficinas-administrativas.html',datos_generales=datos_generales[0],redes_sociales=redes_sociales) 

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
    sql="SELECT * FROM `datos_faq`"
    conn=mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql)
    faqs=cursor.fetchall()

    conn.commit()
    
    return render_template('preguntas_frecuentes.html',datos_generales=datos_generales[0],redes_sociales=redes_sociales,faqs=faqs) 

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
    
    return render_template('contacto.html',datos_generales=datos_generales[0],redes_sociales=redes_sociales) 

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
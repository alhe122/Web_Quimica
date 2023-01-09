from config import config
from flask import Flask
from flask import render_template,request, redirect,url_for,flash
from flaskext.mysql import MySQL
from flask_mysqldb import MySQL as MySQL2
from datetime import datetime
import os

from models.ModelUser import ModelUser

from models.entities.User import User

app =Flask(__name__,template_folder='theme',static_folder='theme',)

mysql=MySQL()
app.config['MYSQL_DATABASE_HOST']='localhost'
app.config['MYSQL_DATABASE_USER']='root'
app.config['MYSQL_DATABASE_PASSWORD']=''
app.config['MYSQL_DATABASE_DB']='quimica'
mysql.init_app(app)
db = MySQL2(app)

CARPETA=os.path.join('theme/images')
app.config['CARPETA']=CARPETA

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method=='POST':
        user = User(0,request.form['username'],request.form['password'])
        logged_user=ModelUser.login(db,user)
        if logged_user != None:
            if logged_user.password:
                #login_user(logged_user)
                return redirect(url_for('index_edit'))
            else:
                flash("Cantraseña Incorrecta...")
                return render_template('login.html')
        else:
            flash("Usuario no Encontrado...")
            return render_template('login.html')
    else:        
        return render_template('login.html')


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
    sql="SELECT * FROM `datos_index`"
    conn=mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql)
    index=cursor.fetchall()
    conn.commit()
    
    return render_template('index.html',datos_generales=datos_generales[0],redes_sociales=redes_sociales,datos_index=index[0],fotos=index[1:])

@app.route('/edit')
def index_edit():

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
    sql="SELECT * FROM `datos_index`"
    conn=mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql)
    index=cursor.fetchall()
    conn.commit()
    
    return render_template('index--edit.html',datos_generales=datos_generales[0],redes_sociales=redes_sociales,datos_index=index[0],fotos=index[1:])

@app.route('/update', methods=['POST'])
def index_update():

    _texto=request.form['texto_index']
    
    sql="UPDATE datos_index SET foto=%s WHERE id=1;"
    datos=(_texto)
    conn=mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql,datos)
    conn.commit()
    
    return redirect('/edit')

@app.route('/upload_imagen', methods=['POST'])
def index_updateimagen():

    _imagen=request.files['txtFile']
    tiempo=datetime.now().strftime("%Y%H%M%S")
    if _imagen.filename!='':
        newNameImage=tiempo+_imagen.filename
        _imagen.save("theme/images/"+newNameImage)
    
    sql="INSERT INTO `datos_index` (`id`,`foto`) VALUES (NULL,%s);"
    datos=(newNameImage)
    conn=mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql,datos)
    conn.commit()
    
    return redirect('/edit')

@app.route('/delete_imagen/<int:id>')
def index_deleteimage(id):
    conn=mysql.connect()
    cursor=conn.cursor()
    
    cursor.execute("SELECT foto FROM datos_index WHERE id=%s",id)
    fila=cursor.fetchall()
    os.remove(os.path.join(app.config['CARPETA'],fila[0][0]))
    
    cursor.execute("DELETE FROM datos_index WHERE id=%s",(id))
    conn.commit()
    return redirect('/edit')

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
    
    return render_template('presentacion.html',datos_generales=datos_generales[0],redes_sociales=redes_sociales,presentacion=presentacion[0])

@app.route('/presentacion_edit')
def presentacion_edit():

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
    
    return render_template('presentacion--edit.html',datos_generales=datos_generales[0],redes_sociales=redes_sociales,presentacion=presentacion[0])

@app.route('/presentacion_update', methods=['POST'])
def presentacion_update():

    _texto=request.form['texto_index']
    
    sql="UPDATE datos_presentacion SET texto=%s WHERE id=1;"
    datos=(_texto)
    conn=mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql,datos)
    conn.commit()
    
    return redirect('/presentacion_edit')

@app.route('/presentacion_upload/<int:id>', methods=['POST'])
def presentacion_updateimagen1(id):
    conn=mysql.connect()
    cursor=conn.cursor()
    _imagen=request.files['txtFile']
    tiempo=datetime.now().strftime("%Y%H%M%S")
    if _imagen.filename!='':
        newNameImage=tiempo+_imagen.filename
        _imagen.save("theme/images/"+newNameImage)
        if id==1:
            cursor.execute("SELECT imagen1 from datos_presentacion WHERE id=1")
            sql="UPDATE datos_presentacion SET imagen1=%s WHERE id=1;"
        else:
            cursor.execute("SELECT imagen2 from datos_presentacion WHERE id=1")
            sql="UPDATE datos_presentacion SET imagen2=%s WHERE id=1;"
        fila=cursor.fetchall()
        os.remove(os.path.join(app.config['CARPETA'],fila[0][0]))
        datos=(newNameImage)
        
    cursor.execute(sql,datos)
    conn.commit()
    
    return redirect('/presentacion_edit')

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

@app.route('/mision_vision_edit')
def misionvision_edit():

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
    
    return render_template('mision_vision--edit.html',datos_generales=datos_generales[0],redes_sociales=redes_sociales,
    mision=misionvision[0],vision=misionvision[1]
    )

@app.route('/mision_vision_update/<int:id>', methods=['POST'])
def misionvision_update(id):
    if id==1:
        _texto=request.form['texto_index1']
        sql="UPDATE datos_misionvision SET mision_vision=%s WHERE id=1;"
    else:
        _texto=request.form['texto_index2']
        sql="UPDATE datos_misionvision SET mision_vision=%s WHERE id=2;"
    datos=(_texto)
    conn=mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql,datos)
    conn.commit()
    
    return redirect('/mision_vision_edit')

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
    
    return render_template('objetivos.html',datos_generales=datos_generales[0],redes_sociales=redes_sociales,presentacion=presentacion[0])

@app.route('/objetivos_edit')
def objetivos_edit():

    sql="SELECT * FROM `datos_objetivos`"
    conn=mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql)
    presentacion=cursor.fetchall()

    conn.commit()
    
    return render_template('objetivos--edit.html',presentacion=presentacion[0])

@app.route('/objetivos_update', methods=['POST'])
def objetivos_update():

    _texto=request.form['texto_index']
    
    sql="UPDATE datos_objetivos SET texto=%s WHERE id=1;"
    datos=(_texto)
    conn=mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql,datos)
    conn.commit()
    
    return redirect('/objetivos_edit')

@app.route('/objetivos_upload', methods=['POST'])
def objetivos_upload():
    conn=mysql.connect()
    cursor=conn.cursor()
    _imagen=request.files['txtFile']
    tiempo=datetime.now().strftime("%Y%H%M%S")
    if _imagen.filename!='':
        newNameImage=tiempo+_imagen.filename
        _imagen.save("theme/images/"+newNameImage)
        cursor.execute("SELECT imagen from datos_objetivos WHERE id=1")
        sql="UPDATE datos_objetivos SET imagen=%s WHERE id=1;"
        fila=cursor.fetchall()
        if fila[0][0]!='' and os.path.exists('theme/images'+fila[0][0]):
            os.remove(os.path.join(app.config['CARPETA'],fila[0][0]))
        datos=(newNameImage)
        
    cursor.execute(sql,datos)
    conn.commit()
    
    return redirect('/objetivos_edit')

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
    sql="SELECT * FROM `datos_organizacion`"
    conn=mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql)
    organizacion=cursor.fetchall()

    conn.commit()
    
    return render_template('organizacion.html',datos_generales=datos_generales[0],redes_sociales=redes_sociales,organizacion=organizacion[0])

@app.route('/organizacion_edit')
def organizacion_edit():

    sql="SELECT * FROM `datos_organizacion`"
    conn=mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql)
    organizacion=cursor.fetchall()

    conn.commit()
    
    return render_template('organizacion--edit.html',organizacion=organizacion[0])

@app.route('/organizacion_update/<int:id>', methods=['POST'])
def organizacion_update(id):
    if id==1:
        _texto=request.form['texto_index']
        sql="UPDATE datos_organizacion SET texto=%s WHERE id=1;"
        datos=(_texto)
        conn=mysql.connect()
        cursor=conn.cursor()
        cursor.execute(sql,datos)
        conn.commit()
    else:
        conn=mysql.connect()
        cursor=conn.cursor()
        _imagen=request.files['txtFile']
        tiempo=datetime.now().strftime("%Y%H%M%S")
        if _imagen.filename!='':
            newNameImage=tiempo+_imagen.filename
            _imagen.save("theme/images/"+newNameImage)
            cursor.execute("SELECT imagen from datos_organizacion WHERE id=1")
            sql="UPDATE datos_organizacion SET imagen=%s WHERE id=1;"
            fila=cursor.fetchall()
            if fila[0][0]!='' and os.path.exists('theme/images'+fila[0][0]):
                os.remove(os.path.join(app.config['CARPETA'],fila[0][0]))
            datos=(newNameImage)
        cursor.execute(sql,datos)
        conn.commit()
    
    return redirect('/organizacion_edit')

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

@app.route('/comites_edit')
def comites_edit():

    sql="SELECT * FROM `datos_comites`"
    conn=mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql)
    comites=cursor.fetchall()

    conn.commit()
    
    return render_template('comites_de_trabajo--edit.html',comites=comites)

@app.route('/comites_update/<int:id>', methods=['POST'])
def comites_update(id):

    _texto1=request.form[str(id)+'txt1']
    _texto2=request.form[str(id)+'txt2']
    sql="UPDATE datos_comites SET `link` = %s, `texto_boton` = %s WHERE id=%s;"
    datos=(_texto2,_texto1,id)
    conn=mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql,datos)
    conn.commit()
    
    return redirect('/comites_edit') 

@app.route('/comites_delete/<int:id>')
def comites_delete(id):
    conn=mysql.connect()
    cursor=conn.cursor()
    cursor.execute("DELETE FROM datos_comites WHERE id=%s",(id))
    conn.commit()
    return redirect('/comites_edit')

@app.route('/comites_insert', methods=['POST'])
def comites_insert():
    _texto1=request.form['txt1']
    _texto2=request.form['txt2']
    sql="INSERT INTO `datos_comites` (`id`, `link`, `texto_boton`) VALUES (NULL, %s, %s);"
    datos=(_texto2,_texto1)
    conn=mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql,datos)
    conn.commit()
    
    return redirect('/comites_edit')

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

@app.route('/autoridades_edit')
def autoridades_edit():

    sql="SELECT * FROM `datos_autoridades`"
    conn=mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql)
    autoridades=cursor.fetchall()
    conn.commit()
    
    return render_template('autoridades--edit.html',autoridades=autoridades) 

@app.route('/autoridades_update/<int:id>', methods=['POST'])
def autoridades_update(id):

    _texto1=request.form[str(id)+'txt1']
    _texto2=request.form[str(id)+'txt2']
    sql="UPDATE datos_autoridades SET `cargo` = %s, `nombre` = %s WHERE id=%s;"
    datos=(_texto1,_texto2,id)
    conn=mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql,datos)
    conn.commit()
    
    return redirect('/autoridades_edit') 

@app.route('/autoridades_delete/<int:id>')
def autoridades_delete(id):
    conn=mysql.connect()
    cursor=conn.cursor()
    cursor.execute("DELETE FROM datos_autoridades WHERE id=%s",(id))
    conn.commit()
    return redirect('/autoridades_edit')

@app.route('/autoridades_insert', methods=['POST'])
def autoridades_insert():
    _texto1=request.form['txt1']
    _texto2=request.form['txt2']
    sql="INSERT INTO `datos_autoridades` (`id`, `cargo`, `nombre`) VALUES (NULL, %s, %s);"
    datos=(_texto1,_texto2)
    conn=mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql,datos)
    conn.commit()
    
    return redirect('/autoridades_edit')

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
    
    return render_template('historica.html',datos_generales=datos_generales[0],redes_sociales=redes_sociales,historica=historica[0])

@app.route('/historica_edit')
def historica_edit():

    sql="SELECT * FROM `datos_historica`"
    conn=mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql)
    historica=cursor.fetchall()

    conn.commit()
    
    return render_template('historica--edit.html',historica=historica[0])

@app.route('/historica_update', methods=['POST'])
def historica_update():

    _texto=request.form['texto_index']
    
    sql="UPDATE datos_historica SET texto=%s WHERE id=1;"
    datos=(_texto)
    conn=mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql,datos)
    conn.commit()
    
    return redirect('/historica_edit')  

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

@app.route('/plan_edit')
def plan_edit():

    sql="SELECT * FROM `datos_plan-estudios`"
    conn=mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql)
    plan=cursor.fetchall()

    conn.commit()
    
    return render_template('plan_de_estudios--edit.html',plan=plan) 

@app.route('/plan_update/<int:id>', methods=['POST'])
def plan_update(id):

    _texto1=request.form[str(id)+'txt1']
    _texto2=request.form[str(id)+'txt2']
    sql="UPDATE `datos_plan-estudios` SET `link` = %s, `texto_boton` = %s WHERE id=%s;"
    datos=(_texto2,_texto1,id)
    conn=mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql,datos)
    conn.commit()
    
    return redirect('/plan_edit') 

@app.route('/plan_delete/<int:id>')
def plan_delete(id):
    conn=mysql.connect()
    cursor=conn.cursor()
    cursor.execute("DELETE FROM `datos_plan-estudios` WHERE id=%s",(id))
    conn.commit()
    return redirect('/plan_edit')

@app.route('/plan_insert', methods=['POST'])
def plan_insert():
    _texto1=request.form['txt1']
    _texto2=request.form['txt2']
    sql="INSERT INTO `datos_plan-estudios` (`id`, `link`, `texto_boton`) VALUES (NULL, %s, %s);"
    datos=(_texto2,_texto1)
    conn=mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql,datos)
    conn.commit()
    
    return redirect('/plan_edit')

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

@app.route('/mallacurricular_edit')
def malla_edit():

    sql="SELECT * FROM `datos_malla`"
    conn=mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql)
    malla=cursor.fetchall()

    conn.commit()
    
    return render_template('malla_curricular--edit.html',malla=malla[0])

@app.route('/mallacurricular_update/<int:id>', methods=['POST'])
def mallacurricular_update(id):
    if id==1:
        _texto=request.form['txtText']
        sql="UPDATE datos_malla SET texto=%s WHERE id=1;"
        datos=(_texto)
        conn=mysql.connect()
        cursor=conn.cursor()
        cursor.execute(sql,datos)
        conn.commit()
    elif id==2:
        _texto1=request.form['txtBoton1']
        _texto2=request.form['txtBoton2']
        sql="UPDATE datos_malla SET `link` = %s, `texto_boton`=%s WHERE id=1;"
        datos=(_texto2,_texto1)
        conn=mysql.connect()
        cursor=conn.cursor()
        cursor.execute(sql,datos)
        conn.commit()
    else:
        conn=mysql.connect()
        cursor=conn.cursor()
        _imagen=request.files['txtFile']
        tiempo=datetime.now().strftime("%Y%H%M%S")
        if _imagen.filename!='':
            newNameImage=tiempo+_imagen.filename
            _imagen.save("theme/images/"+newNameImage)
            cursor.execute("SELECT imagen from datos_malla WHERE id=1")
            sql="UPDATE datos_malla SET imagen=%s WHERE id=1;"
            fila=cursor.fetchall()
            if fila[0][0]!='' and os.path.exists('theme/images'+fila[0][0]):
                os.remove(os.path.join(app.config['CARPETA'],fila[0][0]))
            datos=(newNameImage)
        cursor.execute(sql,datos)
        conn.commit()
    
    return redirect('/mallacurricular_edit') 

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

@app.route('/horarios_edit')
def horarios_edit():

    sql="SELECT * FROM `datos_horarios`"
    conn=mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql)
    horario=cursor.fetchall()

    conn.commit()
    
    return render_template('horarios--edit.html',horario=horario[0]) 

@app.route('/horarios_update', methods=['POST'])
def horarios_update():

    _texto1=request.form['txtBoton1']
    _texto2=request.form['txtBoton2']
    sql="UPDATE datos_horarios SET `link` = %s, `texto_boton`=%s WHERE id=1;"
    datos=(_texto2,_texto1)
    conn=mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql,datos)
    conn.commit()
    
    return redirect('/horarios_edit') 

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

@app.route('/tutorias_edit')
def tutorias_edit():
    
    sql="SELECT * FROM `datos_tutorias`"
    conn=mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql)
    tutorias=cursor.fetchall()

    conn.commit()
    
    return render_template('tutorias--edit.html',tutorias=tutorias) 

@app.route('/tutorias_update/<int:id>', methods=['POST'])
def tutorias_update(id):

    _texto1=request.form[str(id)+'txt1']
    _texto2=request.form[str(id)+'txt2']
    sql="UPDATE `datos_tutorias` SET `texto_boton`= %s,`link` = %s  WHERE id=%s;"
    datos=(_texto1,_texto2,id)
    conn=mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql,datos)
    conn.commit()
    
    return redirect('/tutorias_edit') 

@app.route('/tutorias_delete/<int:id>')
def tutorias_delete(id):
    conn=mysql.connect()
    cursor=conn.cursor()
    cursor.execute("DELETE FROM `datos_tutorias` WHERE id=%s",(id))
    conn.commit()
    return redirect('/tutorias_edit')

@app.route('/tutorias_insert', methods=['POST'])
def tutorias_insert():
    _texto1=request.form['txt1']
    _texto2=request.form['txt2']
    sql="INSERT INTO `datos_tutorias` (`id`, `link`, `texto_boton`) VALUES (NULL, %s, %s);"
    datos=(_texto2,_texto1)
    conn=mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql,datos)
    conn.commit()
    
    return redirect('/tutorias_edit')

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

@app.route('/lineas_investigacion_edit')
def lineas_edit():

    sql="SELECT * FROM `datos_lineas-inv`"
    conn=mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql)
    lineas=cursor.fetchall()

    conn.commit()
    
    return render_template('lineas--edit.html',lineas=lineas) 

@app.route('/lineas_investigacion_update/<int:id>', methods=['POST'])
def lineas_investigacion_update(id):

    _texto1=request.form[str(id)+'txt1']
    _texto2=request.form[str(id)+'txt2']
    _texto3=request.form[str(id)+'txt3']
    _texto4=request.form[str(id)+'txt4']
    sql="UPDATE `datos_lineas-inv` SET `titulo` = %s,`texto` = %s,`link` = %s,`texto_boton`= %s  WHERE id=%s;"
    datos=(_texto1,_texto2,_texto3,_texto4,id)
    conn=mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql,datos)
    conn.commit()
    
    return redirect('/lineas_investigacion_edit') 

@app.route('/lineas_investigacion_delete/<int:id>')
def lineas_investigacion_delete(id):
    conn=mysql.connect()
    cursor=conn.cursor()
    cursor.execute("DELETE FROM `datos_lineas-inv` WHERE id=%s",(id))
    conn.commit()
    return redirect('/lineas_investigacion_edit')

@app.route('/lineas_investigacion_insert', methods=['POST'])
def lineas_investigacion_insert():
    _texto1=request.form['txt1']
    _texto2=request.form['txt2']
    _texto3=request.form['txt3']
    _texto4=request.form['txt4']
    sql="INSERT INTO `datos_lineas-inv` (`id`, `titulo`,`texto`,`link`,`texto_boton`) VALUES (NULL,%s,%s, %s, %s);"
    datos=(_texto1,_texto2,_texto3,_texto4)
    conn=mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql,datos)
    conn.commit()
    
    return redirect('/lineas_investigacion_edit') 

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

@app.route('/proyectos_investigacion_edit')
def proyectos_edit():

    sql="SELECT * FROM `datos_proyectos-inv`"
    conn=mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql)
    proyectos=cursor.fetchall()

    conn.commit()
    
    return render_template('proyectos--edit.html',proyectos=proyectos)

@app.route('/proyectos_investigacion_update/<int:id>', methods=['POST'])
def proyectos_investigacion_update(id):

    _texto1=request.form[str(id)+'txt1']
    _texto2=request.form[str(id)+'txt2']
    _texto3=request.form[str(id)+'txt3']
    sql="UPDATE `datos_proyectos-inv` SET `titulo` = %s,`link` = %s,`texto_boton`= %s  WHERE id=%s;"
    datos=(_texto1,_texto2,_texto3,id)
    conn=mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql,datos)
    conn.commit()
    
    return redirect('/proyectos_investigacion_edit') 

@app.route('/proyectos_investigacion_delete/<int:id>')
def proyectos_investigacion_delete(id):
    conn=mysql.connect()
    cursor=conn.cursor()
    cursor.execute("DELETE FROM `datos_proyectos-inv` WHERE id=%s",(id))
    conn.commit()
    return redirect('/proyectos_investigacion_edit')

@app.route('/proyectos_investigacion_insert', methods=['POST'])
def proyectos_investigacion_insert():
    _texto1=request.form['txt1']
    _texto2=request.form['txt2']
    _texto3=request.form['txt3']
    sql="INSERT INTO `datos_proyectos-inv` (`id`, `titulo`,`link`,`texto_boton`) VALUES (NULL,%s, %s, %s);"
    datos=(_texto1,_texto2,_texto3)
    conn=mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql,datos)
    conn.commit()
    
    return redirect('/proyectos_investigacion_edit') 

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

@app.route('/repositorio_edit')
def repositorio_edit():

    sql="SELECT * FROM `datos_repositorio-tesis`"
    conn=mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql)
    repositorio=cursor.fetchall()

    conn.commit()
    
    return render_template('repositorio_tesis--edit.html',repositorio=repositorio[0])  

@app.route('/repositorio_update', methods=['POST'])
def repositorio_update():

    _texto1=request.form['txtBoton1']
    _texto2=request.form['txtBoton2']
    sql="UPDATE `datos_repositorio-tesis` SET `link` = %s, `texto_boton`=%s WHERE id=1;"
    datos=(_texto2,_texto1)
    conn=mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql,datos)
    conn.commit()
    
    return redirect('/repositorio_edit') 

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

@app.route('/reglamento_edit')
def reglamentos_escuela_edit():

    sql="SELECT * FROM `datos_reglamento`"
    conn=mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql)
    reglamento=cursor.fetchall()

    conn.commit()
    
    return render_template('reglamento--edit.html',reglamento=reglamento[0]) 

@app.route('/reglamento_update', methods=['POST'])
def reglamento_update():

    _texto1=request.form['txtBoton1']
    _texto2=request.form['txtBoton2']
    sql="UPDATE `datos_reglamento` SET `link` = %s, `texto_boton`=%s WHERE id=1;"
    datos=(_texto2,_texto1)
    conn=mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql,datos)
    conn.commit()
    
    return redirect('/reglamento_edit') 

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

@app.route('/seguridad_edit')
def seguridad_edit():

    sql="SELECT * FROM `datos_seguridad`"
    conn=mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql)
    seguridad=cursor.fetchall()

    conn.commit()
    
    return render_template('seguridad--edit.html',seguridad=seguridad)

@app.route('/seguridad_update/<int:id>', methods=['POST'])
def seguridad_update(id):

    _texto1=request.form[str(id)+'txt1']
    _texto2=request.form[str(id)+'txt2']
    _texto3=request.form[str(id)+'txt3']
    sql="UPDATE `datos_seguridad` SET `titulo` = %s,`link` = %s,`texto_boton`= %s  WHERE id=%s;"
    datos=(_texto1,_texto2,_texto3,id)
    conn=mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql,datos)
    conn.commit()
    
    return redirect('/seguridad_edit') 

@app.route('/seguridad_delete/<int:id>')
def seguridad_delete(id):
    conn=mysql.connect()
    cursor=conn.cursor()
    cursor.execute("DELETE FROM `datos_seguridad` WHERE id=%s",(id))
    conn.commit()
    return redirect('/seguridad_edit')

@app.route('/seguridad_insert', methods=['POST'])
def seguridad_insert():
    _texto1=request.form['txt1']
    _texto2=request.form['txt2']
    _texto3=request.form['txt3']
    sql="INSERT INTO `datos_seguridad` (`id`, `titulo`,`link`,`texto_boton`) VALUES (NULL,%s, %s, %s);"
    datos=(_texto1,_texto2,_texto3)
    conn=mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql,datos)
    conn.commit()
    
    return redirect('/seguridad_edit') 


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
    sql="SELECT *,@rownum:=@rownum+1 ‘nro’ FROM `datos_faq`, (SELECT @rownum:=0) r"
    conn=mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql)
    faqs=cursor.fetchall()
    print(faqs)
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
    sql="SELECT * FROM `datos_tramites`"
    conn=mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql)
    tramites=cursor.fetchall()

    conn.commit()
    
    return render_template('tramites.html',datos_generales=datos_generales[0],tramites_texto=tramites[0],tramites=tramites[1:]) 

if __name__=='__main__':
    app.config.from_object(config['development'])
    app.run()
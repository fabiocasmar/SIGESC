import re
# -*- coding: utf-8 -*-
### required - do no delete
def user(): return dict(form=auth())
def download(): return response.download(request,db)
def call(): return service()
### end requires
def index():
	form=auth.login()
	return dict(form=form)


def error():
    return dict()

@auth.requires_login()
def vista_admin():    
    msj= 'Bienvenid@ %s %s' % (auth.user.first_name,auth.user.last_name)

    if auth.has_membership('Proponentes'):    	
    	redirect(URL('vista_proponente'))

    if auth.has_membership('Estudiantes'):
    	redirect(URL('vista_estudiante'))

    return dict(bienvenida=msj)

@auth.requires_membership('Proponentes')
def vista_proponente():
	def my_form_processing(form):
		if not re.match('[1-9][0-9]{0,8}$', form.vars.f_cedula):
			form.errors.f_cedula = 'El formato válido de cédula es: 1232382'
		if not re.match('(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)', form.vars.f_email):
			form.errors.f_email = 'El formato válido de email es example@example.com'
		if not re.match('\d{7,13}', form.vars.f_telefono):
			form.errors.f_telefono = 'El formato válido de telefono es 08002023223'

	msj = 'Bienvenid@ %s %s' % (auth.user.first_name,auth.user.last_name)
	form = SQLFORM(db.t_proponente,
		fields = ['f_tipoprop','f_cedula', 'f_sexo', 'f_telefono'], formstyle='table3cols')

	user = db.auth_user[auth.user.id]
	form.vars.f_user = user
	form.vars.f_email = auth.user.email
	form.vars.f_nombre = auth.user.first_name
	form.vars.f_apellido = auth.user.last_name
	if form.process(onvalidation=my_form_processing, keepvalues=True).accepted:
		response.flash = 'form accepted'
	elif form.errors:
		response.flash = 'form has errors'
	else:
		response.flash = 'please fill out the form'
	return dict(form=form, bienvenida=msj)

@auth.requires_membership('Estudiantes')
def vista_estudiante():
	def my_form_processing(form):
		if not re.match('\d{2}-\d{5}$', form.vars.f_usbid):
			form.errors.f_usbid = 'El formato válido de carnet es: 00-00000'
		if not re.match('[1-9][0-9]{0,8}$', form.vars.f_cedula):
			form.errors.f_cedula = 'El formato válido de cédula es: 1232382'
		if not re.match('(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)', form.vars.f_email):
			form.errors.f_email = 'El formato válido de email es example@example.com'
		if not re.match('\d{7,13}', form.vars.f_telefono):
			form.errors.f_telefono = 'El formato válido de telefono es 08002023223'

	msj = 'Bienvenid@ %s %s' % (auth.user.first_name,auth.user.last_name)
	form = SQLFORM(db.t_estudiante,
    	fields = ['f_usbid','f_cedula', 'f_carrera', 'f_sede', 'f_sexo', 'f_telefono', 'f_direccion'], formstyle='table3cols')

	user = db.auth_user[auth.user.id]
	form.vars.f_user = user
	form.vars.f_email = auth.user.email
	form.vars.f_nombre = auth.user.first_name
	form.vars.f_apellido = auth.user.last_name
	if request.env.request_method =='POST':
	    if form.process(onvalidation=my_form_processing, keepvalues=True).accepted:
	        response.flash = 'form accepted'
	    elif form.errors:
	        response.flash = 'form has errors'
	    else:
	        response.flash = 'please fill out the form'
	return dict(form=form, bienvenida=msj)

@auth.requires_membership('Administrador')
def estudiantes():
    def my_form_processing(form):
        if not re.match('\d{2}-\d{5}$', form.vars.f_usbid):
            form.errors.f_usbid = 'El formato válido de carnet es: 00-00000'
        if not re.match('[1-9][0-9]{0,8}$', form.vars.f_cedula):
            form.errors.f_cedula = 'El formato válido de cédula es: 1232382'
        if not re.match('(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)', form.vars.f_email):
            form.errors.f_email = 'El formato válido de email es example@example.com'
        if not re.match('\d{7,13}', form.vars.f_telefono):
            form.errors.f_telefono = 'El formato válido de telefono es 08002023223'

    form = SQLFORM(db.t_estudiante,formstyle='table3cols')

    if form.process(onvalidation=my_form_processing).accepted:
        response.flash = '1'
        
    elif form.errors:
        response.flash = '0'
        
    else:
        response.flash = 'Llene el formulario'
    return dict(form=form, est=db().select(db.t_estudiante.ALL),message=T(response.flash))

@auth.requires_membership('Administrador')
def proponentes():
    def my_form_processing(form):
        if not re.match('[1-9][0-9]{0,8}$', form.vars.f_cedula):
            form.errors.f_cedula = 'El formato válido de cédula es: 1232382'
        if not re.match('(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)', form.vars.f_email):
            form.errors.f_email = 'El formato válido de email es example@example.com'
        if not re.match('\d{7,13}', form.vars.f_telefono):
            form.errors.f_telefono = 'El formato válido de telefono es 08002023223'

    form = SQLFORM(db.t_proponente)
    if form.process(onvalidation=my_form_processing).accepted:
        response.flash = 'form accepted'
    elif form.errors:
        response.flash = 'form has errors'
    else:
        response.flash = 'please fill out the form'
    return dict(form=form, proponentes=db().select(db.t_proponente.ALL),message=T(response.flash))

@auth.requires_membership('Administrador')
def tutores():
    def my_form_processing(form):
        if form.vars.f_usbid:
            if not re.match('\d{2}-\d{5}$', form.vars.f_usbid) and not re.match('[a-zA-Z0-9_.+-]+', form.vars.f_usbid):
                form.errors.f_usbid = 'usbid invalido'
        if not re.match('[1-9][0-9]{0,8}$', form.vars.f_cedula):
            form.errors.f_cedula = 'El formato válido de cédula es: 1232382'
        if not re.match('(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)', form.vars.f_email):
            form.errors.f_email = 'El formato válido de email es example@example.com'
        if not re.match('\d{7,13}', form.vars.f_telefono):
            form.errors.f_telefono = 'El formato válido de telefono es 08002023223'
    form = SQLFORM(db.t_tutor)
    if form.process(onvalidation=my_form_processing).accepted:
        response.flash = 'form accepted'
    elif form.errors:
        response.flash = 'form has errors'
    else:
        response.flash = 'please fill out the form'
    return dict(form=form, tutores=db().select(db.t_tutor.ALL),message=T(response.flash))


@auth.requires_membership('Administrador')
def moderarProyectos():
    return dict(proyectos=db().select(db.t_cursa.ALL))


@auth.requires_login()
def estado_manage():
    form = SQLFORM.smartgrid(db.t_estado,onupdate=auth.archive)
    return dict(form=form)

@auth.requires_membership('Administrador')
def sedes():
    def my_form_processing(form):
        if not re.match('[A-ZÁÉÍÓÚÑ]|[A-ZÁÉÍÓÚÑa]|[a-zñáéíóúäëïöü]*$', form.vars.f_nombre):
            form.errors.f_nombre = 'Sólo puede contener letras'
    form = SQLFORM(db.t_sede)
    if form.process(onvalidation=my_form_processing).accepted:
        response.flash = 'form accepted'
    elif form.errors:
        response.flash = 'form has errors'
    else:
        response.flash = 'please fill out the form'    
    return dict(form=form, sedes=db().select(db.t_sede.ALL),message=T(response.flash))

@auth.requires_membership('Administrador')
def areas():
    def my_form_processing(form):
        if not re.match('[A-ZÁÉÍÓÚÑ]|[A-ZÁÉÍÓÚÑa]|[a-zñáéíóúäëïöü]*$', form.vars.f_nombre):
            form.errors.f_nombre = 'Sólo puede contener letras'
    form = SQLFORM(db.t_area,onupdate=auth.archive)
    if form.process(onvalidation=my_form_processing).accepted:
        response.flash = 'form accepted'
    elif form.errors:
        response.flash = 'form has errors'
    else:
        response.flash = 'please fill out the form'
    return dict(form=form, areas=db().select(db.t_area.ALL),message=T(response.flash))

@auth.requires_membership('Administrador')
def proyectos():
    def my_form_processing(form):
        if not re.match('\d{4}', form.vars.f_codigo):
            form.errors.f_codigo = 'El formato válido del código son 4 dígitos'
        if not re.match('[A-ZÁÉÍÓÚÑ]|[A-ZÁÉÍÓÚÑa]|[a-zñáéíóúäëïöü]*$', form.vars.f_nombre):
            form.errors.f_nombre = 'Sólo puede contener letras'
        if not re.match('[A-ZÁÉÍÓÚÑ]|[A-ZÁÉÍÓÚÑa]|[a-zñáéíóúäëïöü]*$', form.vars.f_descripcion):
            form.errors.f_descripcion = 'Sólo puede contener letras'
        if not re.match('\d{2}', form.vars.f_version):
            form.errors.f_codigo = 'El formato válido de la versión son 2 dígitos'
    form = SQLFORM(db.t_project,onupdate=auth.archive) 
    if form.process(onvalidation=my_form_processing).accepted:
        response.flash = 'form accepted'
    elif form.errors:
        response.flash = 'form has errors'
    else:
        response.flash = 'please fill out the form'
    return dict(form=form, proyectos=db().select(db.t_project.ALL),message=T(response.flash))


@auth.requires_membership('Administrador')
def validarProyectoEstudiante():
    idProyecto = long(request.args[0])
    db(db.t_cursa.id==idProyecto).update(f_state="2")
    return dict(proyecto=idProyecto)

def cursa():
    idProyecto = long(request.args[0])
    idEstudiante = long(request.args[1])
    return dict(proyectos=db(db.t_project.id==idProyecto).select(),estudianteID=idEstudiante,idProyecto=idProyecto)

def registrarProyectoEstudiante():
    idProyecto = long(request.args[0])
    idEstudiante = long(request.args[1])
    db.t_cursa.insert(f_estudiante=idEstudiante,f_project=idProyecto,f_state="3")
    return dict(proyecto=idProyecto,estudianteID=idEstudiante)

@auth.requires_membership('Administrador')
def sede_manage():
    form = SQLFORM.smartgrid(db.t_sede,onupdate=auth.archive)
    return locals()

@auth.requires_membership('Administrador')
def comunidad_manage():
    form = SQLFORM.smartgrid(db.t_comunidad,onupdate=auth.archive)
    return locals()

@auth.requires_membership('Administrador')
def area_manage():
    form = SQLFORM.smartgrid(db.t_area,onupdate=auth.archive)
    return locals()

@auth.requires_membership('Administrador')
def sexo_manage():
    form = SQLFORM.smartgrid(db.t_sexo,onupdate=auth.archive)
    return locals()

def estudiante_manage():
    form = SQLFORM.smartgrid(db.t_estudiante.id==request.args(0))
    if form.process().accepted:
        response.flash = 'form accepted'
    elif form.errors:
        response.flash = 'form has errors'
    else:
        response.flash = 'please fill out the form'
    return locals()

@auth.requires_login()
def proponente_manage():
    form = SQLFORM.smartgrid(db.t_proponente,onupdate=auth.archive)
    return locals()

@auth.requires_login()
def tutor_manage():
    form = SQLFORM.smartgrid(db.t_tutor,onupdate=auth.archive)
    return locals()

@auth.requires_login()
def proyecto_manage():
    form = SQLFORM.smartgrid(db.t_proyecto,onupdate=auth.archive)
    return locals()

@auth.requires_login()
def condicion_manage():
    form = SQLFORM.smartgrid(db.t_condicion,onupdate=auth.archive)
    return locals()

@auth.requires_login()
def caracterisicas_manage():
    form = SQLFORM.smartgrid(db.t_caracterisicas,onupdate=auth.archive)
    return locals()

@auth.requires_login()
def cursa_manage():
    form = SQLFORM.smartgrid(db.t_cursa,onupdate=auth.archive)
    return locals()

@auth.requires_login()
def carrera_manage():
    form = SQLFORM.smartgrid(db.t_carrera,onupdate=auth.archive)
    return locals()

@auth.requires_login()
def tipoprop_manage():
    form = SQLFORM.smartgrid(db.t_tipoprop,onupdate=auth.archive)
    return locals()

@auth.requires_login()
def relacionestproy_manage():
    form = SQLFORM.smartgrid(db.t_relacionestproy,onupdate=auth.archive)
    return locals()

def sedesDetalles():
    x = long (request.args[0])
    return dict(rows = db(db.t_sede.id==x).select())


def estudianteProyectos():
    x = long (request.args[0])
    return dict(rows = db(db.t_estudiante.id==x).select(),proyectos=db().select(db.t_project.ALL),estudianteID=x)

def estudiantesDetalles():
    x = long (request.args[0])
    #return dict(rows = db(db.t_estudiante.id==x).select())
    return dict(rows = db(db.t_estudiante.id==x).select(),estudianteId=x)

def tutoresDetalles():
    x = long (request.args[0])
    return dict(rows = db(db.t_tutor.id==x).select())

def proyectosDetalles():
    x = long (request.args[0])
    return dict(rows = db(db.t_project.id==x).select())    

def proponentesDetalles():
    x = long (request.args[0])
    return dict(rows = db(db.t_proponente.id==x).select())    

def areasDetalles():
    x = long (request.args[0])
    return dict(rows = db(db.t_area.id==x).select())    

def estudiantesEditar():
    x = long (request.args[0])
    #return dict(rows = db(db.t_sede.id==x).select())
    record = db.t_estudiante(request.args[0])
    form = SQLFORM(db.t_estudiante, record, deletable = True)
    if form.process().accepted:
        response.flash = 'form accepted'
    elif form.errors:
        response.flash = 'form has errors'
    elif not record:
        return dict('La sede ha sido eliminada')
    return dict(form = form)

def areasEditar():
    x = long (request.args[0])
    #return dict(rows = db(db.t_sede.id==x).select())
    record = db.t_area(request.args[0])
    form = SQLFORM(db.t_area, record, deletable = True)
    if form.process().accepted:
        response.flash = 'form accepted'
    elif form.errors:
        response.flash = 'form has errors'
    elif not record:
        return dict('La sede ha sido eliminada')
    return dict(form = form)

def sedesEditar():
    x = long (request.args[0])
    #return dict(rows = db(db.t_sede.id==x).select())
    record = db.t_sede(request.args[0])
    form = SQLFORM(db.t_sede, record, deletable = True)
    if form.process().accepted:
        response.flash = 'form accepted'
    elif form.errors:
        response.flash = 'form has errors'
    elif not record:
        return dict('La sede ha sido eliminada')
    return dict(form = form)

def proponentesEditar():
    x = long (request.args[0])
    #return dict(rows = db(db.t_sede.id==x).select())
    record = db.t_proponente(request.args[0])
    form = SQLFORM(db.t_proponente, record, deletable = True)
    if form.process().accepted:
        response.flash = 'form accepted'
    elif form.errors:
        response.flash = 'form has errors'
    elif not record:
        return dict('La sede ha sido eliminada')
    return dict(form = form)

def tutoresEditar():
    x = long (request.args[0])
    #return dict(rows = db(db.t_sede.id==x).select())
    record = db.t_tutor(request.args[0])
    form = SQLFORM(db.t_tutor, record, deletable = True)
    if form.process().accepted:
        response.flash = 'form accepted'
    elif form.errors:
        response.flash = 'form has errors'
    elif not record:
        return dict('El tutor ha sido eliminado')
    return dict(form = form)

def proyectosEditar():
    x = long (request.args[0])
    #return dict(rows = db(db.t_sede.id==x).select())
    record = db.t_project(request.args[0])
    form = SQLFORM(db.t_project, record, deletable = True)
    if form.process().accepted:
        response.flash = 'form accepted'
    elif form.errors:
        response.flash = 'form has errors'
    elif not record:
        return dict('La sede ha sido eliminada')
    return dict(form = form)

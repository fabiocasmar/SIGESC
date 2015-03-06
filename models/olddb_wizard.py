=======
### we prepend t_ to tablenames and f_ to fieldnames for disambiguity


########################################
db.define_table('t_sede',
    Field('f_nombre', type='string', notnull=True,
          label=T('Nombre')),
    auth.signature,
    format='%(f_nombre)s',
    migrate=settings.migrate)

db.define_table('t_sede_archive',db.t_sede,Field('current_record','reference t_sede',readable=False,writable=False))

########################################
db.define_table('t_sexo',
    Field('f_tipo', type='string', notnull=True,
          label=T('Tipo')),
    auth.signature,
    format='%(f_tipo)s',
    migrate=settings.migrate)

db.define_table('t_sexo_archive',db.t_sexo,Field('current_record','reference t_sexo',readable=False,writable=False))

########################################
db.define_table('t_tutor',
    Field('f_usbid', type='string', notnull=False,
          label=T('Usbid')),
    Field('f_cedula', type='string', notnull=True,
          label=T('Cedula')),
    Field('f_nombre', type='string', notnull=True,
          label=T('Nombre')),
    Field('f_apellido', type='string', notnull=True,
          label=T('Apellido')),
    Field('f_sede', type='reference t_sede', notnull=True,
          label=T('Sede')),
    Field('f_email', type='string', notnull=True,
          label=T('Email')),
    Field('f_sexo', type='reference t_sexo', notnull=True,
          label=T('Sexo')),
    Field('f_telefono', type='string', notnull=True,
          label=T('Telefono')),
    Field('f_direccion', type='text', notnull=True,
          label=T('Direccion')),
    auth.signature,
    format='%(f_usbid)s',
    migrate=settings.migrate)

db.define_table('t_tutor_archive',db.t_tutor,Field('current_record','reference t_tutor',readable=False,writable=False))

########################################
db.define_table('t_tipoprop',
    Field('f_tipo', type='string', notnull=True,
          label=T('Tipo')),
    auth.signature,
    format='%(f_tipo)s',
    migrate=settings.migrate)

db.define_table('t_tipoprop_archive',db.t_tipoprop,Field('current_record','reference t_tipoprop',readable=False,writable=False))

########################################
#db.define_table('t_proyecto',
#    Field('f_codigo', type='string', notnull=True,
#          label=T('Codigo')),
#    auth.signature,
#    format='%(f_codigo)s',
#    migrate=settings.migrate)

#db.define_table('t_proyecto_archive',db.t_proyecto,Field('current_record','reference t_proyecto',readable=False,writable=False))

########################################
db.define_table('t_area',
    Field('f_nombre', type='string', notnull=True,
          label=T('Nombre')),
    auth.signature,
    format='%(f_nombre)s',
    migrate=settings.migrate)

db.define_table('t_area_archive',db.t_area,Field('current_record','reference t_area',readable=False,writable=False))

########################################
db.define_table('t_estado',
    Field('f_nombre', type='string', notnull=True,
          label=T('Nombre')),
    auth.signature,
    format='%(f_nombre)s',
    migrate=settings.migrate)

db.define_table('t_estado_archive',db.t_estado,Field('current_record','reference t_estado',readable=False,writable=False))

########################################
db.define_table('t_condicion',
    Field('f_tipo', type='string', notnull=True,
          label=T('Tipo')),
    auth.signature,
    format='%(f_tipo)s',
    migrate=settings.migrate)

db.define_table('t_condicion_archive',db.t_condicion,Field('current_record','reference t_condicion',readable=False,writable=False))

########################################
db.define_table('t_comunidad',
    Field('f_nombre', type='string', notnull=True,
          label=T('Nombre')),
    Field('f_estado', type='reference t_estado', notnull=True,
          label=T('Estado')),
    Field('f_descripcion', type='text', notnull=True,
          label=T('Descripcion')),
    Field('f_cantidadbeneficiados', type='integer', notnull=True,
          label=T('Cantidadbeneficiados')),
    auth.signature,
    format='%(f_nombre)s',
    migrate=settings.migrate)

db.define_table('t_comunidad_archive',db.t_comunidad,Field('current_record','reference t_comunidad',readable=False,writable=False))

########################################
db.define_table('t_proponente',
    Field('f_tipoprop', type='reference t_tipoprop', notnull=True,
          label=T('Tipoprop')),
    Field('f_user', type='reference auth_user', notnull=True,
        label=T('Nombre de usuario')),
    Field('f_cedula', type='string', notnull=True,
          label=T('Cedula')),
    Field('f_nombre', type='string', notnull=True,
          label=T('Nombre')),
    Field('f_apellido', type='string', notnull=True,
          label=T('Apellido')),
    Field('f_email', type='string', notnull=True,
          label=T('Email')),
    Field('f_sexo', type='reference t_sexo', notnull=True,
          label=T('Sexo')),
    Field('f_telefono', type='string', notnull=True,
          label=T('Telefono')),
    auth.signature,
    format='%(f_tipoprop)s',
    migrate=settings.migrate)

db.define_table('t_proponente_archive',db.t_proponente,Field('current_record','reference t_proponente',readable=False,writable=False))

########################################
db.define_table('t_project',
    Field('f_codigo',notnull=True,
          label=T('Codigo')),
   # Field('f_proyecto', type='reference t_proyecto', notnull=True,
    #      label=T('Proyecto')),
    Field('f_nombre', type='string', notnull=True,
          label=T('Nombre'),default = ''),
    Field('f_descripcion', type='text', notnull=True,
          label=T('Descripcion')),
    Field('f_area', type='reference t_area', notnull=True,
          label=T('Area')),
    Field('f_estado', type='reference t_estado', notnull=True,
          label=T('Estado')),
    Field('f_tutor', type='reference t_tutor', notnull=True,
          label=T('Tutor')),
    Field('f_fechaini', type='date', notnull=True,
          label=T('Fechaini')),
    Field('f_fechafin', type='date',notnull=True,
          label=T('Fechafin')),
    Field('f_version',notnull=True,
          label=T('Version')),
    Field('f_comunidad', type='reference t_comunidad', notnull=True,
          label=T('Comunidad')),
    Field('f_proponente', type='reference t_proponente', notnull=True,
          label=T('Proponente')),
    auth.signature,
    format='%(f_codigo)s',
    #primarykey=['f_version','f_codigo'],
    migrate=settings.migrate)
db.define_table('t_project_archive',db.t_project,Field('current_record','reference t_project',readable=False,writable=False))
#db.define_table('t_caracteristicas_archive',db.t_caracteristicas,Field('current_record','reference t_caracteristicas',readable=False,writable=False))

########################################
db.define_table('t_carrera',
    Field('f_codigo', type='string', notnull=True,
          label=T('Codigo')),
    auth.signature,
    format='%(f_codigo)s',
    migrate=settings.migrate)

db.define_table('t_carrera_archive',db.t_carrera,Field('current_record','reference t_carrera',readable=False,writable=False))

########################################
db.define_table('t_estudiante',
    Field('f_usbid', type='string', notnull=True,
          label=T('Usbid')),
    Field('f_user', type='reference auth_user', notnull=True,
        label=T('Nombre de usuario')),
    Field('f_nombre', type='string', notnull=True,
          label=T('Nombre')),
    Field('f_apellido', type='string', notnull=True,
          label=T('Apellido')),
    Field('f_cedula', type='string', notnull=True,
          label=T('Cedula')),
    Field('f_carrera', type='reference t_carrera', notnull=True,
          label=T('Carrera')),
    Field('f_sede', type='reference t_sede', notnull=True,
          label=T('Sede')),
    Field('f_email', type='string', notnull=True,
          label=T('Email')),
    Field('f_sexo', type='reference t_sexo', notnull=True,
          label=T('Sexo')),
    Field('f_telefono', type='string', notnull=True,
          label=T('Telefono')),
    Field('f_direccion', type='text', notnull=True,
          label=T('Direccion')),
    auth.signature,
    format='%(f_usbid)s',
    migrate=settings.migrate)

db.define_table('t_estudiante_archive',db.t_estudiante,Field('current_record','reference t_estudiante',readable=False,writable=False))

########################################
db.define_table('t_relacionestproy',
    Field('f_tipo', type='string', notnull=True,
          label=T('Tipo')),
    auth.signature,
    format='%(f_tipo)s',
    migrate=settings.migrate)

db.define_table('t_relacionestproy_archive',db.t_relacionestproy,Field('current_record','reference t_relacionestproy',readable=False,writable=False))

########################################
db.define_table('t_cursa',
    Field('f_estudiante', type='reference t_estudiante', notnull=True,
          label=T('Estudiante')),
    Field('f_project', type='reference t_project', notnull=True,
          label=T('Project')),
    Field('f_state', type='reference t_relacionestproy', notnull=True,
          label=T('State')),
    auth.signature,
    format='%(f_estudiante)s',
    migrate=settings.migrate)

db.define_table('t_cursa_archive',db.t_cursa,Field('current_record','reference t_cursa',readable=False,writable=False))
>>>>>>> origin/Login_vista_daniel

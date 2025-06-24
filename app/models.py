# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Actores(models.Model):
    actorid = models.AutoField(db_column='ActorID', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=255)  # Field name made lowercase.
    fechanacimiento = models.DateField(db_column='FechaNacimiento', blank=True, null=True)  # Field name made lowercase.
    biografia = models.TextField(db_column='Biografia', blank=True, null=True)  # Field name made lowercase.
    imagen = models.ImageField(upload_to='actores/',blank=True,null=True)

    class Meta:
        
        db_table = 'actores'


class Peliculas(models.Model):
    peliculaid = models.AutoField(db_column='PeliculaID', primary_key=True)  # Field name made lowercase.
    titulo = models.CharField(db_column='Titulo', max_length=255)  # Field name made lowercase.
    titulooriginal = models.CharField(db_column='TituloOriginal', max_length=255, blank=True, null=True)  # Field name made lowercase.
    aniolanzamiento = models.IntegerField(db_column='AnioLanzamiento', blank=True, null=True)  # Field name made lowercase.
    director = models.CharField(db_column='Director', max_length=255, blank=True, null=True)  # Field name made lowercase.
    guionista = models.CharField(db_column='Guionista', max_length=255, blank=True, null=True)  # Field name made lowercase.
    genero = models.CharField(db_column='Genero', max_length=100, blank=True, null=True)  # Field name made lowercase.
    sinopsis = models.TextField(db_column='Sinopsis', blank=True, null=True)  # Field name made lowercase.
    clasificacion = models.CharField(db_column='Clasificacion', max_length=10, blank=True, null=True)  # Field name made lowercase.
    duracionminutos = models.IntegerField(db_column='DuracionMinutos', blank=True, null=True)  # Field name made lowercase.
    idiomaoriginal = models.CharField(db_column='IdiomaOriginal', max_length=50, blank=True, null=True)  # Field name made lowercase.
    paisproduccion = models.CharField(db_column='PaisProduccion', max_length=100, blank=True, null=True)  # Field name made lowercase.
    fecharegistro = models.DateTimeField(db_column='FechaRegistro', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        
        db_table = 'peliculas'


class Peliculasactores(models.Model):
    peliculaactorid = models.AutoField(db_column='PeliculaActorID', primary_key=True)  # Field name made lowercase.
    peliculaid = models.ForeignKey(Peliculas, models.DO_NOTHING, db_column='PeliculaID', blank=True, null=True)  # Field name made lowercase.
    actorid = models.ForeignKey(Actores, models.DO_NOTHING, db_column='ActorID', blank=True, null=True)  # Field name made lowercase.
    personaje = models.CharField(db_column='Personaje', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        
        db_table = 'peliculasactores'


class Peliculaspremios(models.Model):
    peliculapremioid = models.AutoField(db_column='PeliculaPremioID', primary_key=True)  # Field name made lowercase.
    peliculaid = models.ForeignKey(Peliculas, models.DO_NOTHING, db_column='PeliculaID', blank=True, null=True)  # Field name made lowercase.
    premioid = models.ForeignKey('Premios', models.DO_NOTHING, db_column='PremioID', blank=True, null=True)  # Field name made lowercase.
    ganador = models.IntegerField(db_column='Ganador', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        
        db_table = 'peliculaspremios'


class Premios(models.Model):
    premioid = models.AutoField(db_column='PremioID', primary_key=True)  # Field name made lowercase.
    nombrepremio = models.CharField(db_column='NombrePremio', max_length=255)  # Field name made lowercase.
    anioceremonia = models.IntegerField(db_column='AnioCeremonia', blank=True, null=True)  # Field name made lowercase.
    categoria = models.CharField(db_column='Categoria', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        
        db_table = 'premios'


class Produccion(models.Model):
    produccionid = models.AutoField(db_column='ProduccionID', primary_key=True)  # Field name made lowercase.
    peliculaid = models.ForeignKey(Peliculas, models.DO_NOTHING, db_column='PeliculaID', blank=True, null=True)  # Field name made lowercase.
    productora = models.CharField(db_column='Productora', max_length=255, blank=True, null=True)  # Field name made lowercase.
    distribuidora = models.CharField(db_column='Distribuidora', max_length=255, blank=True, null=True)  # Field name made lowercase.
    presupuesto = models.DecimalField(db_column='Presupuesto', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    recaudacion = models.DecimalField(db_column='Recaudacion', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        
        db_table = 'produccion'


class Resenasusuarios(models.Model):
    resenaid = models.AutoField(db_column='ResenaID', primary_key=True)  # Field name made lowercase.
    usuarioid = models.ForeignKey('Usuarios', models.DO_NOTHING, db_column='UsuarioID', blank=True, null=True)  # Field name made lowercase.
    peliculaid = models.ForeignKey(Peliculas, models.DO_NOTHING, db_column='PeliculaID', blank=True, null=True)  # Field name made lowercase.
    calificacion = models.DecimalField(db_column='Calificacion', max_digits=2, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    comentario = models.TextField(db_column='Comentario', blank=True, null=True)  # Field name made lowercase.
    fecharesena = models.DateTimeField(db_column='FechaResena', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        
        db_table = 'resenasusuarios'


class Usuarios(models.Model):
    usuarioid = models.AutoField(db_column='UsuarioID', primary_key=True)  # Field name made lowercase.
    nombreusuario = models.CharField(db_column='NombreUsuario', unique=True, max_length=50)  # Field name made lowercase.
    correoelectronico = models.CharField(db_column='CorreoElectronico', unique=True, max_length=100, blank=True, null=True)  # Field name made lowercase.
    fecharegistro = models.DateTimeField(db_column='FechaRegistro', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        
        db_table = 'usuarios'

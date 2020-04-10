from django.db import models

# Create your models here.
# Esta clase representa una tabla de base de dato
class Project(models.Model):
    # columnas
    title = models.CharField(max_length = 50, verbose_name = "Titulo") # Cadena de caracteres
    description = models.TextField(verbose_name = "Descripcion")
    image = models.ImageField(verbose_name = "Imagen", upload_to='projects')
    link = models.URLField(verbose_name ="Direccion web" ,null=True, blank=True)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
    

    class Meta:
        verbose_name = 'proyecto'
        verbose_name_plural = 'proyectos'
        ordering = ["-created"]

    def __str__(self):
        return self.title
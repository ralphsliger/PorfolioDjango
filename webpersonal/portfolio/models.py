from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=200,verbose_name="Titulo")
    description = models.TextField(verbose_name="Descripcion")
    image = models.ImageField(verbose_name="Imagen", upload_to="projects")
    link = models.URLField(verbose_name="Direccion web", null= True, blank=True)
    created = models.DateField(auto_now_add=True, verbose_name="Fecha de Creacion")
    updated = models.DateField(auto_now=True, verbose_name="Fecha Edicion")
    

    class Meta:
        verbose_name = "Proyecto"
        verbose_name_plural = "Proyectos"
        ordering = ["-created"]

    def __str__(self):
        return self.title   
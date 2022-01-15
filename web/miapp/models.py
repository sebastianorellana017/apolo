from django.db import models
from django.contrib.auth.models import User
# Create your models her
# e.
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre')
    
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.name

class Article(models.Model):
    user = models.ForeignKey(User, verbose_name='Usuario', blank=True, null=True, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category, verbose_name="Categorias", blank=True) 
    title = models.CharField(max_length=150, blank=True, null=True, verbose_name="Titulo")
    image = models.ImageField(default='null', verbose_name="Imagen", upload_to="articles")
    public = models.BooleanField(verbose_name='Publicado?')
    create_at = models.DateTimeField(auto_now_add=True, verbose_name="Creado el")
    update_at = models.DateTimeField(auto_now=True, verbose_name="Editado el")
    order = models.IntegerField(default=0, verbose_name="Orden")

    class Meta:
        verbose_name = 'Articulo'
        verbose_name_plural = 'Articulos'
        ordering = ["-id"]

    def __str__(self):
        return self.title

    
    
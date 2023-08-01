from django.db import models
from apps.usuarios.models import Usuario
#NO OLVIDAR IMPORTAR EL USUARIO PARA USARLO COMO AUTOR

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre

class Noticia(models.Model):
    titulo = models.CharField(max_length=250)
    resumen = models.CharField(max_length=100)
    contenido = models.TextField()
    fecha_de_publicacion = models.DateTimeField(auto_now_add=True)
    #imagen = models.ImageField(upload_to= 'noticias', default = bojack_foto_de_perfil.url)
    categoria_noticia = models.ForeignKey(Categoria, on_delete= models.CASCADE) #SET_NULL
    author = models.ForeignKey(Usuario, on_delete=models.CASCADE, default=Usuario.objects.get(is_superuser=True).pk) 
  
    def __str__(self):
        return self.titulo
    
class Comment(models.Model):
    noticia = models.ForeignKey(Noticia, on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=100)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.text



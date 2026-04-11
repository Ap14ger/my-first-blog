# Todas las líneas que comienzan con from o import son líneas para agregar algo de otros archivo

from django.conf import settings
from django.db import models
from django.utils import timezone

# Todo este bloque es lo que se define como un objeto.


class Post(models.Model):  # models.Model significa que Post es un modelo de Django
    # este es una relación (link) con otro modelo.
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # así es como defines un texto con un número limitado de caracteres.
    title = models.CharField(max_length=200)
    # este es para texto largo sin límite. Suena perfecto para el contenido de la entrada del blog
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    # este es fecha y hora.
    published_date = models.DateTimeField(blank=True, null=True)

    # las funciones son las que se definen como methodos

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

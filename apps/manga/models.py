from django.db import models

class Manga(models.Model):
    titulo = models.CharField(max_length=255)
    Autor = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    ultima_atualizacao= models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo

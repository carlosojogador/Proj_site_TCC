from django.db import models

#classe que ira se transformar em uma tabela no banco de dados

class Comentario(models.Model):

    id_comentario = models.AutoField(primary_key=True)

    nome = models.TextField(max_length=255)

    comentario = models.TextField(max_length=255)

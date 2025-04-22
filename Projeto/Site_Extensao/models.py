from django.db import models
from django.contrib.auth.models import User  # Importando o modelo User

class Curso(models.Model):
    nome = models.CharField(max_length=255)
    carga_horaria = models.IntegerField()
    data_inicio = models.DateField()
    data_fim = models.DateField()
    anotacoes = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)  # Relacionamento com o modelo User

    def __str__(self):
        return self.nome

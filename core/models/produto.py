from django.db import models

from .categoria import Categoria


class Produto(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=225)
    preco = models.DecimalField(max_digits=10, decimal_places=2, null=True, default=0)
    categoria = models.ForeignKey(
        Categoria, on_delete=models.PROTECT, related_name="produto", null=True, blank=True
    )

    def __str__(self):
        return f"({self.categoria}) {self.nome}"
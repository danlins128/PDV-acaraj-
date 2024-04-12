from django.db import models

# Create your models here.
class Usuario(models.Model):
    nome = models.CharField(max_length=40)
    senha = models.CharField(max_length=16)
    tipo_usuario = models.CharField(max_length=10)

class Produto(models.Model):
    tipo_produto = models.CharField(max_length=20)
    nome = models.CharField(max_length=20)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade_em_estoque = models.IntegerField()


class Venda(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    data_hora = models.DateTimeField(auto_now_add=True)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)

class ItemVenda(models.Model):
    venda = models.ForeignKey(Venda, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.IntegerField()
    valor_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    valor_total_item = models.DecimalField(max_digits=10, decimal_places=2)

    
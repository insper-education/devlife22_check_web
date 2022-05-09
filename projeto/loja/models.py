from django.db import models
from django.core.validators import MinValueValidator

class Produto(models.Model):
    # TODO

    def __str__(self):
        return self.nome

class Cliente(models.Model):
    # TODO 

    def __str__(self):
        return self.nome

class Pedido(models.Model):
    cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE)
    valor_total = models.DecimalField(max_digits=20, decimal_places=2, default=0.0)
    pago = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)+ " --- "+ str(self.cliente) + " --- " + str(self.valor_total)

class ItemPedido(models.Model):
    produto = models.ForeignKey('Produto', on_delete=models.PROTECT)
    pedido = models.ForeignKey('Pedido', on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField(validators=[MinValueValidator(1)])

    class Meta:
        unique_together = ('pedido', 'produto')

    def __str__(self):
        return f"({self.pedido}) - ({self.produto})"
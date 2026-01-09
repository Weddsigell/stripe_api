from django.core.validators import MinValueValidator
from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=255, null=False)
    discription = models.TextField(null=False)
    price = models.PositiveIntegerField(
        validators=[MinValueValidator(51)],
        help_text="Цена в центах (минимум 51 = $0.51)",
    )

    class Meta:
        verbose_name = "Item"
        verbose_name_plural = "Items"

    def __str__(self):
        return f"{self.name} | {self.price}"

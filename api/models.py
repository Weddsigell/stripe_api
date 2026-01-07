from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=255, null=False)
    discription = models.TextField(null=False)
    price = models.PositiveIntegerField()

    class Meta:
        verbose_name = "Item"
        verbose_name_plural = "Items"

    def __str__(self):
        return f"{self.name} | {self.price}"

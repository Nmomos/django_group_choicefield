from django.db import models


class ColorType(models.Model):
    name = models.CharField(max_length=30)
    parent = models.ForeignKey(
        'ColorType', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


class Expense(models.Model):
    name = models.DecimalField(max_digits=10, decimal_places=2)
    birthday = models.DateField()
    colortype = models.ForeignKey(ColorType, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

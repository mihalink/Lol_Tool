from django.db import models


# Create your models here.
class Transformer(models.Model):
    transf_loc = models.CharField(max_length=20)
    sku = models.PositiveIntegerField()
    primary_voltage = models.CharField(max_length=20)
    size_kva = models.CharField(max_length=20, null=True)
    transformer_age = models.CharField(max_length=20, null=True)
    customers = models.CharField(max_length=20, null=True)
    percent_lol = models.CharField(max_length=20, null=True)
    consecutive_months_overloaded = models.CharField(max_length=20, null=True)
    loss_of_life = models.CharField(max_length=20, null=True)
    max_overload = models.CharField(max_length=20, null=True)
    life_expectancy_at_conditions = models.CharField(max_length=20, null=True)
    date_max_overload = models.CharField(max_length=20, null=True)
    loading_flags = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.transf_loc

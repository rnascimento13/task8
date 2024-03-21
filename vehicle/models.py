from django.db import models

class VehicleBrand(models.Model):
    name = models.CharField(max_length=100, verbose_name='Marca do veículo')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Marca do veículo'
        verbose_name_plural = 'Marcas dos veículos'

class VehicleModel(models.Model):
    brand = models.ForeignKey(VehicleBrand, on_delete=models.CASCADE, verbose_name='Marca do veículo')
    name = models.CharField(max_length=100, verbose_name='Modelo')

    def __str__(self):
        return f"{self.brand} - {self.name}"

    class Meta:
        verbose_name = 'Modelo'
        verbose_name_plural = 'Modelos'


class VehicleColor(models.Model):
    name = models.CharField(max_length=50, verbose_name='Cor')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Cor'
        verbose_name_plural = 'Cores'

class VehicleCondition(models.Model):
    name = models.CharField(max_length=50, verbose_name='Condição do veículo')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Condição do veículo'
        verbose_name_plural = 'Condições dos veículos'

class Vehicle(models.Model):
    model = models.ForeignKey(VehicleModel, on_delete=models.CASCADE, verbose_name='Modelo')
    year = models.IntegerField(verbose_name='Ano do modelo')
    color = models.ForeignKey(VehicleColor, on_delete=models.CASCADE, verbose_name='Cor')
    purchase_year = models.IntegerField(verbose_name='Ano da compra')
    condition = models.ForeignKey(VehicleCondition, on_delete=models.CASCADE, verbose_name='Condição do veículo')
    
    def __str__(self):
        return f"{self.model} - {self.year}"

    class Meta:
        verbose_name = 'Veículo'
        verbose_name_plural = 'Veículos'


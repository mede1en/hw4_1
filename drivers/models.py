from django.db import models
from cars_of_facts.models import Car

class DriverModel(models.Model):
    name_driver= models.CharField(max_length=100, verbose_name="ФИО")
    image = models.ImageField(upload_to='drivers_images/')
    date_of_birth = models.DateField()
    choose_car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='drivers')
    experience = models.IntegerField(verbose_name="Стаж вождения (лет)")

    STATUS_RIGHTS =(
        ('Есть','Есть'),
        ('Нет','Нет'),
    )

    status_rights = models.CharField(max_length=50, choices=STATUS_RIGHTS, verbose_name="Наличие водительских прав")

    def __str__(self):
        return self.name_driver

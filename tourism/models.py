from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=100, verbose_name="Введите имя")
    phone = models.CharField(max_length=20, verbose_name="Введите номер телефона")

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Tour(models.Model):
    title = models.CharField(max_length=200, verbose_name="Введите название тура")
    description = models.TextField(verbose_name="Введите описание тура")
    price = models.PositiveIntegerField(verbose_name="Введите цену")
    date = models.DateField(verbose_name="Введите дату тура")

    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.title


class Booking(models.Model):
    person = models.OneToOneField(
        Person,
        on_delete=models.CASCADE
    )
    tour = models.ForeignKey(
        Tour,
        on_delete=models.CASCADE
    )
    booking_date = models.DateField()

    def __str__(self):
        return f"{self.person} -> {self.tour}"



class Review(models.Model):
    tour = models.ForeignKey(
        Tour,
        on_delete=models.CASCADE,
        related_name="reviews"
    )
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    text = models.TextField()
    rating = models.PositiveIntegerField()

    def __str__(self):
        return f"Review by {self.person}"

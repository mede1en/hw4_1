from django.db import models

class Car(models.Model):
    name = models.CharField(max_length=100, verbose_name="название машины")
    description = models.TextField(verbose_name='укажите описание машины')
    manufacturer = models.CharField(max_length=100, verbose_name="производитель")
    year = models.IntegerField(verbose_name="Год выпуска")

    CATEGOTY_CARS = (
        ('(А)мини-автомобили', '(А)мини-автомобили'),
        ('(B)городские автомобили', '(B)городские автомобили'),
        ('(C)среднеразмерные авто ', '(C)среднеразмерные авто '),
        ('(D)семейные авто', '(D)семейные авто'),
        ('(E)бизнес-класс', '(E)бизнес-класс'),
        ('(F)люксовые', '(F)люксовые'),
        ('(S)спортивные', '(S)спортивные'),
        ('(M)минивэны', '(M)минивэны'),
        ('(J)кроссоверы', '(J)кроссоверы'),
        ('(SUV)внедорожники', '(SUV)внедорожники'),
    )

    category = models.CharField(max_length=100, choices=CATEGOTY_CARS, verbose_name="Категория")
    color = models.CharField(max_length=50, verbose_name="Цвет")
    image = models.ImageField(upload_to='car_images/', verbose_name="Изображение машины")
    url_car = models.URLField(verbose_name='укажите ссылку на обзор машины')
    price = models.IntegerField(verbose_name="Цена")
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Машину"
        verbose_name_plural = "Машины"
from django.db import models


class Categories(models.Model):
    name = models.CharField(max_length=200, verbose_name='Категория')
    no_size = models.BooleanField(default=False, verbose_name='Без размера')

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Color(models.Model):
    name = models.CharField(max_length=200,
                            verbose_name='Цвет')

    class Meta:
        verbose_name = 'Цвет'
        verbose_name_plural = 'Цвета'


class Size(models.Model):
    name = models.CharField(max_length=200,
                            verbose_name='Размер')

    class Meta:
        verbose_name = 'Размер'
        verbose_name_plural = 'Размеры'


class Products(models.Model):
    name = models.CharField(max_length=200,
                            verbose_name='Название блюда')
    category = models.ForeignKey(Categories,
                                 on_delete=models.CASCADE,
                                 related_name='products',
                                 verbose_name='Категория')
    color = models.ForeignKey(Color,
                              on_delete=models.CASCADE,
                              related_name='products',
                              verbose_name='Цвет')
    # size = models.ForeignKey(Size,
    #                          on_delete=models.CASCADE,
    #                          blank=True,
    #                          null=True,
    #                          related_name='products',
    #                          verbose_name='Размер')
    image = models.ImageField(upload_to='media/img/%Y/%m',
                              null=True,
                              blank=True,
                              verbose_name='Фотография')
    price = models.DecimalField(max_digits=12,
                                decimal_places=2,
                                verbose_name='Цена')

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товар'

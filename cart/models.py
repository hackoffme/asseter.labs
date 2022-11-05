from django.db import models
from django.contrib.auth.models import User

from catalog import models as catalog


# Корзнина:
# - id
# - Пользователь
# - Состав
# Под составом имеется ввиду четрые поля item, color, size, quantity или отдельная таблица с этими же полями и связью fk
# на эту таблицу?
class Cart(models.Model):
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE)
    item = models.ForeignKey(catalog.Products,
                             on_delete=models.CASCADE)
    color = models.ForeignKey(catalog.Color,
                              on_delete=models.CASCADE)
    size = models.ForeignKey(catalog.Size,
                             on_delete=models.CASCADE)
    quantity = models.IntegerField()

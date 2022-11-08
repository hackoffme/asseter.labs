from django.db import models
from django.contrib.auth.models import User

from catalog import models as catalog



class Cart(models.Model):
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE)
    item = models.ForeignKey(catalog.Products,
                             on_delete=models.CASCADE)
    size = models.ForeignKey(catalog.Size,
                             blank=True,
                             null=True,
                             on_delete=models.CASCADE)
    quantity = models.IntegerField()

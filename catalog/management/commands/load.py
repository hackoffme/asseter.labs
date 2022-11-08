import logging
from random import randint
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from faker import Faker

from catalog import models

logging.getLogger('faker').setLevel(logging.ERROR)

fake = Faker('ru_RU')


class Command(BaseCommand):
    help = 'load data'

    def handle(self, *args, **options):
        color = [models.Color.objects.create(name=i) for i in [
            'Черный', 'Белый', 'Красный']]
        cat = [models.Categories.objects.create(
            name=i) for i in ['Одежда', 'Обувь']]
        cat.append(models.Categories.objects.create(name='Головные уборы', no_size=True))
        size = [models.Size.objects.create(name=i)
                for i in ['XS', 'S', 'M', 'L']]
        for _ in range(20):
            models.Products.objects.create(
                name=fake.word(),
                category=cat[randint(0, len(cat)-1)],
                color=color[randint(0, len(color)-1)],
                # size=size[randint(0, len(size)-1)],
                image=fake.image_url(),
                price=randint(100, 10000)
            )
        User.objects.create_user(
            username='admin', password='fghgfhhuser123', email='af@df.dd', is_staff=True)
        User.objects.create_user(
            username='user', password='fghgfhhuser123', email='af@df.dd', is_staff=False)

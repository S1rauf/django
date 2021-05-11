from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
# Create your models here.

User =get_user_model()


class order_material(models.Model):

    material = models.CharField(max_length=255, verbose_name='Наименование материала')
    unit = models.CharField(max_length=5, verbose_name='Единица измерения')
    objec = models.CharField(max_length=255, verbose_name='Объект')
    persona_1 = models.PositiveSmallIntegerField( verbose_name='Работник 1')

    def __str__(self):
        return self.material
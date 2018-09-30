import uuid
from django.db import models


# Create your models here.
class Beacon(models.Model):
    """
    Пункты меню сверху
    """
    title = models.CharField('Название маячка', max_length=50)
    UUID = models.UUIDField('UUID маячка', default=uuid.uuid4, editable=False)
    description = models.TextField('Описание', null=True, blank=True)

    class Meta:
        ordering = ('title',)
        verbose_name = "Маячок"
        verbose_name_plural = "Маячки"

    def __str__(self):
        return self.title

from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Genre(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name="ID жанра")
    uuid = models.UUIDField(verbose_name="UUID жанра")
    name = models.CharField(max_length=255, verbose_name="Название жанров")
    is_root = models.BooleanField(default=False, verbose_name="Корневой ли?")
    url = models.CharField(max_length=255, verbose_name="URL жанра")
    is_main = models.BooleanField(default=False, verbose_name="Основной ли?")

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"

    def __str__(self): return self.name

class Publisher(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name="ID издательства")
    name = models.CharField(max_length=255, verbose_name="Название издательства")
    url = models.CharField(max_length=255, verbose_name="URL издательства", blank=True, null=True)

    class Meta:
        verbose_name = "Издательство"
        verbose_name_plural = "Издательства"

    def __str__(self): return self.name

class Copyrighter(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name="ID копирайтера", blank=True)
    name = models.CharField(max_length=255, verbose_name="Название копирайтера")
    url = models.CharField(max_length=255, verbose_name="URL", blank=True, null=True)

    class Meta:
        verbose_name = "Копирайтер"
        verbose_name_plural = "Копирайтеры"

    def __str__(self): return self.name


class Rightholder(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name="ID правообладателя")
    name = models.CharField(max_length=255, verbose_name="Название")
    url = models.CharField(max_length=255, verbose_name="URL", blank=True, null=True)

    class Meta:
        verbose_name = "Правообладатель"
        verbose_name_plural = "Правообладатели"

    def __str__(self): return self.name
